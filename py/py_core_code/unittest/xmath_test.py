# ==========================================================
#  alltest.py
# ========================================================== 

import unittest 
from xmath import *
 
class Xmath_Ave_TestCase(unittest.TestCase):
    def test_avesequence(self):
        """ave: return the known average for a known numerical sequence"""
        sequences = ( ([1,1,1,1,1,1,1], 1),
                      ([1,2,3,4,5], 3),
                      ([-1,-2], -1.5),
                      ([7], 7),
                      ([0,33.5,66.245,100], 49.93625),
                      ([2e101,5e100], 1.25e101),
                      ([2e-101,5e-100], 2.6e-100),
                      ([2e20,2e-20], 1e20),
                      ([1.453e22,1.453e22], 1.453e22),
                      ((1,2,3,4,5), 3),
                      ((((1,2,3,4,5))), 3) )
        for x, average in sequences:
            self.assertEqual(ave(x), average)
        return
 
    def test_avenumber(self):
        """ave: return the given value for a given single number"""
        for x in range(1,545,34):
            self.assertEqual(ave(x), x)
        for x in (0.345,1.1,3214.887,12.099621235,-23.32):
            self.assertEqual(ave(x), x)
        self.assertEqual(ave(1e100), 1e100)
        self.assertEqual(ave(1e-100), 1e-100)
        return
 
    def test_nonnumerical(self):
        """ave: fail when given non-numerical input"""
        for x in ['a', 'hello', bool(True), None, {1:1,2:2}]:
            self.assertRaises(XmathError, ave, x)
        return
 
    def test_nonsinglevaluedsequence(self):
        """ave: fail if given sequence contains a non-single-valued item"""
        for x in ( [1,2,3,'abcd',5], ([1,2],3,4), ((1,2),(3,4)) ):
            self.assertRaises(XmathError, ave, x)
        return
 
    def test_emptysequence(self):
        """ave: fail when given an empty sequence"""
        for x in ((),[]):
            self.assertRaises(XmathError, ave, x)
        return
 
class Xmath_Fact_TestCase(unittest.TestCase):
    def test_factinteger(self):
        """fact: return the known factorial for a known integer"""
        exact_values = ( (0,1),
                          (1,1),
                          (5,120),
                          (10,3628800),
                          (13,6227020800) )
        for x, factorial in exact_values:
            self.assertEqual(fact(x), factorial)
        return
 
    def test_noninteger(self):
        """fact: fail when given a non-integer"""
        for x in (0.345,1.1,3214.887,12.099621235,-23.32):
            self.assertRaises(XmathError, fact, x)
        for x in ['a', bool(True), None]:
            self.assertRaises(XmathError, fact, x)
        return
 
    def test_negative(self):
        """fact: fail when given a negative integer"""
        for x in (-1,-5,-13,-263):
            self.assertRaises(XmathError, fact, x)
        return
 
    def test_nonsinglevalueditem(self):
        """fact: fail when given a non-single-valued item"""
        for x in ['hello',[1,2,3,4,5],(6,7,8,9),{1:1,2:2}]:
            self.assertRaises(XmathError, fact, x)
        return
 
if __name__ == "__main__":
    suite1 = unittest.makeSuite(Xmath_Ave_TestCase)
    suite2 = unittest.makeSuite(Xmath_Fact_TestCase)
    alltests = unittest.TestSuite((suite1,suite2))
    unittest.TextTestRunner(verbosity=2).run(alltests)
 
# End of file
