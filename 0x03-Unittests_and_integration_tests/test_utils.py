#!/usr/bin/env python3
""" Parameterize a unit test """
import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ inherits from unittest.TestCase """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ method to test that the access_nested_map method returns
        what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ method to test that a KeyError is raised """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ method to test that utils.get_json returns the expected result """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, payload, mocked):
        """ method to test that the method returns what it is supposed to """
        class MyMock(Mock):
            """
            class that inherits from Mock
            """
            def json(self):
                """ json method returning a payload
                """
                return payload

        mocked.return_value = MyMock()
        self.assertEqual(get_json(test_url), payload)


class TestMemoize(unittest.TestCase):
    """ class with a test_memoize method """

    def test_memoize(self):
        """" a method that test memoize"""
        class TestClass:
            """ A test class """
            def a_method(self):
                """ returns 42 """
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            test_obj = TestClass()
            test_obj.a_property
            test_obj.a_property
            mocked.assert_called_once()

