from typing import (
    Any, 
    TypedDict, 
    Dict, 
    Union,
    Tuple,
    List
)


class IRoute(TypedDict):
    url: str
    handler: Any


IHeader = Dict[str, Union[str]]
IHeaderList = List[Tuple[str, str]]