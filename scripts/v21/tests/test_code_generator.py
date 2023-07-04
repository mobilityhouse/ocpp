""" Some of the tests in this module load schema files from scripts/v21/tests/fixtures,
generate code and compare that code against the 'golden files' in scripts/v21/tests/golden_files.

Let's say you realize that the code generator contains a bug: the enums generated for schema
TransactionEventRequest are incorrect. To use this schema in the the unit perform the following 2 steps:

1. Add a copy of the schema to scripts/v21/tests/fixtures/enums/TransactionEventRequest.json.
2. Create a Python file with the expected code output in scripts/v21/tests/golden_files/enums/TransactionEventRequest.py.

Now run the tests with `poetry run pytest scripts/v21/tests`.
"""
import json
import pathlib
import sys
from typing import List, Tuple

import pytest

PARENT_DIR = pathlib.Path(__file__).parent
FIXTURES_DIR = PARENT_DIR / "fixtures"
GOLDEN_FILES_DIR = PARENT_DIR / "golden_files"

sys.path.append(str(PARENT_DIR.absolute()))

from code_generator import (
    _camel_to_snake_case,
    generate_call_results,
    generate_calls,
    generate_datatypes,
    generate_enums,
)
from json_schema_parser import Object, parse


def _load_objects(path: pathlib.Path) -> List[Tuple[str, Object]]:
    """Load all schema files at `path` as `Object`s."""
    schema_files = sorted(path.glob("*.json"))

    objects = []

    for schema_file in schema_files:
        name = schema_file.stem
        schema = json.load(schema_file.open(encoding="utf-8-sig"))
        if name.endswith("Request"):
            name_without_suffix = name[:-7]
        elif name.endswith("Response"):
            name_without_suffix = name[:-8]
        else:
            raise RuntimeError(
                f"Schema file {schema_file} doesn't end with either 'Request.json' or 'Response.json'"
            )

        object = parse(name_without_suffix, schema)

        objects.append((name, object))

    return objects


@pytest.mark.parametrize("name, object", _load_objects(FIXTURES_DIR / "enums"))
def test_generate_enums(name: str, object: Object):
    code = generate_enums([object])
    compare_code_against_golden_file(code, GOLDEN_FILES_DIR / "enums" / f"{name}.py")


@pytest.mark.parametrize("name, object", _load_objects(FIXTURES_DIR / "datatypes"))
def test_generate_datatypes(name: str, object: Object):
    code = generate_datatypes([object])
    compare_code_against_golden_file(
        code, GOLDEN_FILES_DIR / "datatypes" / f"{name}.py"
    )


@pytest.mark.parametrize("name, object", _load_objects(FIXTURES_DIR / "calls"))
def test_generate_calls(name: str, object: Object):
    code = generate_calls([object])
    compare_code_against_golden_file(code, GOLDEN_FILES_DIR / "calls" / f"{name}.py")


@pytest.mark.parametrize("name, object", _load_objects(FIXTURES_DIR / "call_results"))
def test_generate_call_results(name: str, object: Object):
    code = generate_call_results([object])
    compare_code_against_golden_file(
        code, GOLDEN_FILES_DIR / "call_results" / f"{name}.py"
    )


@pytest.mark.parametrize(
    "input, output",
    [
        ("evseId", "evse_id"),
        ("prioritizedEMAIDs", "prioritized_emaids"),
        ("iso15118SchemaVersion", "iso_15118_schema_version"),
        ("evMinV2XEnergyRequest", "ev_min_v2x_energy_request"),
    ],
)
def test_camel_to_snake_case(input: str, output: str):
    assert _camel_to_snake_case(input) == output


def compare_code_against_golden_file(code: str, golden_file: pathlib.Path):
    """Verify that `code` matches the content of `golden_file`."""
    if not golden_file.exists():
        raise FileNotFoundError(f"Golden file '{golden_file}' doesn't exists")

    assert code == golden_file.open().read()
