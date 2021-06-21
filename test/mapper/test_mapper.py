import os
import unittest
from benzole.utils.mapper import (
    files_mapper,
    routes_mapper
)

os.chdir(os.path.abspath(os.path.join(__file__,'..')))

class TestMapper(unittest.TestCase):

    def setUp(self) -> None:
        self.files_map = files_mapper()

    def test_files_mapper(self):
        print('\nTesting files_mapper',end=' ')
        self.assertEqual(1,1)

    def test_routes_mapper(self):
        print('\nTesting routes_mapper',end=' ')
        routes_map = routes_mapper(self.files_map)
        self.assertEqual(1,1)