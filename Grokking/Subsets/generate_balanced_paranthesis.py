# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
# Input: N=2, O/p: (()), ()()
# Input: N=3, O/p: ((())), (()()), (())(), ()(()), ()()()
from collections import deque, Counter

def check_unbalanced(str):
    if len(str) < 2:
        return False
    state = Counter(str)
    print (">> ", state)
    try:
        if state.get('(') > state.get(')'):
            return True
        else:
            return False
    except:
        return True

def generate_valid_parentheses(num):
    result = deque()
    result.append(['('])
    flag = True

    while flag:
        print ("------------------------------------")
        queue = deque()

        for set in result:
            print ("Adding %s to queue" % str(set))
            queue.append(set)

        #result = []
        while queue:
            combination = queue.popleft()
            print ("Combination = ", combination)
            if check_unbalanced(''.join(combination)):
                result.append(combination + [')'])
            else:
                stringed = ''.join(combination)
                if not Counter(stringed).get('(') >= num:
                    result.append(combination + ['('])
                else:
                    flag = False
    result = list(map(lambda x: ''.join(x), result))                
    print (result)
    return result

def main():
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
    # print("All combinations of balanced parentheses are: " +
    #     str(generate_valid_parentheses(3)))

    check_unbalanced("(())()(")

main()
