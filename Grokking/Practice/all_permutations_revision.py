from itertools import permutations, chain

def generate_power_set(arr):
    if len(arr) == 0:
        yield []
    elif len(arr) == 1:
        yield []
        yield arr

    else:
        for item in generate_power_set(arr[1:]):
            yield item
            yield [arr[0]] + item

def generate_permutations(list):
    if len(list) == 2:
        return [list, list[::-1]]

    result = []
    for idx in range(len(list)):
        others = generate_permutations(list[:idx]+list[idx+1:])
        for permute in others:
            result += [list[idx]] + permute,
    return result

def enumerate_possible_permutations(arr):
    powersets = generate_power_set(arr)
    final_result = []
    for set in powersets:
        if len(set) == 1:
            final_result += set[0],
        elif len(set) > 1:
            final_result.extend(generate_permutations(set))

    final_result = (map(lambda x: ''.join(x), final_result))
    final_result = sorted(final_result, key=lambda x: (len(x), x))
    return final_result

def enumerate_possible_permutations2(arr):
    result = []
    for r in range(1, len(arr)+1):
        for set in permutations(arr, r):
            result += ''.join(set),
    return result

# a,b,c,ab,bc,ac,ba,cb,ab,abc,bca,cab,acb,bac,CBA,

def main():
    print (enumerate_possible_permutations(list("abc")))
    print (enumerate_possible_permutations2(list("abc")))

main()
