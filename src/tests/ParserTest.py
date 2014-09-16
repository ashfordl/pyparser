import unittest
import pyparser

class ParserTest(unittest.TestCase):

    def testFindClosingBracket(self):
        self.assertEqual(pyparser.findClosingBracket("(4-3)", 0), 4)
        
        self.assertEqual(pyparser.findClosingBracket("(4-(4+4/5))", 0), 10)
        
        self.assertEqual(pyparser.findClosingBracket("5-(4(-3))", 2), 8)
        
        self.assertEqual(pyparser.findClosingBracket("5-(4(-3))*3", 2), 8)

    def testListConvert(self):
        self.assertEqual(pyparser.convertToList("4.5*4.5"), ["4.5", "*", "4.5"])
        
        self.assertEqual(pyparser.convertToList("4.5*4.5+.4-3"), ["4.5", "*", "4.5", "+", "0.4", "-", "3"])
        
        self.assertEqual(pyparser.convertToList("4.5*4.5"), ["4.5", "*", "4.5"])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()