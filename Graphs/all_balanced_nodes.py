# Ref: https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/
# Finding if all the nodes are balanced (i.e. no of incoming and outgoing edges are equal)
import unittest
import operator

def newRoadSystem(roadRegister):
    for x, y in zip(zip(map(sum, roadRegister)), zip(map(sum, zip(*roadRegister)))):
        if x != y:
            return False
    return True

class Test(unittest.TestCase):
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_1(self):
        roadRegister = [[False, True,  False, False], [False, False, True,  False], [True,  False, False, True ], [False, False, True,  False]]
        self.assertTrue(newRoadSystem(roadRegister))
    def test_2(self):
        roadRegister = [[False, True,  False, False, False, False, False],
                [True,  False, False, False, False, False, False],
                [False, False, False, True,  False, False, False],
                [False, False, True,  False, False, False, False],
                [False, False, False, False, False, False, True ],
                [False, False, False, False, True,  False, False],
                [False, False, False, False, False, True,  False]]
        self.assertTrue(newRoadSystem(roadRegister))
    def test_3(self):
        roadRegister = [[False, True,  False],
                [False, False, False],
                [True,  False, False]]
        self.assertFalse(newRoadSystem(roadRegister))

def main():
    unittest.main()

main()
