# Python file for hosting multiple fibonacci implementations
#Importing the required packages
import unittest
import numpy as np

def fibonacci_recurssion(n):
    ''' Fibonacci by naive recursion'''
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recurssion(n-1) + fibonacci_recurssion(n-2)

def fibonacci_recurssion_mem(n):
    ''' Naive fibonacci recursion using memoization '''
    if fibonacci_memory[n] == -1 and n > 1:
        fibonacci_memory[n] = fibonacci_recurssion_mem(n-1) + fibonacci_recurssion_mem(n-2)
    return fibonacci_memory[n]

def fibonacci_recurssion_mem_main(n):
    global fibonacci_memory
    fibonacci_memory = (np.ones(n+1))*-1
    fibonacci_memory[0:2] = [0, 1]
    return fibonacci_recurssion_mem(n)

def fibonacci_recurssion_td(n):
    fib_arr = np.zeros(n+1)
    fib_arr[0:2] = [0, 1]
    for i in range(2, n+1):
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]
    return fib_arr[n]

class Test(unittest.TestCase):
    def test_fibonacci_recurssion(self):
        self.assertEqual(fibonacci_recurssion(25), 75025)
    def test_fibonacci_recurssion_mem(self):
        self.assertEqual(fibonacci_recurssion_mem_main(25), 75025)
    def test_fibonacci_recurssion_td(self):
        self.assertEqual(fibonacci_recurssion_td(25), 75025)

if __name__ == '__main__':
    unittest.main()
