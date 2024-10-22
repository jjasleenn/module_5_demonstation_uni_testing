"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: jasleen kaur 
Date: 22 october 2024
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

import unittest
from unittest.mock import patch
import unittest.mock
from src.functions import greet_name_age, grade_outcome, prompt_name_greeting, math_operation
class testfunctions(unittest.TestCase):
    def test_greet_name_with_all_parameters(self):
        # Arrange
        name = "joe"
        age = "25"
        expected = "Hello joe, you are 25 years old!"

        # Act 
        actual = greet_name_age(name,age)

        # Assert 
        self.assertEqual (expected, actual)

    def test_grade_outcome_a_plus(self):
      # Arrange
      grade = 91
      expected = "A+"
      # Act
      actual = grade_outcome(grade)
      # Assert
      self.assertEqual(expected,actual)


     #Example Test 2:
    def test_grade_outcome_pass(self):
     # Arrange
     # Edge cases ensure that our function handles values at the boundaries of conditions correctly
     grade = 76
     low_edge = 50
     high_edge = 90
     expected = "Pass"

     # Act
     # Has been COMMENT OUT, since this time we are replacing the single test for multiple tests at once.

     # Act and Assert including edge cases
     # Our multiple test ensures that both all normal values and boundary values for grades are handled
     # correctly.
     self.assertEqual(expected, grade_outcome(grade))
     self. assertEqual(expected, grade_outcome(low_edge))
     self. assertEqual(expected, grade_outcome (high_edge))

     #Example Test 2:

     # Testing middle case (76 or middle value)
     # Testing lower boundary (50 or lowest grade)
     # Testing upper boundary (90 or highest grade