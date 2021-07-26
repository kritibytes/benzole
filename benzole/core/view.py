from typing import Any
from .response import Response


class DefaultView:
    def get(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"name":"Yunis"})

    def post(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"name":"Yunis"})

    def put(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"name":"Yunis"})

    def patch(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"name":"Yunis"})

    def delete(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"name":"Yunis"})
