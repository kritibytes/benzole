from typing import Any
from .response import Response


class BenzoleView:
    def get(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"data":"data"})

    def post(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"data":"data"})

    def put(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"data":"data"})

    def patch(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"data":"data"})

    def delete(
        self,
        req: Any = "",  # Request object
    ) -> Response:
        return Response.json({"data":"data"})
