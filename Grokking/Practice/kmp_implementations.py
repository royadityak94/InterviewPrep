
def strStr_naive(haystack: str, needle: str) -> int:
        sub_len = len(needle)
        if not sub_len:
            return 0
        for idx in range(len(haystack)-sub_len+1):
            if haystack[idx:idx+sub_len] == needle:
                return idx
        return -1

def strStr_kmp(haystack: str, needle: str) -> int:
    # Using KMP Algorithm (Knuth Morris Pratt) - Suffix, Prefix information
    h, n = len(haystack), len(needle)

    # Create prefix table with i, j dancing pointer
    i, j, prefix_table = 1, 0, [-1]+[0]*n

    while i < n:
        if j==-1 or needle[i] == needle[j]:
            i += 1
            j += 1
            prefix_table[i] = j
        else:
            j = prefix_table[j]

    # Iterating over the main string
    i = j = 0
    while i < h and j < n:
        if j == -1 or haystack[i] == needle[j]:
            i, j = i+1, j+1
        else:
            j = prefix_table[j]

    return (i-j) if j==len(needle) else -1



def main() -> None:
    print (strStr_naive("abxabcabcaby", "abcaby"))
    # Using KMP Algorithm
    print (strStr_kmp("abxabcabcaby", "abcaby"))

main()
