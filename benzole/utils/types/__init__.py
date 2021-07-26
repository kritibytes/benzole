from typing import (
    Any,
    TypedDict,
    Dict,
    Union,
    Tuple,
    List
)
from enum import Enum


class IRoute(TypedDict):
    url: str
    handler: Any


IHeader = Dict[str, str]
IHeaderList = List[Tuple[str, str]]


class HTTP_Method(Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
