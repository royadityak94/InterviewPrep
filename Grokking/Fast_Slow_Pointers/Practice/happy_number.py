
def sum_of_squares(num):
    resultant = 0
    while num:
        resultant += ((num % 10) ** 2)
        num //= 10
    return resultant

# O(log N) time | O(1) space
def find_happy_number(num):
    slow = num
    fast = num
    while True:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))
        if slow == fast:
            break
    return slow == 1

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
