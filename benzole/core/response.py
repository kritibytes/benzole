from typing import Any, Union, List
from ..utils.types import Header, HeaderList
import json


class Response:
    status_code: str = "200"
    _headers: Header
    body: Any

    def __init__(self, type: str, body: Any) -> None:
        self._headers = {
            "Content-Type": type,
        }
        self.body = body

    def add_header(self, header: Header) -> None:
        self._headers = {
            **self._headers,
            **header
        }

    def get_headers(self) -> HeaderList:
        return list(self._headers.items())

    def set_headers(self, header_obj: Header) -> None:
        self._headers = header_obj

    def status(self, status_code: Union[str, int]) -> 'Response':
        self.status_code = str(status_code)
        return self

    headers = property(get_headers, set_headers)

    # Response generator methods

    @classmethod
    def json(cls, data: Union[dict, list]) -> 'Response':
        rendered_data = json.dumps(data)
        return cls("application/json", rendered_data)

    @classmethod
    def render(cls, template_name: str, template_data: dict) -> 'Response':
        return cls('text/html', "")
