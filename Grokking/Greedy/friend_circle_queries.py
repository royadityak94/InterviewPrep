# Source : https://www.hackerrank.com/challenges/friend-circle-queries/problem

# Complete the maxCircle function below: Inefficient, fails all test cases in the Run test except the first 3 !!
def maxCircle_baseline(queries):
    max_friends = float('-inf')
    unison = []
    result = []

    for player1, player2 in queries:
        def check_if_in_list(ele):
            for idx, team in enumerate(unison):
                if ele in team:
                    return True, idx
            return False, -1

        status_pl1, index_pl1 = check_if_in_list(player1)
        status_pl2, index_pl2 = check_if_in_list(player2)

        if (not status_pl1) and (not status_pl2):
            unison += [player1, player2],
            max_friends = max(max_friends, 2)
        elif status_pl1:
            if (index_pl2+1):
                unison[index_pl1].extend(unison[index_pl2])
                del unison[index_pl2]
            else:
                unison[index_pl1] += player2,
            #print (">> INdex = ", index_pl1, unison)
            if index_pl1 < index_pl2:
                max_friends = max(max_friends, len(unison[index_pl1]))
            else:
                max_friends = max(max_friends, len(unison[index_pl2]))
        else:
            if (index_pl1+1):
                unison[index_pl2].extend(unison[index_pl1])
                del unison[index_pl1]
            else:
                unison[index_pl2] += player1,
            if index_pl1 < index_pl2:
                max_friends = max(max_friends, len(unison[index_pl1]))
            else:
                max_friends = max(max_friends, len(unison[index_pl2]))
        result += max_friends,
        #print (player1, player2, unison, max_friends)
    return result


def maxCircle(queries):
    links = {} # to keep track of associations
    length = {} # to keep track of community length
    result = []
    max_friends = float('-inf')

    def getRoot(ele):
        while ele != links[ele]:
            ele = links[ele]
        return ele

    def init(ele):
        if ele in links:
            return getRoot(ele)
        length[ele] = 1
        links[ele] = ele
        return ele

    for player1, player2 in queries:
        player1 = init(player1)
        player2 = init(player2)

        if player1 != player2:
            if length[player2] > length[player1]:
                player1, player2 = player2, player1
            links[player2] = player1
            length[player1] += length[player2]
            max_friends = max(max_friends, length[player1])
        result += max_friends,
    return result

if __name__ == '__main__':
    print (maxCircle([[1, 2], [1, 3]]))
    print (maxCircle([[1, 2], [3, 4], [1, 3], [5, 7], [5, 6], [7, 4]]))
