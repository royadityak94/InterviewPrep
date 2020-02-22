# Sub-routine to host the unbounded knapsack algorithm
# Importing the required packages
import unittest
import numpy as np

def unbounded_knapsack(w, v, W):
    ''' unbounded knapsack module '''
    dp = np.zeros(W+1)
    for i in range(min(w), W+1):
        dp[i] = dp[i-1]
        for k, Ck in enumerate(v):
            if w[k] <= i and dp[i] < (dp[i - w[k]] + Ck):
                dp[i] = dp[i - w[k]] + Ck
    return dp[W]

class Test(unittest.TestCase):
    def test_unbounded_knapsack(self):
        self.assertEqual(unbounded_knapsack([5, 10, 15], [10, 30, 20], 100), 300)
        #self.assertEqual(unbounded_knapsack2(100, [10, 30, 20], [5, 10, 15]), 300)

if __name__ == '__main__':
    unittest.main()
