import unittest

def length_of_longest_substring(arr, k):
    # Time Complexity = O(N+N) ~ O(N)
    # Space Complexity: (1)
    ws_start = 0
    onesCount = 0
    longest_substring = float('-inf')

    for ws_end in range(len(arr)):
        elementRight = arr[ws_end]
        if elementRight == 1:
            onesCount += 1

        while (ws_end-ws_start+1-onesCount) > k:
            elementLeft = arr[ws_start]
            if elementLeft == 1:
                onesCount -= 1
            ws_start += 1
        longest_substring = max(longest_substring, ws_end-ws_start+1)
    return longest_substring

class Test(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        self.assertEqual(6, length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    def test_2(self):
        self.assertEqual(9, length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

if __name__ == '__main__':
    unittest.main()
    print (length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
