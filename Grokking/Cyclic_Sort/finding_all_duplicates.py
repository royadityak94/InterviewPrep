# Python program to find the single duplicate in a fixed range of numbers: 1->n

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def finding_all_duplicates_1(arr):
    i = 0
    all_duplicates = []
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] == arr[j] and arr[i] not in all_duplicates and i!=j:
            all_duplicates.append(arr[i])
        elif arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    return sorted(all_duplicates)

def finding_all_duplicates_2(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j] and i!=j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    # Finding the requisite duplicates
    all_duplicates = []
    for i in range(len(arr)):
        if arr[i] != (i+1):
            all_duplicates.append(arr[i])

    return sorted(all_duplicates)

def main():
    test([4, 5], finding_all_duplicates_1([3, 4, 4, 5, 5]), "Test - 1")
    test([3, 5], finding_all_duplicates_1([5, 4, 7, 2, 3, 5, 3]), "Test - 2")

    test([4, 5], finding_all_duplicates_2([3, 4, 4, 5, 5]), "Test - 1 (Recommended)")
    test([3, 5], finding_all_duplicates_2([5, 4, 3, 7, 2, 3, 5]), "Test - 2 (Recommended)")

main()
