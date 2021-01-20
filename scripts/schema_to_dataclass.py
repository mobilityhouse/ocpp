#!/usr/bin/env python
import sys
import re
import json
from pathlib import Path

map_schema_type_to_python = {
    "object": "Dict",
    "array": "List",
    "integer": "int",
    "string": "str",
    "number": "int",
    "boolean": "bool",
    "any": "Any",
}


def create_dataclass(name):
    return dataclass(name)


def create_attribute(name, type, required):
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

    type = map_schema_type_to_python[type]

    return attribute(name, type, required)


class dataclass:
    def __init__(self, name):
        self.name = name
        self.attrs = []

    def add_attr(self, attr):
        self.attrs.append(attr)

    def __str__(self):
        output = f"@dataclass\nclass {self.name}Payload:\n"

        if len(self.attrs) == 0:
            return output + "    pass\n"

        optional_attrs = ""
        for attr in self.attrs:
            if attr.required:
                output += str(attr)

            else:
                optional_attrs += str(attr)

        return output + optional_attrs


class attribute:
    def __init__(self, name, type, required):
        self.name = name
        self.type = type
        self.required = required

    def __str__(self):
        name = self.name
        if not re.match("^[a-zA-Z_]", self.name):
            name = "_" + self.name

        definition = f"    {name}: {self.type}"
        if self.required is True:
            definition += "\n"
        else:
            definition += " = None\n"

        return definition

    def __repr__(self):
        return f"<{self.name}, {self.type}, {self.required}> "


calls = []
call_results = []


def parse_schema(schema):
    with open(schema, "r") as f:
        schema = json.loads(f.read())

    name = schema['$id'].split(":")[-1]

    call = False
    call_result = False
    if name.endswith("Request"):
        call = True
        name = name[:-len("Request")]
    elif name.endswith("Response"):
        call_result = True
        name = name[:-len("Response")]

    dc = create_dataclass(name)
    try:
        properties = schema['properties']
    except KeyError:
        if call:
            calls.append(dc)
        elif call_result:
            call_results.append(dc)
        return

    for property, definition in properties.items():
        if property == "customData":
            continue
        required = True
        try:
            required = property in schema['required']
        except KeyError:
            required = False

        try:
            type = definition['type']
        except KeyError:
            try:
                ref = definition['$ref'].split('/')[-1]
                type = schema['definitions'][ref]['type']
            except KeyError:
                if definition == {}:
                    type = "any"

        attr = create_attribute(property, type, required)
        dc.add_attr(attr)

    if call:
        calls.append(dc)
    elif call_result:
        call_results.append(dc)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Pass path to folder with schemas")
        sys.exit(-1)

    p = Path(sys.argv[1])
    schemas = list(p.glob("*.json"))

    for schema in schemas:
        parse_schema(schema)

    with open('call.py', 'wb+') as f:
        f.write(b"from typing import Any, Dict, List\n")
        f.write(b"from dataclasses import dataclass, field, Optional\n")

        for call in sorted(calls, key=lambda call: call.name):
            f.write(b"\n\n")
            f.write(str(call).encode('utf-8'))

    with open('call_result.py', 'wb+') as f:
        f.write(b"from typing import Any, Dict, List\n")
        f.write(b"from dataclasses import dataclass, field\n")

        for call in sorted(call_results, key=lambda call: call.name):
            f.write(b"\n\n")
            f.write(str(call).encode('utf-8'))
