# Python program to check the validity of a given tic-toe configuration
import unittest
import itertools

def create_empty_map(board):
    size=len(board)
    configuration = {}
    for itr in range(size):
        configuration['r%d'%(itr+1)] = (0, 0)
        configuration['c%d'%(itr+1)] = (0, 0)
    # Populating for the diagonal entries
    configuration['d1'] = (0, 0)
    configuration['d2'] = (0, 0)
    return configuration

def update_tuple(inp_tuple, player):
    x, y = inp_tuple
    if player == 0:
        x += 1
    else:
        y += 1
    return (x, y)

def return_flattened_tuples_player_wise(configuration):
    flatten = itertools.chain.from_iterable
    player1, player2 = [], []
    for key in configuration.keys():
        val1, val2 = configuration.get(key)
        player1.append(val1)
        player2.append(val2)
    return player1, player2

def update_configuration(configuration, i, j, player):
    size = int((len(configuration.keys())-2)/2)
    # Update the rows and columns
    configuration['r%d'%(i+1)] = update_tuple(configuration.get('r%d'%(i+1)), player)
    configuration['c%d'%(j+1)] = update_tuple(configuration.get('c%d'%(j+1)), player)

    # Update for diagonal and anti-diagonals
    if i == j:
        configuration['d1'] = update_tuple(configuration.get('d1'), player)
    elif i==size-1-j:
        configuration['d2'] = update_tuple(configuration.get('d2'), player)
    return configuration

def extract_diagonals_playerwise(configuration):
    d1 = configuration.get('d1')
    d2 = configuration.get('d2')
    return ([d1[0], d2[0]], [d1[1], d2[1]])

def is_configuration_valid(board):
    size = len(board)
    configuration = create_empty_map(board)
    marked = (0, 0)
    for row in range(size):
        for col in range(size):
            if board[row][col] is None:
                continue
            configuration = update_configuration(configuration, row, col, board[row][col])
            marked = update_tuple(marked, board[row][col])

            # Anomaly statistics
            conf_play1, conf_play2 = return_flattened_tuples_player_wise(configuration)
            diag_play1, diag_play2 = extract_diagonals_playerwise(configuration)
            if (size in diag_play1 and size in diag_play2) or (diag_play1 == [size, size]) or (diag_play2 == [size, size]):
                return False
            elif size in diag_play1 or size in diag_play2:
                return True
            elif size in conf_play1 and size in conf_play2:
                return False
    if abs(marked[0] - marked[1]) > 1:
        return False
    return True

class Test(unittest.TestCase):
    def test_case1(self):
        ''' Base Case '''
        board1 = [[0, 1, 0], [1, 0, 1], [0, 1, None]]
        board2 = [[None, 1, None], [0, 1, None], [0, 1, 0]]
        board3 = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]

        self.assertEqual(is_configuration_valid(board1), True)
        self.assertEqual(is_configuration_valid(board2), True)
        self.assertEqual(is_configuration_valid(board3), True)

    def test_case2(self):
        board = [[0, 0, 1], [0, 1, 1], [0, 0, 1]]
        self.assertEqual(is_configuration_valid(board), False)
    def test_case3(self):
        board = [[0, None, 1], [0, None, 1], [0, None, 1]]
        self.assertEqual(is_configuration_valid(board), False)

    def test_case4(self):
        board=[[1, 0, 1], [1, 1, 0], [None, 1, 0]]
        self.assertEqual(is_configuration_valid(board), False)



if __name__ == '__main__':
    unittest.main()
