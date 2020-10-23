# Source : https://www.hackerrank.com/challenges/friend-circle-queries/problem

def maxCircle(queries):
    links = {}
    lengths = {}
    maximum_friends = float('-inf')
    result = []

    def getRoot(ele):
        while ele != links[ele]:
            ele = links[ele]
        return ele


    def init(ele):
        if ele in links:
            return getRoot(ele)
        lengths[ele] = 1
        links[ele] = ele
        return ele


    for player1, player2 in queries:
        player1 = init(player1)
        player2 = init(player2)

        if player1 != player2:

            if lengths[player2] > lengths[player1]:
                player1, player2 = player2, player1

            links[player2] = player1
            lengths[player1] += lengths[player2]
            maximum_friends = max(maximum_friends, lengths[player1])
        result  += maximum_friends,
    return result

if __name__ == '__main__':
    print (maxCircle([[1, 2], [1, 3]]))
    print (maxCircle([[1, 2], [3, 4], [1, 3], [5, 7], [5, 6], [7, 4]]))
