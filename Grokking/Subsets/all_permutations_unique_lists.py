# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

def find_subsets(nums):
    subsets = []
    # Sorting the input list to place the number alongside each other
    list.sort(nums)
    subsets.append([])
    last_set = []
    for idx in range(len(nums)):
        new_set = []
        if nums[idx] != nums[idx-1]:
            for i in range(len(subsets)):
                set = subsets[i] + [nums[idx]]
                new_set.append(set)
            last_set = new_set
        else:
            for i in range(len(last_set)):
                set = last_set[i] + [nums[idx]]
                new_set.append(set)
        subsets.extend(new_set)
    return subsets

def find_subsets_alternate(nums):
    # Time Complexity: O(N*(2^N)), Space Complexity: O(2^N)
    subsets = []
    subsets.append([])

    for ele in nums:
        for i in range(len(subsets)):
            set = subsets[i] + [ele]
            if set not in subsets:
                subsets.append(set)
    return subsets

def list_of_list_equality(list1, list2):
    if len(list1) != len(list2):
        return False

    for sub_list in list2:
        if sub_list not in list1:
            print ("Not matching .... ", sub_list)
            return False
    return True

def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets_alternate([1, 5, 3, 3])))

main()
