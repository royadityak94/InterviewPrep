# Determine if a string is a permutation of the other

# Importing the required packages
import unittest
from collections import Counter

def  check_for_permutations(str1, str2, case_insensitive=True):
     ''' Check if two strings are permutations of one another : case insensitive '''
     if len(str1) != len(str2):
         return False
     if case_insensitive:
        str1, str2 = str1.lower(), str2.lower()
     counter = Counter([char for char in str1])
     for char in str2:
         if not counter[char]:
             return False
         counter[char] -= 1
     return True

class Test(unittest.TestCase):
    ''' Module to test for unit test cases '''
    def test_case_1(self):
        self.assertEqual(check_for_permutations('Alph', 'lAPh'), True)

if __name__ == '__main__':
    unittest.main()
