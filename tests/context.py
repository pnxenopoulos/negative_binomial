''' Used to provide easy access to package for unit tests
'''
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from negative_binomial.core import r_derv, p_equa, neg_bin_fit
