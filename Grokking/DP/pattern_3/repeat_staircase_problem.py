'''
Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the
top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.
'''
from unittest import main, TestCase

def count_ways_recursion(n):
    # Time: O(3^N), Space: O(N)
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    take1step = count_ways_recursion(n-1)
    take2step = count_ways_recursion(n-2)
    take3step = count_ways_recursion(n-3)
    return take1step + take2step + take3step

def count_ways_td(n):
    # Time: O(N), Space: O(N)
    dp = [0 for _ in range(n+1)]
    return count_ways_td_recursive(dp, n)

def count_ways_td_recursive(dp, n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2

    if not dp[n]:
        take1step = count_ways_recursion(n-1)
        take2step = count_ways_recursion(n-2)
        take3step = count_ways_recursion(n-3)
        dp[n] = take1step + take2step + take3step
    return dp[n]

def count_ways_btmup(n):
    # Time: O(N), Space: O(N)
    dp = [0 for _ in range(n+1)]
    dp[:3] = [1, 1, 2]

    for idx in range(3, n+1):
        dp[idx] = dp[idx-1] + dp[idx-2] + dp[idx-3]
    return dp[-1]

class Test(TestCase):
    def test_1(self):
        self.assertEqual(count_ways_recursion(3), 4)
        self.assertEqual(count_ways_td(3), 4)
        self.assertEqual(count_ways_btmup(3), 4)
    def test_2(self):
        self.assertEqual(count_ways_recursion(4), 7)
        self.assertEqual(count_ways_td(4), 7)
        self.assertEqual(count_ways_btmup(4), 7)
    def test_3(self):
        self.assertEqual(count_ways_recursion(5), 13)
        self.assertEqual(count_ways_td(5), 13)
        self.assertEqual(count_ways_btmup(5), 13)

if __name__ == '__main__':
    main()
