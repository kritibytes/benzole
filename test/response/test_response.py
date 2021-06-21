import os
import unittest
from benzole.core.response import Response


class TestResponse(unittest.TestCase):

    def test_response_object(self):
        response = Response(code=404)
        self.assertEqual(response.code, 404)
        response = Response()
        self.assertEqual(response.code, 200)
