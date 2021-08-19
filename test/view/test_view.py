import os
import unittest
from benzole import BenzoleView
from benzole.core.response import Response


class TestView(unittest.TestCase):

    def test_default_view(self):
        class ExampleView(BenzoleView):
            pass

        obj = ExampleView()

        self.assertIsInstance(obj.get(), Response)
        self.assertIsInstance(obj.post(), Response)
        self.assertIsInstance(obj.patch(), Response)
        self.assertIsInstance(obj.put(), Response)
        self.assertIsInstance(obj.delete(), Response)
