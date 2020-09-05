# Python program to return the largest number in a list

def test(expected, output, msg=''):
    if expected == output:
        print ("Test Case successful: %s" % msg)
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ("Failed Test Case: %s" % msg)

def solution(numbers):
    if len(numbers) == 0:
        return 0
    max = numbers[0]
    start, end = 1, len(numbers)-1
    while start <= end and end > 0:
        if numbers[start] > max:
            max = numbers[start]

        if numbers[end] > max:
            max = numbers[end]

        start += 1
        end -= 1
    return max

def main():
    test(7, solution([7, 2, 6, 3]))
    test(7, solution([2, 4, 7, 6, 3]))
    test (10, solution([-2, 0, 10, 1]))

main()
