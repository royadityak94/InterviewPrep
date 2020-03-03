# Python program to implement sorted array based on count of occurrences
from collections import Counter
from itertools import permutations

def compare_list(list1, list2):
    keys1 = dict(Counter(list1).most_common())
    keys2 = dict(Counter(list2).most_common())

    for key in keys1:
        if keys1.get(key) != keys2.get(key):
            return False
    return True

if __name__ == '__main__':
    items = ['adi', 'minu', 'zeta', 'keta']
    items_distinct = list(set(items))
    for i in range(175):
        items.append(items[-1])
    for i in range(99):
        items.append(items[1])
    for i in range(100):
        items.append(items[0])
    for i in range(50):
        items.append(items[2])

    # Most Common
    print (Counter(items).most_common())

    # Create another resultant_mat list
    resultant_mat = [i for item, count in Counter(items).most_common()
            for i in [item] * count]
    print ("Is resultant_mat same as original matrix? %r " % compare_list(resultant_mat, items) )

    distinct_elements = set()
    cnt = 0
    for ele in permutations('Aditya', 5):
        formed = "".join(ele)
        distinct_elements.add(formed)
        cnt += 1
    print ("Total Count = %d" % cnt)
    print ("Size of set = %d" % len(distinct_elements))
