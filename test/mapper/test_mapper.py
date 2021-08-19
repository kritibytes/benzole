import os
import unittest
from benzole.utils.mapper import (
    files_mapper,
    routes_mapper
)


class TestMapper(unittest.TestCase):

    def setUp(self) -> None:
        os.chdir(os.path.abspath(os.path.join(__file__, '..')))
        self.files_map = files_mapper()

    def test_files_mapper(self):
        """Testing files_mapper"""
        self.assertEqual(self.files_map.sort(), ['src/index.py', 'src/api/users.py'].sort())

    def test_routes_mapper(self):
        """Testing routes_mapper"""
        routes_map = routes_mapper(self.files_map)
        print(routes_map)
        self.assertEqual(len(routes_map), 2)
