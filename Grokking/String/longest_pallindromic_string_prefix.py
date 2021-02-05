# Finding longest pallindromic prefix of a given string (using KMP algorithm)
# O(N) time gaurantee (Naive: O(n^2) time)
# Source : https://www.geeksforgeeks.org/print-the-longest-palindromic-prefix-of-a-given-string/

# O(n) time, O(n) space
def longest_palindromic_prefix(string):
    temp = string + '?' + string[::-1]
    prefix = [0] * len(temp)

    for i in range(1, len(temp)):
        curr_len = prefix[i - 1]

        while curr_len > 0 and temp[curr_len] != temp[i]:
            curr_len = prefix[curr_len-1]
        if temp[i] == temp[curr_len]:
            curr_len += 1
        prefix[i] = curr_len
    return string[:prefix[len(temp)-1]]

def main():
    print (longest_palindromic_prefix('abaac')) # 'aba'
    print (longest_palindromic_prefix('abacabaxyz')) # 'abacaba'

main()
