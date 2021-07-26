from typing import Any
from ..utils.types import HTTP_Method, IHeader


class Request:
    headers: IHeader
    body: Any
    method: HTTP_Method
