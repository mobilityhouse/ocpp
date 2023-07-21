import re
from typing import List, Union

from json_schema_parser import (
    Any,
    Array,
    Boolean,
    Enum,
    Integer,
    Number,
    Object,
    String,
)

# Tab's are 4 spaces.
TAB = "    "


def generate_calls(calls: List[Object]) -> str:
    """Generate the dataclasses that represent all OCPP 2.1 Calls."""
    return _generate_messages(calls)


def generate_call_results(call_results: List[Object]) -> str:
    """Generate the dataclasses that represent all OCPP 2.1 CallResults."""
    return _generate_messages(call_results)


def generate_enums(messages: List[Object]) -> str:
    """Generate all Enum that `messages` rely on directly or indirectly."""
    dependencies = _all_dependencies(messages)
    enums = []

    for dependency in dependencies:
        if not isinstance(dependency, Enum):
            continue

        if dependency in enums:
            continue

        enums.append(dependency)

    # Order enums alphabetically
    enums = sorted(enums, key=lambda x: x.name)

    code = """try:
    # breaking change introduced in python 3.11
    from enum import StrEnum
except ImportError:  # pragma: no cover
    from enum import Enum  # pragma: no cover

    class StrEnum(str, Enum):  # pragma: no cover
        pass  # pragma: no cover"""
    for enum in enums:
        lines = _generate_code_for_enum(enum)
        code += "\n\n\n" + lines
    code += "\n"

    return code


def generate_datatypes(messages: List[Object]) -> str:
    """Generate all custom types that OCPP 2.1 Calls and CallResults rely on."""
    objects = []
    dependencies = _all_dependencies(messages)

    for dependency in dependencies:
        if not isinstance(dependency, Object):
            continue

        if dependency in objects:
            continue

        objects.append(dependency)

    objects = sorted(objects, key=lambda x: x.name)

    code = ""
    code += "from __future__ import annotations\n"
    code += "from typing import List, Optional\n"
    code += "from dataclasses import dataclass\n"
    imports = _generate_import_statement_for_external_enums(objects)
    if imports != "":
        code += "\n"
        code += imports

    for object in objects:
        code += "\n\n" + _generate_code_for_object(object)

    return code


def _generate_messages(messages: List[Object]) -> str:
    objects = sorted(messages, key=lambda x: x.name)

    code = ""
    code += "from dataclasses import dataclass\n"
    code += "from typing import Any, List, Optional\n"
    imports = _generate_import_statement_for_external_datatypes(objects)
    if imports != "":
        code += "\n"
        code += imports

    imports = _generate_import_statement_for_external_enums(objects)
    if imports != "":
        code += "\n"
        code += imports

    for object in objects:
        code += "\n\n" + _generate_code_for_object(object)

    return code


def _all_dependencies(
    containers: List[Union[Object, Array]],
) -> List[Union[Object, Enum, Array]]:
    """Return a list of `Object`s`, `Enum`s and `Array`s `containers` rely on."""
    visited_dependencies = []
    while True:
        containers = _direct_dependencies(containers)
        visited_dependencies += containers

        if len(containers) == 0:
            break

    return visited_dependencies


def _direct_dependencies(
    containers: List[Union[Object, Array]],
) -> List[Union[Object, Enum, Array]]:
    """Return a list with all direct dependencies of `containers`.

    This function iterates over every `container`s properties. When a property is of type `Object` or `Enum`, these types
    are included in the return value. `Array`s holding `Object`s or `Enum`s are included too.

    Different `Object`s might rely on the same dependency. Any duplicate dependencies are removed.
    `Object`s relying on each other aren't in the return value either.

    """
    dependencies = []

    for container in containers:
        if isinstance(container, Array):
            if (
                isinstance(container.type, Object)
                or isinstance(container.type, Enum)
                or isinstance(container.type, Array)
            ):
                dependencies.append(container.type)
            continue

        if isinstance(container, Enum):
            continue

        for property in container.properties.values():
            if (
                isinstance(property.type, Object)
                or isinstance(property.type, Enum)
                or isinstance(property.type, Array)
            ):
                dependencies.append(property.type)
    return dependencies


def _generate_code_for_objects(objects: List[Object]) -> str:
    # Order enums alphabetically
    objects = sorted(objects, key=lambda x: x.name)

    code = ""
    for object in objects:
        code += "\n\n\n" + _generate_code_for_object(object)

    return code


def _generate_code_for_object(object: Object) -> str:
    lines = [
        "@dataclass",
        f"class {object.name}:",
    ]
    if len(object.properties) == 0:
        lines.append(f"{TAB}pass")

        return "\n".join(lines)

    property_names = sorted(
        object.properties.keys(), key=lambda x: _camel_to_snake_case(x)
    )
    skipped_properties = []

    for name in property_names:
        property = object.properties[name]
        if not property.required or property.has_default_value():
            skipped_properties.append(name)
            continue

        lines.append(
            f"{TAB}{_camel_to_snake_case(name)}: {_get_python_type(property.type)}"
        )

    for name in skipped_properties:
        property = object.properties[name]
        if isinstance(property.type, Any):
            lines.append(
                f"{TAB}{_camel_to_snake_case(name)}: {_get_python_type(property.type)} = None"
            )
            continue

        if not property.has_default_value():
            lines.append(
                f"{TAB}{_camel_to_snake_case(name)}: Optional[{_get_python_type(property.type)}] = None"
            )
            continue

        default = property.default
        if isinstance(property.type, Enum):
            default = f"{property.type.name}.{_camel_to_snake_case(property.default)}"
        if isinstance(property.type, String):
            default = f'"{property.default}"'

        lines.append(
            f"{TAB}{_camel_to_snake_case(name)}: {_get_python_type(property.type)} = {default}"
        )

    return "\n".join(lines) + "\n"


