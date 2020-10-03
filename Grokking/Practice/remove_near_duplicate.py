# Python program to remove the near duplicates
import unittest
import inspect

def remove_adjacent_duplicate_2(input: str) -> str:
    if len(input) < 2:
        return input
    input = list(input+'')
    i = 1
    while i > 0 and i < len(input):
        if input[i-1] == input[i]:
            del input[i-1]
            del input[i-1]
            i -= 1
        else:
            i += 1
    return ''.join(input)

def remove_adjacent_duplicate(input:str) -> str:
    if len(input) < 2:
        return input
    input += ' '
    stack = [input[0]]
    last_seen = input[0]
    i = 1
    while i in range(len(input)):
        ch = input[i]
        if ch == last_seen:
            if stack and ch == stack[-1]:
                stack.pop()
            i += 1
            continue

        j = 1
        while j > 0 and j < len(stack):
            if stack[j-1] == stack[j]:
                del stack[j-1]
                del stack[j-1]
                j -= 1
            else:
                j += 1

        stack += ch,
        last_seen = ch
        i +=1

    return ''.join(stack[:-1])

class Test(unittest.TestCase):
    def test_1(self):
        try:
            self.assertEqual(remove_adjacent_duplicate('abccba'), '')
        except AssertionError:
            print ('Failed Test Case: ', inspect.currentframe().f_code.co_name)
    def test_2(self):
        try:
            self.assertEqual(remove_adjacent_duplicate('foobar'), 'fbar')
        except AssertionError:
            print ('Failed Test Case: ', inspect.currentframe().f_code.co_name)
    def test_3(self):
        try:
            self.assertEqual(remove_adjacent_duplicate('abccbefggfe'), 'a')
        except AssertionError:
            print ('Failed Test Case: ', inspect.currentframe().f_code.co_name)
    def test_4(self):
        try:
            self.assertEqual(remove_adjacent_duplicate('aaaaacaaabbbacdc'), 'cacdc')
        except AssertionError:
            print ('Failed Test Case: ', inspect.currentframe().f_code.co_name)

if __name__ == '__main__':
    unittest.main()
