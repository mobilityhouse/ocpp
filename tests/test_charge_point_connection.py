"""Tests for charge point ID extraction and connection handling.

These tests address the issues described in GitHub issue #751:
- Robust extraction of charge point IDs from WebSocket paths
- Connection exceptions propagate to consumers for proper handling
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from ocpp.charge_point import extract_charge_point_id
from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp_16
from ocpp.v16 import call_result
from ocpp.v16.enums import Action, RegistrationStatus

# ---------------------------------------------------------------------------
# Tests for extract_charge_point_id
# ---------------------------------------------------------------------------


class TestExtractChargePointId:
    """Test the extract_charge_point_id utility function."""

    def test_simple_path(self):
        """Standard OCPP path with just the charge point ID."""
        assert extract_charge_point_id("/CP001") == "CP001"

    def test_nested_path(self):
        """Path with prefix segments (e.g., /ocpp/CP001)."""
        assert extract_charge_point_id("/ocpp/CP001") == "CP001"

    def test_deeply_nested_path(self):
        """Deeply nested path still returns the last segment."""
        assert extract_charge_point_id("/api/v1/ocpp/CP001") == "CP001"

    def test_trailing_slash(self):
        """Trailing slash should not affect extraction."""
        assert extract_charge_point_id("/CP001/") == "CP001"

    def test_root_path_returns_none(self):
        """Root path '/' has no charge point ID."""
        assert extract_charge_point_id("/") is None

    def test_empty_string_returns_none(self):
        """Empty string has no charge point ID."""
        assert extract_charge_point_id("") is None

    def test_none_returns_none(self):
        """None input returns None."""
        assert extract_charge_point_id(None) is None

    def test_path_without_leading_slash(self):
        """Path without leading slash should still work."""
        assert extract_charge_point_id("CP001") == "CP001"

    def test_path_with_query_string(self):
        """Query strings should be stripped before extracting ID."""
        assert extract_charge_point_id("/CP001?token=abc123") == "CP001"

    def test_path_with_fragment(self):
        """Fragments should be stripped before extracting ID."""
        assert extract_charge_point_id("/CP001#section") == "CP001"

    def test_whitespace_only_segment(self):
        """Path with only whitespace segment returns None."""
        assert extract_charge_point_id("/   ") is None

    def test_charge_point_id_with_special_chars(self):
        """Charge point IDs can contain hyphens, underscores, etc."""
        assert extract_charge_point_id("/CP-001_v2") == "CP-001_v2"

    def test_charge_point_id_with_dots(self):
        """Charge point IDs can contain dots (serial numbers)."""
        assert extract_charge_point_id("/EVB-P12354.00.01") == "EVB-P12354.00.01"

    def test_multiple_slashes(self):
        """Multiple consecutive slashes should be handled gracefully."""
        assert extract_charge_point_id("///CP001") == "CP001"


# ---------------------------------------------------------------------------
# Tests for ChargePoint.start() connection handling
# ---------------------------------------------------------------------------


class TestChargePointStart:
    """Test that ChargePoint.start() propagates connection exceptions."""

    @pytest.mark.asyncio
    async def test_start_propagates_exception_on_connection_closed(self, connection):
        """start() should let connection exceptions propagate to the caller."""

        class MyCP(cp_16):
            @on(Action.boot_notification)
            def on_boot_notification(self, **kwargs):
                return call_result.BootNotification(
                    current_time="2025-01-01T00:00:00Z",
                    interval=10,
                    status=RegistrationStatus.accepted,
                )

        connection.recv = AsyncMock(side_effect=Exception("Connection closed"))

        cp = MyCP("CP001", connection)

        with pytest.raises(Exception):
            await cp.start()

    @pytest.mark.asyncio
    async def test_start_processes_messages_before_exception(self, connection):
        """start() should process messages until the connection raises."""
        messages_received = []

        class MyCP(cp_16):
            @on(Action.boot_notification)
            def on_boot_notification(self, **kwargs):
                messages_received.append("boot")
                return call_result.BootNotification(
                    current_time="2025-01-01T00:00:00Z",
                    interval=10,
                    status=RegistrationStatus.accepted,
                )

        boot_msg = (
            '[2,"123","BootNotification",'
            '{"chargePointVendor":"vendor","chargePointModel":"model"}]'
        )
        connection.recv = AsyncMock(
            side_effect=[boot_msg, Exception("Connection closed")]
        )

        cp = MyCP("CP001", connection)

        with pytest.raises(Exception):
            await cp.start()

        assert len(messages_received) == 1

    @pytest.mark.asyncio
    async def test_reconnection_with_new_instance(self, connection):
        """Simulates a charger reconnecting by creating a new ChargePoint."""
        connection.recv = AsyncMock(side_effect=Exception("Connection closed"))

        # First connection
        cp1 = cp_16("CP001", connection)
        with pytest.raises(Exception):
            await cp1.start()

        # Second connection (simulating reconnect with new websocket)
        connection2 = MagicMock()
        connection2.send = AsyncMock()
        connection2.recv = AsyncMock(side_effect=Exception("Connection closed"))

        cp2 = cp_16("CP001", connection2)
        with pytest.raises(Exception):
            await cp2.start()
