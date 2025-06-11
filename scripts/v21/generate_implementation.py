#!/usr/bin/env python
"""This scripts consumes json schemas provided by the Open Charge Alliance
and produces Python code for all data types in these schemas.

Each schema follows the following structure:

    {
      "properties": {
        "customData": {
          "$ref": "#/definitions/CustomDataType"
        },
        "type": {
          "$ref": "#/definitions/ResetEnumType"
        },
      },
      "required": [
        "type"
      ],
      "definitions": {
        "CustomDataType": {
          "type": "object",
          "properties": {
            "vendorId": {
              "type": "string",
              "maxLength": 255
            }
          },
          "required": [
            "vendorId"
          ]
        },
        "ResetEnumType": {
          "type": "string",
          "additionalProperties": false,
          "enum": [
            "Immediate",
            "OnIdle"
          ]
        }
      },
      ...
    }

First, this script iterates over each property in "properties" and resolve
the reference. Any references in the references (E.g. assume #/definitions/someObject also contains references) are resolved too.

Per schema, an `Object` is created Below you'll see a simplified representation of the such `Object`:

    Object(
        name="Reset",
        properties={
            "type": Property(
                type=Enum(...),
                required=True,
                ...
            ),
            "customData": Property(
                type=Object(...),
                required=False,
                ...
            )
        }
    )


Second, the list of `Object`s is passed to 4 code generators:
    * `generate_calls()`
    * `generate_call_results()`
    * `generate_enums()`
    * `generate_types()`

Each generater returns a `str` with valid Python code. The generators remove duplicate objects and enums, sort items alphabetically, generate import statements etc.

This Python code can be written to source files.
"""

import json
import pathlib
import sys

import click
from code_generator import (
    generate_call_results,
    generate_calls,
    generate_datatypes,
    generate_enums,
)
from json_schema_parser import Object, parse


@click.command()
@click.argument("input", type=click.Path(exists=True))
@click.option(
    "--output",
    help="folder for the generated code",
    type=click.Path(file_okay=False, dir_okay=True, writable=True),
)
def main(input: str, output: str):
    input: pathlib.Path = pathlib.Path(input)
    output: pathlib.Path = pathlib.Path(output)

    if input.is_dir():
        schema_files = input.glob("*json")
    elif input.is_file() and input.suffix == ".json":
        schema_files = [input]
    else:
        sys.exit(1)

    calls: list[Object] = []
    call_results: list[Object] = []

    for schema_file in schema_files:
        schema = json.load(schema_file.open(encoding="utf-8-sig"))

        if schema["$id"].endswith("Response"):
            name = schema["$id"].split(":")[-1][:-8]
            object = parse(name, schema)
            call_results.append(object)
        if schema["$id"].endswith("Request"):
            name = schema["$id"].split(":")[-1][:-7]
            object = parse(name, schema)
            calls.append(object)

        continue

    messages = calls + call_results
    (output / "call.py").write_text(generate_calls(calls))
    (output / "call_result.py").write_text(generate_call_results(call_results))
    (output / "enums.py").write_text(generate_enums(messages))
    (output / "datatypes.py").write_text(generate_datatypes(messages))


if __name__ == "__main__":
    main()
