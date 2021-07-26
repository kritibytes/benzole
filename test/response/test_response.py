import os
import unittest
from benzole.core.response import Response
import json


class TestResponse(unittest.TestCase):

    def test_response_json(self):

        # Testing json response
        data = {"name": "John", "age": 26}
        response: Response = Response.json(data).status(201)
        self.assertEqual(response.body, '{"name": "John", "age": 26}')
        self.assertEqual(response.headers, [('Content-Type', 'application/json')])
        self.assertEqual(response.status_code, "201")
        
