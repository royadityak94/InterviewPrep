'''
    Python program to implement 2 baselines -
    A) Count number of lines very fast
    B) Average Value of the tip_amount field.
'''
import time
import csv
from multiprocessing import Pool, cpu_count
import sys
import functools
import unittest
import pytest

def chunk(file, size=4096*1024):
    while True:
        b = file.read(size)
        if not b:
            break
        yield b

def naive_read(file_name):
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
        next(f)
        line_count = sum([b.count('\n') for b in chunk(f)])

    with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
        next(f)
        total_tip = sum([extract_sum_chunkwise(curr_chunk) for curr_chunk in chunk(f)])
    return line_count, total_tip

def extract_sum_chunkwise(curr_chunk):
    return sum([float(line.split(',')[-4])  for line in curr_chunk.split('\n') if len(line.split(',')) > 15])

def line_counter(curr_chunk):
    return curr_chunk.count('\n')

def naive_parallel(file_name):
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
        next(f)
        with Pool(processes=cpu_count()) as pool1:
            results_cnt = pool1.map(line_counter, [smaller_chunks for smaller_chunks in chunk(f)])
        pool1.close()
        line_count = functools.reduce(lambda x, y: x+y, results_cnt)

    with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
        next(f)
        with Pool(cpu_count()*2) as pool2:
            results_agg = pool2.map(extract_sum_chunkwise, [smaller_chunks for smaller_chunks in chunk(f)])
        pool2.close()
        total_tip = functools.reduce(lambda x, y: x+y, results_agg)
    return line_count, total_tip

class Test(unittest.TestCase):
    pytest.file_name = 'yellow_tripdata_2016-01.csv'#'sample_file.csv'
    pytest.iterations = 1
    def test_case1(self):
        # Optimized approach
        start_time = time.time()
        line_count, total_tip_amount = naive_parallel(pytest.file_name)
        end_time = time.time()
        print ("Optimized Approach: Line Count = %d, Avg.value of tip=%.4f, Avg. Time Taken = %.7f seconds." % (line_count, (total_tip_amount/line_count), ((end_time-start_time)/pytest.iterations)))

    def test_case2(self):
        # Naive approach
        start_time = time.time()
        line_count, total_tip_amount = naive_read(pytest.file_name)
        end_time = time.time()
        print ("\nNaive Approach: Line Count = %d, Avg.value of tip=%.4f, Avg. Time Taken = %.7f seconds." % (line_count, (total_tip_amount/line_count), ((end_time-start_time)/pytest.iterations)))

if __name__ == '__main__':
    unittest.main()
