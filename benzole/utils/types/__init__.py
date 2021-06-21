from typing import Any, TypedDict


class IRoute(TypedDict):
    url: str
    handler: Any
