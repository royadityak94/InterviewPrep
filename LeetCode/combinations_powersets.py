'''Combinations/Powersets
Ex: [1, 2, 3]
Powersets: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
Combinations: <same as powersets>
'''
import itertools

def getPowerSets(arr):
    _output = [[]]

    for ele in arr:
        for idx in range(len(_output)):
            subset = _output[idx] + [ele]
            _output += subset,
    return list(map(tuple, _output))


if __name__ == '__main__':
    arr = [1, 2, 3]
    op_combinations = []
    for _len in range(len(arr)+1):
        subsets = itertools.combinations(arr, _len)
        op_combinations.extend(subsets)
    print ("Ouput1: ", op_combinations)
    print ("Ouput2: ", getPowerSets(arr))
