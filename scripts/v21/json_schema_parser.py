from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Optional, Union

Schema = dict
SubSchema = dict


class _NOT_SET:
    pass


NOT_SET = _NOT_SET()


def parse(name: str, schema: Schema) -> Object:
    """Parse `schema` as an `Object`."""
    return _parse_as_object(name, schema, schema)


def _parse_as_object(name: str, parent: SubSchema, schema: Schema) -> Object:
    properties = {}
    for attribute, sub_schema in parent.get("properties", {}).items():
        print(f"attribute: {attribute}")
        print(f"sub_schema: {sub_schema}")
        sub_schema_key = ""

        if sub_schema.get("type") == None:
            sub_schema["type"] = "string"

        if contains_reference(sub_schema):
            sub_schema, sub_schema_key = resolve_reference(sub_schema["$ref"], schema)

        if sub_schema == {}:
            type = Any()
        elif is_object(sub_schema):
            type = _parse_as_object(
                pascal_to_camel_case(sub_schema_key), sub_schema, schema
            )
        elif is_string(sub_schema):
            type = String.from_sub_schema(sub_schema)
        elif is_enum(sub_schema):
            type = Enum.from_sub_schema(sub_schema, sub_schema_key)
        elif is_integer(sub_schema):
            type = Integer.from_sub_schema(sub_schema)
        elif is_boolean(sub_schema):
            type = Boolean()
        elif is_number(sub_schema):
            type = Number.from_sub_schema(sub_schema)
        elif is_array(sub_schema):
            if contains_reference(sub_schema["items"]):
                _name = sub_schema["items"]["$ref"].split("/")[-1]

                sub_schema, sub_schema_key = resolve_reference(
                    sub_schema["items"]["$ref"], schema
                )
                if is_object(sub_schema):
                    type = _parse_as_object(_name, sub_schema, schema)
                elif is_enum(sub_schema):
                    type = Enum.from_sub_schema(sub_schema, sub_schema_key)
                else:
                    raise RuntimeError("HOOY")
            elif is_string(sub_schema["items"]):
                type = String.from_sub_schema(sub_schema["items"])
            elif is_integer(sub_schema["items"]):
                type = Integer.from_sub_schema(sub_schema["items"])
            else:
                raise RuntimeError(
                    f"No support for array of type {
                        sub_schema['items']} in {attribute}"
                )
            type = Array(
                type=type,
                min_items=sub_schema.get("minItems"),
            )

        else:
            raise RuntimeError(
                f"No support for {
                               sub_schema['type']} in {attribute}"
            )

        # TODO: add support for default value sub_schema['default']
        properties[attribute] = Property(
            type=type,
            required=attribute in parent.get("required", []),
            default=sub_schema.get("default", NOT_SET),
        )

    return Object(pascal_to_camel_case(name), properties)


@dataclass(frozen=True)
class Boolean:
    pass


@dataclass(frozen=True)
class String:
    max_length: Optional[int]

    @staticmethod
    def from_sub_schema(sub_schema: SubSchema) -> "String":
        if sub_schema.get("type") != "string":
            raise RuntimeError("sub schema is not a string")

        return String(sub_schema.get("maxLength"))


@dataclass(frozen=True)
class Enum:
    """Class modelling the Enum in JSON schema."""

    name: str
    variants: List[str]

    @staticmethod
    def from_sub_schema(schema: SubSchema, name: str) -> "Enum":
        """Create `Enum` from a json subschema that defines an enum.
        Such subschema looks like this:

        ```
        {
          "javaType": "UpdateFirmwareStatusEnum",
          "type": "string",
          "additionalProperties": false,
          "enum": [
            "Accepted",
            "Rejected",
            "AcceptedCanceled",
            "InvalidCertificate",
            "RevokedCertificate"
          ]
        }
        ```
        """
        return Enum(name=name, variants=schema["enum"])


@dataclass(frozen=True)
class Object:
    name: str
    properties: dict[str, "Property"]


@dataclass(frozen=True)
class Integer:
    minimum: Optional[None]
    maximum: Optional[None]

    @staticmethod
    def from_sub_schema(sub_schema: SubSchema) -> "Integer":
        if sub_schema.get("type") != "integer":
            raise RuntimeError("sub schema is not a string")

        return Integer(sub_schema.get("minimum"), sub_schema.get("maximum"))


@dataclass(frozen=True)
class Number:
    minimum: Optional[None]
    maximum: Optional[None]

    @staticmethod
    def from_sub_schema(sub_schema: SubSchema) -> "Number":
        if sub_schema.get("type") != "number":
            raise RuntimeError("sub schema is not a string")

        return Number(sub_schema.get("minimum"), sub_schema.get("maximum"))


@dataclass(frozen=True)
class Array:
    type: Union[Object, Integer, String]
    min_items: Optional[int]


@dataclass(frozen=True)
class Any:
    pass


@dataclass(frozen=True)
class Property:
    type: Union[String, Object, Integer, Boolean, Array, Any]
    required: bool
    default: Any = NOT_SET

    def has_default_value(self) -> bool:
        return self.default is not NOT_SET


def contains_reference(sub_schema: SubSchema) -> bool:
    return "$ref" in sub_schema.keys()


def is_object(sub_schema: SubSchema) -> bool:
    return sub_schema.get("type") == "object"


def is_string(sub_schema: SubSchema) -> bool:
    return (
        sub_schema.get("type") == None
        or sub_schema.get("type") == "string"
        and not "enum" in sub_schema.keys()
    )


def is_enum(sub_schema: SubSchema) -> bool:
    return sub_schema.get("type") == "string" and "enum" in sub_schema.keys()


def is_integer(sub_schema: SubSchema) -> bool:
    return sub_schema.get("type") == "integer"


def is_array(sub_schema: SubSchema) -> bool:
    return sub_schema.get("type") == "array"


def is_boolean(sub_schema: SubSchema) -> bool:
    return sub_schema.get("type") == "boolean"


def is_number(sub_schema: SubSchema) -> bool:
    return sub_schema.get("type") == "number"


def resolve_reference(reference: str, schema: Schema) -> tuple[SubSchema, str]:
    elements = reference.split("/")
    key = ""

    if elements[0] != "#":
        raise RuntimeError(f"Reference {reference} doesn't start with #")

    sub_schema = schema
    for element in elements[1:]:
        try:
            sub_schema = sub_schema[element]
            key = element
        except KeyError as e:
            raise RuntimeError(
                f"Failed to resolve reference {
                               reference}"
            ) from e

    return sub_schema, key


def pascal_to_camel_case(input: str) -> str:
    """Convert a pascalCase string to CamelCase.
    All letters of following abbreviations are capitalized:
        * AC
        * DC
        * EV
        * EVSE
        * V2X
        * VPN
    """
    if len(input) < 2:
        return input.upper()

    if input[0:4] in ["evse", "ocsp"]:
        return input[0:4].upper() + input[4:]

    # TODO: Handle cases like 'eventNotification", "eventData", "actualValue" etc.
    if input[0:2] in ["ac", "dc", "ev"]:
        return input[0:2].upper() + input[2:]

    if input[0:3] in ["v2x", "vpn", "apn"]:
        return input[0:3].upper() + input[3:]

    return input[0:1].upper() + input[1:]
