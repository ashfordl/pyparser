import unittest
import pyparser

class ParserTest(unittest.TestCase):

    def test_find_closing_bracket(self):
        self.assertEqual(pyparser.find_closing_bracket("(4-3)", 0), 4)
        self.assertEqual(pyparser.find_closing_bracket("(4-(4+4/5))", 0), 10)
        self.assertEqual(pyparser.find_closing_bracket("5-(4(-3))", 2), 8)
        self.assertEqual(pyparser.find_closing_bracket("5-(4(-3))*3", 2), 8)

    def test_convert_to_list(self):
        # Test basic expressions
        self.assertEqual(pyparser.convert_to_list("4.5*4.5"), ["4.5", "*", "4.5"])
        self.assertEqual(pyparser.convert_to_list("4.5*4.5+.4-3"), ["4.5", "*", "4.5", "+", "0.4", "-", "3"])

        # Test bracketed expressions
        self.assertEqual(pyparser.convert_to_list("4.5+(3.2*3.6)"), ['4.5', '+', ['3.2', '*', '3.6']])
        self.assertEqual(pyparser.convert_to_list("4.5(3.2*3.6)+2"), ['4.5', ['3.2', '*', '3.6'], '+', '2'])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
