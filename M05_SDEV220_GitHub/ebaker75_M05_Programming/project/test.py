<<<<<<< Updated upstream
from fractions import Fraction
import unittest

from my_sum import sum #import the sum function from the __init__ file


class TestSum(unittest.TestCase): #inherit unittest.TestCase, as it should for unittest
    def test_list_int(self): #title describes what is being tested
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3] #the list
        result = sum(data) #imported sum function acting on the list
        self.assertEqual(result, 6) #a different way of writing the assert function

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)] #use fractions instead of integers
        result = sum(data)
        self.assertEqual(result, 1) #this test is a negative control; it should fail

if __name__ == '__main__':
    unittest.main() #command-line entry point; this is the unittest test runner

    # test passed as expected
    # had some issues: incorrect file structure
    # my_sum, with the __init__ file in it, belongs in project folder
    # test.py belongs in project folder, not the my_sum folder; it couldn't find the module because it didn't "look" in that direction with the commands used here
    # tried python -m unittest -v test and got OK
    # ran python -m unittest discover and it ran one file; didn't tell which file it ran, so special attention should be paid to which folder I'm in before running this command
    # when navigating up a folder, discover only printed the location of the test that failed
    # discover -s test tested a sqlite3 folder even though I was not in a directory that used this program; I don't think I need -s test for my projects
        # it's been about 5 minutes and I think it's searching my entire machine.
        # too long -- keyboard interrupted
=======
from fractions import Fraction
import unittest

from my_sum import sum #import the sum function from the __init__ file


class TestSum(unittest.TestCase): #inherit unittest.TestCase, as it should for unittest
    def test_list_int(self): #title describes what is being tested
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3] #the list
        result = sum(data) #imported sum function acting on the list
        self.assertEqual(result, 6) #a different way of writing the assert function

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)] #use fractions instead of integers
        result = sum(data)
        self.assertEqual(result, 1) #this test is a negative control; it should fail

if __name__ == '__main__':
    unittest.main() #command-line entry point; this is the unittest test runner

    # test passed as expected
    # had some issues: incorrect file structure
    # my_sum, with the __init__ file in it, belongs in project folder
    # test.py belongs in project folder, not the my_sum folder; it couldn't find the module because it didn't "look" in that direction with the commands used here
    # tried python -m unittest -v test and got OK
    # ran python -m unittest discover and it ran one file; didn't tell which file it ran, so special attention should be paid to which folder I'm in before running this command
    # when navigating up a folder, discover only printed the location of the test that failed
    # discover -s test tested a sqlite3 folder even though I was not in a directory that used this program; I don't think I need -s test for my projects
        # it's been about 5 minutes and I think it's searching my entire machine.
        # too long -- keyboard interrupted
>>>>>>> Stashed changes
