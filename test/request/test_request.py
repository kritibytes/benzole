from benzole.utils.types import HTTP_Method
import unittest
from benzole.core.request import Request
from benzole.utils.types import HTTP_Method

class TestResponse(unittest.TestCase):

    def test_response_json(self):
        req: Request = Request()
        req.method = HTTP_Method.POST
        req.body = "Hello World!!!"
        
        self.assertIsInstance(req.method,HTTP_Method)
        self.assertEqual(req.body,"Hello World!!!")