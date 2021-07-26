import unittest
from benzole.core.response import Response


class TestResponse(unittest.TestCase):

    def test_response_json(self):

        # Testing json response
        data = {"name": "John", "age": 26}
        response: Response = Response.json(data).status(201)
        self.assertEqual(response.body, '{"name": "John", "age": 26}')
        self.assertEqual(response.status_code, "201")
        self.assertEqual(response.headers, [('Content-Type', 'application/json')])

        response.set_headers({"AppName": "Benzole"})
        self.assertEqual(response.headers, [('AppName', 'Benzole')])

        response.add_header({"Company": "Kritibytes"})
        self.assertEqual(response.headers.sort(), [('AppName', 'Benzole'), ('Company', 'Kritibytes')].sort())
