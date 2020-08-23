# Program to implement max same type of fruits which a basket can contain
# Input: Fruit=['A', 'B', 'C', 'A', 'C'], Output = 3, ['C', 'A', 'C']
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C'], Output = 5, ['B', 'C', 'B', 'B', 'C']

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def max_same_fruits_in_basket(fruits, K=2):
    # Runtime Complexity: O(N+N) ~ O(N)
    max_fruit_length = 0
    fruits_frequency = {}
    window_start = 0

    for window_end in range(len(fruits)):
        fruit_right = fruits[window_end]
        if fruit_right not in fruits_frequency:
            fruits_frequency[fruit_right] = 0
        fruits_frequency[fruit_right] += 1

        while len(fruits_frequency) > K:
            fruit_left = fruits[window_start]
            fruits_frequency[fruit_left] -= 1
            if fruits_frequency[fruit_left] == 0:
                del fruits_frequency[fruit_left]
            window_start += 1

        max_fruit_length = max(max_fruit_length, window_end-window_start+1)

    return max_fruit_length

def main():
    test(3, max_same_fruits_in_basket(['A', 'B', 'C', 'A', 'C']), "Test - 1")
    test(5, max_same_fruits_in_basket(['A', 'B', 'C', 'B', 'B', 'C']), "Test - 2")

main()
