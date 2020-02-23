# Python fnc to count all char occurrences in string
# Importing the required packages
from collections import Counter
import unittest

def count_occurrences(list_str):
    counts = Counter()
    list_str = map(lambda x:x.lower(), list_str)
    for str in list_str:
        counts.update(str)
    return counts

class Test(unittest.TestCase):
    def test_case1(self):
        list_str = ['alPHA', 'GAAmma', 'zeta', 'gANroo']
        print (count_occurrences(list_str))

if __name__ == '__main__':
    unittest.main()
