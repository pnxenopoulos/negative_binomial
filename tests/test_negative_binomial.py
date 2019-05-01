''' Unit tests for negative binomial fitting
'''
import unittest
from context import *

class BadInputTest(unittest.TestCase):
    ''' Class to test bad inputs
    '''
    def test_r_param_neg(self):
        ''' r_derv should fail with negative values
        '''
        with self.assertRaises(ValueError):
            r_derv(-1, [0, 1])

    def test_r_param_zero(self):
        ''' r_derv should fail with a value of 0
        '''
        with self.assertRaises(ValueError):
            r_derv(0, [0, 1])

    def test_p_param_neg(self):
        ''' p_equa should fail with a value of 0
        '''
        with self.assertRaises(ValueError):
            p_equa(-1, [0,1])

    def test_p_param_zero(self):
        ''' r_derv should fail with a value of 0
        '''
        with self.assertRaises(ValueError):
            p_equa(0, [0, 1])

class FunctionValueTests(unittest.TestCase):
    ''' Class to tests return values of functions
    '''
    def test_r_derv(self):
        ''' r_derv should return -1.9593823933705767 given the input
        '''
        self.assertEqual(r_derv(1,[0,47]),-1.9593823933705767)

    def test_p_equa(self):
        ''' p_equa should return 0.04081632653061229 given the input
        '''
        self.assertEqual(p_equa(1,[0,47]),0.04081632653061229)

if __name__ == '__main__':
    unittest.main()
