# Python program to suggest impute possible timestamps against single missing values
import unittest

def compute_seconds(inp_ts):
    hour, minute, seconds = inp_ts.split(':')
    return (hour*3600 + minute*60 + seconds)

def suggest_possible_timestamps(inp_ts):
    range_idx = {0:3, 1:4, 3:6, 4:10, 6:6, 7:10}
    max_seconds = compute_seconds('23:59:59')
    for ch in inp_ts:
        if ch != '?':
            continue
        else:
            missing_index = inp_ts.index('?')
            for i in range(range_idx.get(missing_index)):
                imputed_value = inp_ts.replace('?', str(i))
                if compute_seconds(imputed_value) < max_seconds:
                    print (imputed_value)
                else:
                    break

class Test(unittest.TestCase):
    def test_case1(self):
        pass

if __name__ == '__main__':
    #unittest.main()
    suggest_possible_timestamps('?1:12:59')
