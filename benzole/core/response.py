from typing import Any
from ..utils.types import IHeader, IHeaderList


class Response:
    status_code: str
    _headers: IHeader
    body: Any

    def __init__(self, status_code: str, type: str, additional_header: IHeader, body: Any) -> None:
        self.status_code = status_code
        self._headers = {
            "Content-Type": type,
            **additional_header
        }
        self.body = body

    def add_header(self, header: IHeader) -> None:
        self._headers = {
            **self._headers,
            **header
        }

    def get_headers(self) -> IHeaderList:
        return list(self._headers.items())

    headers = property(get_headers)
