import unittest
import inspect

def is_paranthesis_balanced(input):
    bracket_map = {')': '(', '}': '{', ']': '['}
    bracket_lists = bracket_map.keys()
    stack = []
    for ch in input:
        if ch in bracket_lists:
            last_opened = bracket_map.get(ch)
            if stack.pop() != last_opened:
                return False
        else:
            stack += ch,

    if len(stack):
        return False
    return True


class Test(unittest.TestCase):
    def test_1(self):
        input = '{[()]}'
        try:
            self.assertTrue(is_paranthesis_balanced(input))
        except AssertionError:
            print ("Failed Test Case: ", inspect.currentframe().f_code.co_name)

    def test_2(self):
        input = '({)'
        try:
            self.assertFalse(is_paranthesis_balanced(input))
        except AssertionError:
            print ("Failed Test Case: ", inspect.currentframe().f_code.co_name)

    def test_3(self):
        input = '({)()[]'
        try:
            self.assertEqual(is_paranthesis_balanced(input), False)
        except AssertionError:
            print ("Failed Test Case: ", inspect.currentframe().f_code.co_name)

    def test_4(self):
        input = '({})()[]{'
        try:
            self.assertEqual(is_paranthesis_balanced(input), False)
        except AssertionError:
            print ("Failed Test Case: ", inspect.currentframe().f_code.co_name)

if __name__ == '__main__':
    unittest.main()
