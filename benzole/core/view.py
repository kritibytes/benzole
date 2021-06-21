from .response import Response


class DefaultView:
    def get(self):
        return Response(code=200)

    def post(self):
        return Response(code=200)

    def put(self):
        return Response(code=200)

    def patch(self):
        return Response(code=200)

    def delete(self):
        return Response(code=200)
