# Module to check if the edit distance between two strings in less than two

# Importing the required packages
import unittest

def is_one_edit_away(s1, s2):
    ''' Module to check for edit distance conformability to one edit '''
    if len(s1) == len(s2):
        return is_one_replace_away(s1, s2)
    elif abs(len(s1) - len(s2)) == 1:
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        return is_one_insert_away(s1, s2)
    else:
        return False

def is_one_replace_away(s1, s2):
    ''' Module for implementing replacement check '''
    edited = False
    for i, j in zip(s1, s2):
        if i != j:
            if edited:
                return False
            edited = True
    return True

def is_one_insert_away(s1, s2):
    ''' Module for implementing insertion check '''
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            i += 1
        else:
            i, j = i+1, j+1
    return True

class Test(unittest.TestCase):
    ''' Test cases '''
    def test_case1(self):
        data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

        for _data in data:
            self.assertEqual(is_one_edit_away(_data[0], _data[1]), _data[2])

if __name__ == '__main__':
    unittest.main()
