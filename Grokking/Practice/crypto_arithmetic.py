def map_to_dict(solution):
    mapped = {}
    for item in solution:
        mapped[item[0]] = item[1]
    return mapped

def decode_vals(mapper, item):
    final_val = []
    for ch in item:
        got = mapper[ch]
        if not final_val and (len(item) > 1) and got == '0':
            print ("Returning false: ", final_val, item, got)
            return False, ''
        final_val += got,
    return True, ''.join(final_val)


def isCryptSolution(crypt, solution):
    solution = map_to_dict(solution)
    print ("Parsed: ", solution)

    flag, first = decode_vals(solution, crypt[0])
    if not flag:
        return False
    flag, second = decode_vals(solution, crypt[1])
    if not flag:
        return False
    flag, final = decode_vals(solution, crypt[2])
    if not flag:
        return False

    print ("Formed: ", first, second, final)

    if int(first) + int(second) != int(final):
        return False
    return True


if __name__ == '__main__':
    crypt = ["WASD", "IJKL", "AOPAS"]
    solution = [["W","2"],["A","0"],["S","4"],["D","1"],
                ["I","5"],["J","8"],["K","6"],["L","3"],
                ["O","7"],["P","9"]]
    # crypt =["A", "A", "A"]
    # solution = [["A", "0"]]

    print (isCryptSolution(crypt, solution))
