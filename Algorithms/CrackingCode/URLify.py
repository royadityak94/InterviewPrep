# Module to implement the URLify
# Importing the required packages
import unittest


# def urlify(url):
#     ''' Module to perform string URLify'''
#     return url.strip().replace(' ', '%20')

urlify = lambda url: url.strip().replace(' ', '%20')

class Test(unittest.TestCase):
    ''' Class to perform testing '''
    def test_case1(self):
        url_dict = {
        'much ado about nothing      ': 'much%20ado%20about%20nothing',
        'Mr John Smith    ': 'Mr%20John%20Smith'
        }
        for url in url_dict.keys():
            self.assertEqual(urlify(url), url_dict.get(url))


if __name__ == '__main__':
    unittest.main()
