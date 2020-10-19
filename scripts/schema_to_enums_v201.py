#!/usr/bin/env python
import sys
import re
import json
from pathlib import Path

enum_types = []
enum_types_names = []


def create_attribute(name, casing_style="snake_case"):
    """
    Gets an attribute name from the enum an convert it to snake_case, by
    default, or to CamelCase
    """
    # Removes any hyphens or dots from the name, substituting by an underscore
    name_normalized = re.sub('[-.]', '_', name)
    if casing_style == "CamelCase":
        name_converted = name_normalized[0].lower() + name_normalized[1:]
    else:
        # Assumes the variable name is a concatenation of
        # capitalized terms, e.g., "CamelCase" or "SuperHyperMega"
        name_converted = re.sub('([a-z0-9])([A-Z])', r'\1_\2',
                                name_normalized).lower()

    return Attribute(name, name_converted)


class NormalClass:
    def __init__(self, name):
        self.name = name
        self.attrs = []

    def add_attr(self, attr):
        self.attrs.append(attr)

    def __str__(self):
        output = f"class {self.name}(str, Enum):\n"

        if len(self.attrs) == 0:
            return output + "    pass\n"

        for attr in self.attrs:
            output += str(attr)

        return output


class Attribute:
    def __init__(self, name, name_converted):
        self.name = name
        self.name_converted = name_converted

    def __str__(self):
        name = self.name
        if not re.match("^[a-zA-Z_]", self.name):
            name = "_" + self.name

        # The 4 spaces after the start of the string is to guarantee the proper
        # indentation
        return f'    {self.name_converted} = "{name}"\n'

    def __repr__(self):
        return f"<{self.name}, {self.name_converted}> "


def parse_schema(schema):
    with open(schema, "r") as f:
        schema = json.loads(f.read())

    try:
        definitions = schema['definitions']
    except KeyError:
        print("Error: No definitions field found on the schema")
        return

    for enum_type, value in definitions.items():
        if "Enum" in enum_type:
            type_name = enum_type.replace("Enum", '')
            if type_name not in enum_types_names:
                nc = NormalClass(type_name)
                for enum_attr in value['enum']:
                    attr = create_attribute(enum_attr)
                    nc.add_attr(attr)
                enum_types.append(nc)
                enum_types_names.append(nc.name)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Pass path to folder with schemas")
        sys.exit(-1)

    # The second argument of argv is the path for the schemas
    p = Path(sys.argv[1])
    schemas = list(p.glob("*.json"))

    # This loop will update the lists enum_types and enum_types_names:
    # The former contains the enum objects that are later parsed to the
    # enum.py, using the str representation. And the latter, is used to keep
    # track of the already processed Enums, avoiding data duplication
    for schema in schemas:
        parse_schema(schema)

    with open('enums.py', 'wb+') as f:
        f.write(b"from enum import Enum\n")
        for enum_type_ in sorted(enum_types,
                                 key=lambda enum_type: enum_type.name):
            f.write(b"\n\n")
            f.write(str(enum_type_).encode('utf-8'))

