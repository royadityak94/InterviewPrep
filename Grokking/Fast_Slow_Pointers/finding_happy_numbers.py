def find_happy_number(num):
    slow = fast = num
    while True:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))
        if slow == fast:
            break
    return slow == 1

def sum_of_squares(num):
    sum = 0
    while num > 0:
        sum += pow(num % 10, 2)
        num //= 10
    return sum

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))

main()
