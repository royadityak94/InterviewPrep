
def kadanesAlgorithm(array):
    # Write your code here.
    maximum_sum = 0
    global_best = float('-inf')
    for ele in array:
        if ele > maximum_sum + ele:
            maximum_sum = ele
        else:
            maximum_sum += ele
        print (ele, maximum_sum)
        global_best = max(global_best, maximum_sum)
    return global_best


if __name__ == '__main__':
    print (kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
