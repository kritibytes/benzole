from typing import (
    Any,
    TypedDict,
    Dict,
    Union,
    Tuple,
    List
)
from enum import Enum


class Route(TypedDict):
    url: str
    handler: Any


Header = Dict[str, str]
HeaderList = List[Tuple[str, str]]


class HTTP_Method(Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
