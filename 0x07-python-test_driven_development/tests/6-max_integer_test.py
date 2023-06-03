#!/usr/bin/python3
""" Unittest for max_integer([..]) """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaster(unittest.TestCase):
    """ TestMaster is a class with function used to test code """
    def test_normal_input(self):
        """ method used to test simple input """
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 1, 1, 1, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, 0, -5]), 0)

    def test_advanced_input(self):
        """ method used to test complex input """
        self.assertEqual(max_integer([-0, 0, -0, 0, -0]), 0)
        self.assertEqual(max_integer((1, -2, 2, -3, 99, 0)), 99)
        self.assertEqual(max_integer([0.1, 0.2, -0.1, -0.2, 0.3]), 0.3)
        self.assertEqual(max_integer([9.997, 9.998, 9.992, 9.999]), 9.999)
        self.assertEqual(max_integer([(5/2.5), (-10/3), (3/3), (3/1)]), 3.0)


    def test_special_input(self):
        """ method used to test input that did not come in a list """
        self.assertEqual(max_integer([[1, 2 + 100], [4, -30], [4, 5], [4, 5.1]]), [4, 5.1])
        self.assertEqual(max_integer([(1, 2), (0, 20), (1, 2, 3)]), (1, 2, 3))
        self.assertEqual(max_integer([[-100], [-2]]), [-2])
        self.assertEqual(max_integer(["1", "2", '-3']), '2')
        self.assertEqual(max_integer("(10), (20), (7)"), '7')


    
    def test_no_input(self):
        """ method used to test Null list input """
        self.assertEqual(max_integer([]), None)


    def test_error_input(self):
        """ method used to test wrong input """

        with self.assertRaises(TypeError):
            max_integer([0, 1, 2, '3'])

        with self.assertRaises(TypeError):
            max_integer(10, 20 , 30)
        
        with self.assertRaises(TypeError):
            max_integer(1.99)

        with self.assertRaises(TypeError):
            max_integer([1, 2, 3], [3, 2, 1])


    def test_type_error_input(self):
        """ now we try anything other than lists """

        with self.assertRaises(TypeError):
            max_integer('', '')
        
        with self.assertRaises(TypeError):
            max_integer(False)

        with self.assertRaises(TypeError):
            max_integer({1:100}, {1:200})


