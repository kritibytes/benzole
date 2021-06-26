from .response import Response


class DefaultView:
    def get(self):
        return Response("200","text/html",{},"Hello World!!!")

    def post(self):
        return Response("200","text/html",{},"Hello World!!!")

    def put(self):
        return Response("200","text/html",{},"Hello World!!!")

    def patch(self):
        return Response("200","text/html",{},"Hello World!!!")

    def delete(self):
        return Response("200","text/html",{},"Hello World!!!")
