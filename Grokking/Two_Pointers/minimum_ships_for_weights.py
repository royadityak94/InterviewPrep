# Giving weights of passengers and limit of each ship, compute minimum ships needed
# Input: [3, 2, 1, 2, 3, 5], Wt = 5. Output: 4
# Input: [1, 3, 5, 2], Wt = 5, O/p : 3
# Input : [1, 2], Wt = 3, O/p: 1
# Input: [4, 2, 3, 3], Wt = 5, O/p:3

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def return_min_boats(weights, limit):
    weights = sorted(weights) # Sorting the weights array
    front, back = 0, len(weights) - 1
    boat_count = 0
    while front <= back:
        if  weights[front] + weights[back] <= limit:
            front += 1
            back -= 1
        else:
            back -= 1
            current_sum = 0
        boat_count += 1
    return boat_count

def main():
    test(4, return_min_boats([3, 2, 1, 2, 3, 5], 5), "Test - 1")
    test(2, return_min_boats([1, 3, 4, 2], 5), "Test - 2")
    test(1, return_min_boats([1, 2], 3), "Test - 3")
    test(3, return_min_boats([4, 2, 3, 3], 5), "Test - 4")

main()
