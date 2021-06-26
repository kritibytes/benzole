import os
import unittest
from benzole.core.response import Response
import json


class TestResponse(unittest.TestCase):

    def test_response_object(self):
        data = {"name": "John", "age": 26}
        data_json = json.dumps(data)
        response = Response("200", "application/json", {"ApplicationName": "Benzole"}, data_json)
        print(response.headers)
        self.assertEqual(response.headers.sort(), [('Content-Type', 'application/json'), ('ApplicationName', 'Benzole')].sort())
        self.assertEqual(response.status_code, "200")
        self.assertEqual(response.body, data_json)
        response.add_header({"UserName": "yunisdev"})
        self.assertEqual(response.headers.sort(), [('Content-Type', 'application/json'), ('ApplicationName', 'Benzole'), ('UserName', 'yunisdev')].sort())
