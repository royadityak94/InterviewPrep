# Python program to implement the longest substring with atmost k distinct characters
import unittest

def find_max_substring_k_distinct(inp_str, max_distinct):
    start = 0
    longest = 0
    curr_window = ''
    for end in range(len(inp_str)):
        curr_window += inp_str[end]
        if len(set(curr_window)) > max_distinct:
            longest = max(longest, len(curr_window))
            start += 1
            curr_window = inp_str[start:end]
    return longest

class Test(unittest.TestCase):
    def test_case1(self):
        print (find_max_substring_k_distinct('araaaaaaci', 3)) #abbbcb
    def test_case2(self):
        print (find_max_substring_k_distinct('alllbpppaaja', 3)) #abbbcb

if __name__ == '__main__':
    unittest.main()
