from itertools import chain, combinations, takewhile
from functools import reduce

def generate_power_set_redun(arr):
    if len(arr) == 0:
        yield []
    elif len(arr) == 1:
        yield arr
        yield []
    else:
        for item in generate_power_set(arr[1:]):
            yield item + [arr[0]]
            yield item

def return_power_set(input):
    arr = list(set(input))
    final_set = []
    for item in generate_power_set(arr):
        final_set += ''.join(item),
    return final_set, len(final_set)

def alternate_powerset(input):
    iterable = list(input)
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    final = list(filter(lambda x: len(x), (map(lambda set: ''.join(set),
        (chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))))
        ))
    return final, len(final)

def generate_power_set(input):
    arr = list(input)
    subsets = list(reduce(lambda result, item: result + [subset + [item] for subset in result]
        , arr, [[]]))

    final_set = []
    for set in subsets:
        if len(set) > 0:
            final_set += ''.join(set),

    return final_set, len(final_set)


def main():
    print (generate_power_set('abcde'))
    print ('----------------')
    print (alternate_powerset('abcde'))
    # print (return_power_set('abcde'))
    # print (alternate_powerset('abc'))
    #print (list(generate_power_set(list("abcde"))))

main()
