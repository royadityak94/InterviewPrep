'''
Given a string, find the total number of palindromic substrings in it. Please note we need to find the
total number of substrings and not subsequences.
Ip("abdbca") => 7, {"a", "b", "d", "b", "c", "a", "bdb"}
Ip("cddpd") => 7, {"c", "d", "d", "p", "d", "dd", "dpd"}
Ip("pqr") => 3, {"p", "q", "r"}

Similar Problems: Minimum String insertions to make it pallindromic, check if a string is K-Palindromic
'''

def count_pallindromes(st):
    n = len(st)
    count = {}
    count_pallindromes_recursive(st, 0, len(st)-1, count)
    return len(st) + len(count)

def count_pallindromes_recursive(st, startIdx, endIdx, count):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if st[startIdx] == st[endIdx]:
        remaining = endIdx - startIdx - 1
        if remaining == count_pallindromes_recursive(st, startIdx+1, endIdx-1, count):
            key = '%d%d' % (startIdx, endIdx)
            if key not in count:
                count[key] = 1
            return remaining+2
    withoutStart = count_pallindromes_recursive(st, startIdx+1, endIdx, count)
    withoutEnd = count_pallindromes_recursive(st, startIdx, endIdx-1, count)
    return max(withoutStart, withoutEnd)

def count_pallindromes_td(st):
    n = len(st)
    count = {}
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    count_pallindromes_td_recursive(dp, st, 0, len(st)-1, count)
    return len(st) + len(count)

def count_pallindromes_td_recursive(dp, st, startIdx, endIdx, count):
    if startIdx > endIdx:
        return 0
    elif startIdx == endIdx:
        return 1

    if dp[startIdx][endIdx] == -1:
        if st[startIdx] == st[endIdx]:
            remaining = endIdx - startIdx - 1
            if remaining == count_pallindromes_td_recursive(dp, st, startIdx+1, endIdx-1, count):
                key = '%d%d' % (startIdx, endIdx)
                if key not in count:
                    count[key] = 1
                return remaining+2
        withoutStart = count_pallindromes_td_recursive(dp, st, startIdx+1, endIdx, count)
        withoutEnd = count_pallindromes_td_recursive(dp, st, startIdx, endIdx-1, count)
        dp[startIdx][endIdx] = max(withoutStart, withoutEnd)
    return dp[startIdx][endIdx]

def count_pallindromes_btmup(st):
    n = len(st)
    dp = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        count += 1
        dp[i][i] = True

    for i in range(n)[::-1]:
        for j in range(i+1, n):
            if st[i] == st[j]:
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