def _get_python_type(value) -> str:
    """Return a Python type hint as a `str` for given object."""
    if isinstance(value, Any):
        return "Any"

    if isinstance(value, String):
        return "str"

    if isinstance(value, Integer):
        return "int"

    if isinstance(value, Number):
        return "float"

    if isinstance(value, Array):
        value.type
        return f"List[{_get_python_type(value.type)}]"

    if isinstance(value, Object):
        return value.name

    if isinstance(value, Enum):
        if _has_potential_naming_collision_with_a_message(value.name):
            return f"enums.{value.name}"
        return value.name

    if isinstance(value, Boolean):
        return "bool"
    else:
        raise RuntimeError(value)


def _generate_code_for_enum(value: Enum) -> str:
    lines = [
        f"class {value.name}(StrEnum):",
    ]

    for variant in value.variants:
        lines.append(f'{TAB}{_camel_to_snake_case(variant)} = "{variant}"')

    return "\n".join(lines)


def _generate_import_statement_for_external_enums(objects: List[Object]) -> str:
    """Generate an import statement for all `Enum`s that the `objects` rely on."""
    enums = _external_enums_required(objects)
    enums = sorted(enums, key=lambda x: x.name)

    code = ""
    if len(enums) == 0:
        return code

    for enum in enums:
        if _has_potential_naming_collision_with_a_message(enum.name):
            code += "from ocpp.v21 import enums\n"
            break

    enums = [
        enum
        for enum in enums
        if not _has_potential_naming_collision_with_a_message(enum.name)
    ]

    if len(enums) == 0:
        return code

    code += "from ocpp.v21.enums import (\n"
    for enum in enums:
        code += f"{TAB}{enum.name},\n"
    code += ")\n"

    return code


def _generate_import_statement_for_external_datatypes(objects: List[Object]) -> str:
    """Generate an import statement for all datatypes that the `objects` rely on."""
    objects = _external_datatypes_required(objects)
    objects = sorted(objects, key=lambda x: x.name)

    if len(objects) == 0:
        return ""

    code = "from ocpp.v21.datatypes import (\n"
    for object in objects:
        if object.name == "data" and len(object.properties) == 0:
            continue

        code += f"{TAB}{object.name},\n"
    code += ")\n"

    return code


def _external_enums_required(objects: List[Object]) -> List[Enum]:
    """Return a list of all `Enum`s that `objects` depend on directly.
    The list is sorted alphabetically and without duplicates. These enums are
    not in scope of the `objects` and must be imported."""
    enums = []
    for dependency in _direct_dependencies(objects):
        if isinstance(dependency, Array):
            dependency = dependency.type

        if not isinstance(dependency, Enum):
            continue

        if dependency in enums:
            continue

        enums.append(dependency)

    return enums


def _external_datatypes_required(objects: List[Object]) -> List[Object]:
    """Return a list of all `Object`s that `objects` depend on directly."""
    filtered_objects = []
    for dependency in _direct_dependencies(objects):
        if isinstance(dependency, Array):
            dependency = dependency.type

        if not isinstance(dependency, Object):
            continue

        if dependency in objects:
            continue

        if dependency in filtered_objects:
            continue

        filtered_objects.append(dependency)

    return filtered_objects


def _has_potential_naming_collision_with_a_message(name: str) -> bool:
    """A few request and responses rely on enums that collide with message names.

    For example, the Reset request relies on the Reset enum. Without handling these naming collisions, the code for the Reset request looks like this:

        from ocpp.v21.enums import (
            Reset,
        )

        class Reset(StrEnum):
            type: Reset

    This is wrong. Instead, the code should look like this:

        from ocpp.v21 import enums

        class Reset(StrEnum):
            type: enums.Reset

    It's hard to find these exceptional cases dynamically. So I opted to hard code all
    enums that share a name with a call or call result.
    """
    return name in [
        "GetCertificateStatus",
        "IdToken",
        "Reset",
        "TransactionEvent",
        "VPN",
    ]


def _camel_to_snake_case(value: str) -> str:
    # Make sure "_" is inserted between "iso" and "15118".
    value = value.replace("iso15118", "iso_15118")

    # Prevent "V2X" from becoming "v2_x".
    value = value.replace("V2X", "V2x")

    # Prevent "V2G" from becoming "v2_g".
    value = value.replace("V2G", "V2g")

    # Prevent "prioritizedEMAIDs" from becoming "prioritized_emaid_s".
    value = value.replace("EMAID", "Emaid")

    # quick for measurands like "CUrrent.Import"
    value = value.replace(".", "")

    # This fix prevents "V2X" from becomming "v2_x".

    value = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", value)
    value = re.sub("([a-z0-9])([A-Z])(?=\\S)", r"\1_\2", value).lower()

    # fix  for	s309-1_p-16a = "s309-1P-16A"
    return value.replace("-", "_")
