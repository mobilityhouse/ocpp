try:
    # breaking change introduced in python 3.11
    from enum import StrEnum
except ImportError:  # pragma: no cover
    from enum import Enum  # pragma: no cover

    class StrEnum(str, Enum):  # pragma: no cover
        pass  # pragma: no cover


class ControlMode(StrEnum):
    scheduled = "Scheduled"
    dynamic = "Dynamic"


class EnergyTransferMode(StrEnum):
    ac_single_phase = "AC_single_phase"
    ac_two_phase = "AC_two_phase"
    ac_three_phase = "AC_three_phase"
    dc = "DC"
    ac_single_phase_bpt = "AC_single_phase_BPT"
    ac_two_phase_bpt = "AC_two_phase_BPT"
    ac_three_phase_bpt = "AC_three_phase_BPT"
    dc_bpt = "DC_BPT"
    dc_acdp = "DC_ACDP"
    dc_acdp_bpt = "DC_ACDP_BPT"
    wpt = "WPT"


class MobilityNeedsMode(StrEnum):
    evcc = "EVCC"
    evcc_secc = "EVCC_SECC"


class Pricing(StrEnum):
    no_pricing = "NoPricing"
    absolute_pricing = "AbsolutePricing"
    price_levels = "PriceLevels"
