import unittest

from intrep import Interpretator


class TestInterpretator(unittest.TestCase):
    def test_simple_operator1(self):
        """тeсты оператора >"""
        interpretator = Interpretator()
        token = ['>', '1', '2']
        result = interpretator.operation_simple(token)
        self.assertEqual(result, False)

    def test_simple_operator2(self):
        """тeсты оператора +"""
        interpretator = Interpretator()
        token = ['+', '1', '2']
        result = interpretator.operation_simple(token)
        self.assertEqual(result, 3)

    def test_test_simple_operator_Exception(self):
        """тeсты оператора на исключения"""
        interpretator = Interpretator()
        token = ['f', '1', '2']
        with self.assertRaises(Exception) as context:
            interpretator.operation_simple(token)

    def test_get_value_operator_Exception(self):
        """тeсты на исключения при взятие из словаря"""
        interpretator = Interpretator()
        with self.assertRaises(Exception) as context:
            interpretator.get_value('b')

    def test_get_value_and_assign(self):
        """тeсты на исключения при взятие из словаря"""
        interpretator = Interpretator()
        token = ['=', 'a', '2']
        interpretator.assign(token)
        result = interpretator.get_value('a')
        self.assertEqual(result, 2)

    def test_func_str(self):
        """тeсты на функцию работы со строками"""
        interpretator = Interpretator()
        token = ['=', 'a', 'Привет']
        interpretator.assign(token)
        token = ['.', 'a', 'Upper']
        interpretator.func_str(token)
        result = interpretator.get_value('a')
        self.assertEqual(result, 'ПРИВЕТ')



