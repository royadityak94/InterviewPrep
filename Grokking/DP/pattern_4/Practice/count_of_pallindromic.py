'''
Given a string, find the total number of palindromic substrings in it. Please note we need to find the
total number of substrings and not subsequences.
Ip("abdbca") => 7, {"a", "b", "d", "b", "c", "a", "bdb"}
Ip("cddpd") => 7, {"c", "d", "d", "p", "d", "dd", "dpd"}
Ip("pqr") => 3, {"p", "q", "r"}

Similar Problems: Minimum String insertions to make it pallindromic, check if a string is K-Palindromic
'''

def count_pallindromes(s1):
    distinct_cnt = {}
    count_pallindromes_recursive(s1, 0, len(s1)-1, distinct_cnt)
    return len(s1) + len(distinct_cnt.keys())

def count_pallindromes_recursive(s1, startIdx, endIdx, distinct_cnt):
    #print ("Got Count: ", count)
    n = len(s1)
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if s1[startIdx] == s1[endIdx]:
        remaining = endIdx - startIdx - 1
        if remaining == count_pallindromes_recursive(s1, startIdx+1, endIdx-1, distinct_cnt):
            key = '%d%d'%(startIdx, endIdx)
            if key not in distinct_cnt:
                distinct_cnt[key] = 1
            return remaining+2
    withoutStart = count_pallindromes_recursive(s1, startIdx+1, endIdx, distinct_cnt)
    withoutEnd = count_pallindromes_recursive(s1, startIdx, endIdx-1, distinct_cnt)
    return withoutStart + withoutEnd


def count_pallindromes_td(s1):
    n = len(s1)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    distinct_cnt = {}
    count_pallindromes_td_recursive(dp, s1, 0, len(s1)-1, distinct_cnt)
    return len(s1) + len(distinct_cnt.keys())

def count_pallindromes_td_recursive(dp, s1, startIdx, endIdx, distinct_cnt):
    #print ("Got Count: ", count)
    n = len(s1)
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if dp[startIdx][endIdx] == -1:
        if s1[startIdx] == s1[endIdx]:
            remaining = endIdx - startIdx - 1
            if remaining == count_pallindromes_td_recursive(dp, s1, startIdx+1, endIdx-1, distinct_cnt):
                key = '%d%d'%(startIdx, endIdx)
                if key not in distinct_cnt:
                    distinct_cnt[key] = 1
                return remaining+2
        withoutStart = count_pallindromes_td_recursive(dp, s1, startIdx+1, endIdx, distinct_cnt)
        withoutEnd = count_pallindromes_td_recursive(dp, s1, startIdx, endIdx-1, distinct_cnt)
        dp[startIdx][endIdx] = withoutStart + withoutEnd
    return dp[startIdx][endIdx]

def count_pallindromes_btmup(s1):
    n = len(s1)
    dp = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        dp[i][i] = 1
        count += 1

    for i in range(n)[::-1]:
        for j in range(i+1, n):
            if s1[i] == s1[j]:
                if (j-i) == 1 or dp[i+1][j-1]:
                    count += 1
                    dp[i][j] = True
    return count


if __name__ == '__main__':
    #main()
    # Plain Recursion
    print (count_pallindromes('abdbca'))
    print (count_pallindromes('cddpd'))
    print (count_pallindromes('pqr'))
    # TopDown DP
    print (count_pallindromes_td('abdbca'))
    print (count_pallindromes_td('cddpd'))
    print (count_pallindromes_td('pqr'))
    # Bottomup DP
    print (count_pallindromes_btmup('abdbca'))
    print (count_pallindromes_btmup('cddpd'))
    print (count_pallindromes_btmup('pqr'))
