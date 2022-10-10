from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                lst = [2,3,5,2,0]
                self.assertTrue(puzzle(lst))


        def testCounterClockwise(self):
                 """Tests a board solveable using only CCW moves"""
                 lst = [1,100,0,2,0]
                 self.assertTrue(puzzle(lst))
        
        def testMixed(self):
                  """Tests a board solveable using only a combination of CW and CCW moves"""
                  lst = [1,2,3,4,0]
                  self.assertTrue(puzzle(lst))
        

        def testUnsolveable(self):
                '''tests an unsolveable board'''
                lst = [4,0,4,0]
                self.assertFalse(puzzle(lst))

                lst = [3,4,1,2,0]
                self.assertFalse(puzzle(lst))
unittest.main()

