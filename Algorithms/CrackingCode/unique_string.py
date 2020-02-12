# To check if a string contains duplicate characters

#Importing the required packages
import unittest

def check_for_duplicates(text):
    ''' Module to check for duplicates
        Return Type: True/False '''

    seen = []
    for char in text:
        if char in seen:
            return True
        else:
            seen.append(char)
    return False

class Test(unittest.TestCase):
    def test_case_1(self):
        ''' Test case - 1 '''
        text_list = ['alpha', 'gonsq', 'rete', 'oxizas']
        outcomes = [True, False, True, False]

        for idx in range(len(text_list)):
            self.assertEqual(check_for_duplicates(text_list[idx]), outcomes[idx])

    def test_case_2(self):
        '''Module for case - 2'''
        text_list = ['/#a^', 's@!', '@@##', '!@']
        outcomes = [False, False, True, False]

        for idx in range(len(text_list)):
            self.assertEqual(check_for_duplicates(text_list[idx]), outcomes[idx])

if __name__ == '__main__':
    unittest.main()
