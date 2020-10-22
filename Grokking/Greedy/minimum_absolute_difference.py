# Source: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

# I/p: [-2, 2, 4], O/p: 2
# I/p: [3, -7, 0], O/p: 3

def minimum_absolute_difference(arr):
    minimum_ = float('inf')
    arr.sort() # Converts N^2 to N order
    for i in range(len(arr)-1):
        diff = abs(arr[i+1]-arr[i])
        if diff < minimum_:
            minimum_ = diff
        if not minimum_:
            return 0
    return minimum_


if __name__ == '__main__':
    print (minimum_absolute_difference([-2, 2, 4]))
    print (minimum_absolute_difference([3, -7, 0]))
