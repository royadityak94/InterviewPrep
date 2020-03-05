# This program aims to find a tic-tac-toe winner given a board configuration,
# in constant time, O(1) but in linear space complexity
import unittest
import itertools

def create_empty_map(size):
    game_status = {}
    for itr in range(size):
        game_status['r%d'%(itr+1)] = (0, 0)
        game_status['c%d'%(itr+1)] = (0, 0)

    #diagonal (d1) and anti-diagonal (d2)
    game_status['d1'] = (0, 0)
    game_status['d2'] = (0, 0)
    return game_status

def update_appropriate_player(curr_tuple, player):
    x, y = curr_tuple
    if player == 0:
        x += 1
    else:
        y += 1
    return (x, y)

def is_winning_configuration(game_status):
    size = int((len(game_status)-2)/2)
    extract_conf = [game_status.get(key) for key in game_status.keys()]
    flatten = itertools.chain.from_iterable

    if size in list(flatten(extract_conf)):
        return True
    else:
        return False

def update_game_status(game_status, i, j, player):
    size = int((len(game_status.keys()) - 2)/2)
    # Update it for appropriate row and column
    game_status['r%d' % (i+1)] = update_appropriate_player(game_status.get('r%d'%(i+1)), player)
    game_status['c%d' % (j+1)] = update_appropriate_player(game_status.get('c%d'%(j+1)), player)

    if i==j:
        game_status['d1'] = update_appropriate_player(game_status.get('d1'), player)
    if i==(size-1-j):
        game_status['d2'] = update_appropriate_player(game_status.get('d2'), player)

    return game_status

def game_decision(board_conf):
    ''' Return_types:
        0/1 : Winner with id of player
        2 : Draw
    '''
    size = len(board_conf)
    game_status = create_empty_map(size)

    for i in range(size):
        for j in range(size):
            if board_conf[i][j] is None:
                continue
            else:
                game_status = update_game_status(game_status, i, j, board_conf[i][j])

            if is_winning_configuration(game_status):
                return board_conf[i][j]
    return 2


class Test(unittest.TestCase):
    def test_case1(self):
        board_conf = [[0, 1, 0], [1, 0, 1], [0, 1, None]]
        self.assertEqual(game_decision(board_conf), 0)

    def test_case2(self):
        board_conf = [[None, 1, None], [0, 1, None], [0, 1, 0]]
        self.assertEqual(game_decision(board_conf), 1)

    def test_case3(self):
        board_conf = [[1, 0, 0], [0, 1, 1], [0, 1, 0]]
        self.assertEqual(game_decision(board_conf), 2)

    def test_case4(self):
        board_conf = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
        self.assertEqual(game_decision(board_conf), 0)

if __name__ == '__main__':
    unittest.main()
