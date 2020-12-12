'''
Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.
'''
from unittest import main, TestCase

def count_ways(n):
    # Time: O(3^N), Space: O(N)
    if n in range(3):
        return 1
    elif n == 3:
        return 2

    diff1repr = count_ways(n-1)
    diff3repr = count_ways(n-3)
    diff4repr = count_ways(n-4)
    return diff1repr + diff3repr + diff4repr

def count_ways_td(n):
    dp = [0 for _ in range(n+1)]
    return count_ways_td_recursive(dp, n)

def count_ways_td_recursive(dp, n):
    # Time: O(N), Space: O(N)
    if n in range(3):
        return 1
    elif n == 3:
        return 2

    if not dp[n]:
        diff1repr = count_ways(n-1)
        diff3repr = count_ways(n-3)
        diff4repr = count_ways(n-4)
        dp[n] = diff1repr + diff3repr + diff4repr
    return dp[n]

def count_ways_btmup(n):
    # Time: O(N), Space: O(N)
    dp = [0 for _ in range(n+1)]
    dp[:4] = [1, 1, 1, 2]

    for idx in range(4, n+1):
        dp[idx] = dp[idx-1] + dp[idx-3] + dp[idx-4]
    return dp[-1]

class Test(TestCase):
    def test_1(self):
        self.assertEqual(count_ways(4), 4)
        self.assertEqual(count_ways_td(4), 4)
        self.assertEqual(count_ways_btmup(4), 4)
    def test_2(self):
        self.assertEqual(count_ways(5), 6)
        self.assertEqual(count_ways_td(5), 6)
        self.assertEqual(count_ways_btmup(5), 6)
    def test_3(self):
        self.assertEqual(count_ways(6), 9)
        self.assertEqual(count_ways_td(6), 9)
        self.assertEqual(count_ways_btmup(6), 9)

if __name__ == '__main__':
    main()
