'''
Rethinking FizzBuzz Implementation
'''

def get_naive_implementations(n: int):
    results: Union[int, str] = []
    for i in range(1, n+1):
        if not i % 15:
            results += 'FizzBuzz',
        elif not i % 5:
            results += 'Buzz',
        elif not i % 3:
            results += 'Fizz',
        else:
            results += i,
    return results


def get_optimized_implementations_1(n:int):
    results: Union[int, str] = []
    count3 = 3
    count5 = 5

    for i in range(1, n+1):
        count3 -= 1
        count5 -= 1

        if not (count3 or count5):
            results += 'FizzBuzz',
            count3, count5 = 3, 5
        elif not count5:
            results += 'Buzz',
            count5 = 5
        elif not count3:
            results += 'Fizz',
            count3 = 3
        else:
            results += i,
    return results

def get_optimized_implementations_2(n:int):
    results: Union[int, str] = []
    count3 = 0
    count5 = 0

    for i in range(1, n+1):
        count3 += 1
        count5 += 1
        holder = ''
        if count3 == 3:
            holder = 'Fizz'
            count3 = 0
        if count5 == 5:
            holder += 'Buzz'
            count5 = 0
        if holder:
            results += holder,
        else:
            results += i,
    return results

if __name__ == '__main__':
    naive_impl = get_naive_implementations(30)
    optimized_implementations1 = get_optimized_implementations_1(30)
    optimized_implementations2 = get_optimized_implementations_2(30)
    assert optimized_implementations1 == naive_impl, "The first implementation is incorrect!"
    assert optimized_implementations2 == naive_impl, "The second implementation is incorrect!"
