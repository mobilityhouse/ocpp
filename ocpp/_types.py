from typing import Any, Callable, Literal, TypedDict

OCPPVersion = Literal["1.6", "2.0", "2.0.1", "2.1"]


Handler = Callable[..., Any]


class Route(TypedDict, total=False):
    _on_action: Handler
    _after_action: Handler
    _skip_schema_validation: bool
