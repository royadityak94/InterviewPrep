def firstDuplicateValue(array):
    # Write your code here.
    # Changing to seen within the element position

    for ele in array:
        idx = abs(ele)
        print (ele, array)
        if array[idx-1] < 0:
        	return idx
        else:
        	array[idx-1] *= -1
    return -1

if __name__ == '__main__':
    print (firstDuplicateValue([2, 1, 1]))
