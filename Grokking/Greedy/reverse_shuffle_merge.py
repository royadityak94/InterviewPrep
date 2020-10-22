# Source: https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem
# a.  denotes the string obtained by reversing string . Example:
# b.  denotes any string that's a permutation of string . Example:
# c.  denotes any string that's obtained by interspersing the two strings  & , maintaining the order of characters in both. For example,  & , one possible result of  could be , another could be , another could be  and so on.
# Given a string, S s.t. s = merge(reverse(A), shuffle(A)) for some string A, find the "lexicographically smallest" A.

from collections import Counter, defaultdict

def reverseShuffleMerge(string):
    charAvailable = Counter(string)
    charUsed = defaultdict(int)
    charRemaining = Counter(string)
    resulting_str = []

    def can_use(ch):
        return charAvailable[ch] // 2 > charUsed[ch]

    def can_pop(ch):
        return (charUsed[ch] + charRemaining[ch]-1) >= charAvailable[ch] // 2


    for ch in reversed(string):
        if can_use(ch):
            while resulting_str and resulting_str[-1] > ch and can_pop(resulting_str[-1]):
                popped = resulting_str.pop()
                charUsed[popped] -= 1
            charUsed[ch] += 1
            resulting_str += ch,
        charRemaining[ch] -= 1

    return ''.join(resulting_str)

def frequency(s):
    res = defaultdict(int)
    for char in s:
        res[char] += 1
    return res

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge22(s):
    char_freq = Counter(s) #frequency(s)
    used_chars = defaultdict(int)
    remain_chars = Counter(s) #dict(char_freq)
    res = []

    def can_use(char):
        return (char_freq[char] // 2 ) > used_chars[char]

    def can_pop(char):
        needed_chars = char_freq[char] // 2
        return used_chars[char] + remain_chars[char] - 1 >= needed_chars

    for char in s[::-1]:
        if can_use(char):
            while res and res[-1] > char and can_pop(res[-1]):
                removed_char = res.pop()
                used_chars[removed_char] -= 1

            used_chars[char] += 1
            res.append(char)

        remain_chars[char] -= 1

    return "".join(res)

if __name__ == '__main__':
    print (reverseShuffleMerge("eggegg")) # egg
    print (reverseShuffleMerge("abcdefgabcdefg")) # agfedcb
    print (reverseShuffleMerge("aeiouuoiea")) #aeiou
