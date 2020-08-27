# Python program to compare 2 strings containing backspaces
# Inp: str1="xy#z", str2="xzz#"; Op: True
# str1="xp#", str2="xyz##"; Op: True
# str1="xywrrmp", str2="xywrrmu#p"; Op: True

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def compare_string_containing_backspaces_simple(str1, str2):
    ptr_1, ptr_2 = len(str1)-1, len(str2)-1

    while (ptr_1 > -1 or ptr_2 > -1):
        while ptr_1 > -1 and str1[ptr_1] == '#':
            ptr_1 -= 2
        while ptr_2 > -1 and str2[ptr_2] == '#' and str2[ptr_2-1] != '#':
            ptr_2 -= 2

        if ptr_1 > -1 and ptr_2 > -1 and str1[ptr_1] != str2[ptr_2]:
            return False
        else:
            ptr_1, ptr_2 = ptr_1 - 1, ptr_2 - 1

    if ptr_1 == ptr_2 == -1:
        return True
    else:
        return False

def count_backspaces(str, curr_idx):
    ptr = curr_idx
    backspaces = 0
    while ptr > -1 and str[ptr] == '#':
        backspaces += 1
        ptr -= 1
    return backspaces

def compare_string_containing_backspaces_recursive(str1, str2):
    # Time Complexity : O(M+N), Space Complexity: O(1); M - len(str1), N - len(str2)
    ptr_1, ptr_2 = len(str1)-1, len(str2)-1

    while (ptr_1 > -1 or ptr_2 > -1):
        while ptr_1 > -1 and str1[ptr_1] == '#':
            ptr_1 -= (count_backspaces(str1, ptr_1) * 2)

        while ptr_2 > -1 and str2[ptr_2] == '#':
            ptr_2 -= (count_backspaces(str2, ptr_2) * 2)

        if ptr_1 > -1 and ptr_2 > -1 and str1[ptr_1] != str2[ptr_2]:
            return False
        ptr_1, ptr_2 = ptr_1 - 1, ptr_2 - 1

    if ptr_1 == ptr_2 < 0:
        return True
    else:
        return False

def main():
    test(True, compare_string_containing_backspaces_simple("xyp#z", "xyy#zz#"), "Test - 1 (Simple)")
    test(True, compare_string_containing_backspaces_simple("xy#z", "xzz#"), "Test - 2  (Simple)")
    test(False, compare_string_containing_backspaces_simple("xy#z", "xyz#"), "Test - 3  (Simple)")
    test(True, compare_string_containing_backspaces_simple("xywrrmp", "xywrrmu#p"), "Test - 4  (Simple)")
    test(True, compare_string_containing_backspaces_recursive("xyp#z", "xyy#zz#"), "Test - 1 (Advanced)")
    test(True, compare_string_containing_backspaces_recursive("xy#z", "xzz#"), "Test - 2 (Advanced)")
    test(False, compare_string_containing_backspaces_recursive("xy#z", "xyz#"), "Test - 3 (Advanced)")
    test(True, compare_string_containing_backspaces_recursive("xywrrmp", "xywrrmu#p"), "Test - 4 (Advanced)")
    test(True, compare_string_containing_backspaces_recursive("xp#", "xyz##"), "Test - 5 (Advanced)")
    test(True, compare_string_containing_backspaces_recursive("xyupx###p#zxwr#", "xyzxw"), "Test - 6 (Advanced)")
    test(True, compare_string_containing_backspaces_recursive("xyu###px", "px"), "Test - 7 (Advanced)")
    test(True, compare_string_containing_backspaces_recursive("bdsz#bds###bds###xyu###px", "bdsxwe###px"), "Test - 8 (Advanced)")

main()
