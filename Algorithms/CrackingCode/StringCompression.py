# Module to implement string compression
import unittest

def compress_string(string):
    compressed = []
    counter = 0
    for idx in range(len(string)):
        if idx != 0 and string[idx] != string[idx-1]:
            compressed.append(string[idx-1] + str(counter))
            counter = 0
        counter += 1

    compressed.append(string[-1] + str(counter))
    return min(string, ''.join(compressed), key=len)

class Test(unittest.TestCase):
    def test_case1(self):
        data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
        ]
        for item in data:
            self.assertEqual(compress_string(item[0]), item[1])

if __name__ == '__main__':
    unittest.main()
