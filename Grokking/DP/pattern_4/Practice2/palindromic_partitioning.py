'''
    Given a string, we want to cut it into pieces such that each piece is a palindrome.
    Write a function to return the minimum number of cuts needed.
    IP('abdbca') -> 3 ["a", "bdb", "c", "a"]
    IP('cddpd') -> 2 ["c", "d", "dpd"]
    IP('pqr') -> 2 ["p", "q", "r"]
    IP('pp') -> 0 [] (No need to cut 'pp' as it's already pallindrome)
'''

def isPallindrome(st, i, j):
    while (i < j):
        if st[i] != st[j]:
            return False
        i += 1
        j -= 1
    return True

def find_mpp_cuts(st):
    return find_mpp_cuts_recursive(st, 0, len(st)-1)

def find_mpp_cuts_recursive(st, startIdx, endIdx):
    if startIdx >= endIdx or isPallindrome(st, startIdx, endIdx):
        return 0

    minimum_cuts = endIdx - startIdx
    for i in range(startIdx, endIdx+1):
        if isPallindrome(st, startIdx, i):
            minimum_cuts = min(minimum_cuts,
            1 + find_mpp_cuts_recursive(st, i+1, endIdx))
    return minimum_cuts


def find_mpp_cuts_td(st):
    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_mpp_cuts_td_recursive(dp, st, 0, len(st)-1)

def find_mpp_cuts_td_recursive(dp, st, startIdx, endIdx):
    if startIdx >= endIdx or isPallindrome(st, startIdx, endIdx):
        return 0

    if dp[startIdx][endIdx] == -1:
        minimum_cuts = endIdx - startIdx
        for i in range(startIdx, endIdx+1):
            if isPallindrome(st, startIdx, i):
                minimum_cuts = min(minimum_cuts,
                1 + find_mpp_cuts_td_recursive(dp, st, i+1, endIdx))
        dp[startIdx][endIdx] = minimum_cuts
    return dp[startIdx][endIdx]



if __name__ == '__main__':
    #main()
    # Plain Recursion
    print (find_mpp_cuts("abdbca"))
    print (find_mpp_cuts("cdpdd"))
    print (find_mpp_cuts("pqr"))
    print (find_mpp_cuts("pp"))
    print (find_mpp_cuts("madam"))
    # TopDown DP
    print (find_mpp_cuts_td("abdbca"))
    print (find_mpp_cuts_td("cdpdd"))
    print (find_mpp_cuts_td("pqr"))
    print (find_mpp_cuts_td("pp"))
    print (find_mpp_cuts_td("madam"))
    # Bottomup DP
    # print (find_mpp_cuts_btmup("abdbca"))
    # print (find_mpp_cuts_btmup("cdpdd"))
    # print (find_mpp_cuts_btmup("pqr"))
    # print (find_mpp_cuts_btmup("pp"))
    # print (find_mpp_cuts_btmup("madam"))
