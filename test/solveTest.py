from unittest import TestCase
import sudoku.solve as sudoku 
from sudoku.solve import _solve as solvee

class SolveTest(TestCase):
    TestCase.maxDiff = None
    def setUp(self):
        self.inputDicthionary = {}

        
    def setGrid(self, grd):
        self.inputDicthionary['grid'] = grd
        
    def setIntegrity(self, intgty):
        self.inputDicthionary['integrity'] = intgty
        
    def testInsert100_010(self):
        self.setGrid('[0,-5,-8,-9,0,-1,-6,0,0,-2,0,0,-5,-8,0,0,-4,-1,-9,0,0,0,0,0,0,-5,0,-3,0,-6,-1,-5,0,0,-2,0,-1,-4,0,0,-2,0,-7,0,-9,0,0,0,0,-6,0,-5,0,0,0,-1,-3,-2,0,0,-4,-8,-7,0,0,-4,0,0,-3,0,0,0,-5,0,0,-8,-1,0,-2,0,0]')
        self.setIntegrity('6594d6506dc349fdbd9e5dda58acfa8d563657b0ef8bfc3a24ea53df9c988f9b')
        testDictionary = {'grid': [4, -5, -8, -9, 3, -1, -6, 7, 2, -2, 3, 7, -5, -8, 6, 9, -4, -1, 
                                   -9, 6, 1, 7, 4, 2, 3, -5, 8, -3, 9, -6, -1, -5, 7, 8, -2, 4, -1, -4, 5, 
                                   3, -2, 8, -7, 6, -9, 7, 8, 2, 4, -6, 9, -5, 1, 3, 6, -1, -3, -2, 9, 5, -4, 
                                   -8, -7, 8, 2, -4, 6, 7, -3, 1, 9, 5, -5, 7, 9, -8, -1, 4, -2, 
                                   3, 6],'integrity': 'e33e2de2fdbb25aacf25b299e101cccfdd2e1be4284acc257bcdc76737272af6', 'status':'ok'}
        result = solvee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
        
    
    def testInsert100_020(self):
        self.setGrid('[4,-5,-8,-9,3,-1,-6,7,2,-2,3,7,-5,-8,6,9,-4,-1,-9,6,1,7,4,2,3,-5,8,-3,9,-6,-1,-5,7,8,-2,4,-1,-4,5,3,-2,8,-7,6,-9,7,8,2,4,-6,9,-5,1,3,6,-1,-3,-2,9,5,-4,-8,-7,8,2,-4,6,7,-3,1,9,5,-5,7,9,-8,-1,4,-2,3,6]')
        self.setIntegrity('e33e2de2fdbb25aacf25b299e101cccfdd2e1be4284acc257bcdc76737272af6')
        testDictionary = {'grid': [4, -5, -8, -9, 3, -1, -6, 7, 2, -2, 3, 7, -5, -8, 6, 9, -4, -1, 
                                   -9, 6, 1, 7, 4, 2, 3, -5, 8, -3, 9, -6, -1, -5, 7, 8, -2, 4, -1, -4, 5, 
                                   3, -2, 8, -7, 6, -9, 7, 8, 2, 4, -6, 9, -5, 1, 3, 6, -1, -3, -2, 9, 5, -4, 
                                   -8, -7, 8, 2, -4, 6, 7, -3, 1, 9, 5, -5, 7, 9, -8, -1, 4, -2, 
                                   3, 6],'integrity': 'e33e2de2fdbb25aacf25b299e101cccfdd2e1be4284acc257bcdc76737272af6', 'status':'ok'}
        result = solvee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
        
    def testInsert900_010(self):
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,8,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('fb50f09c24b3af3d2633b4b6648ea412785c9d2a9ef117e7fecb3d2993456d0e')
        testDictionary = {'status':'error: grid not solvable'}
        result = solvee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert900_020(self):
        self.setGrid('[a,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'error: invalid grid'}
        result = solvee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert900_030(self):
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('0000000000000000000000000000000000000000000000000000000000000000')
        testDictionary = {'status':'error: integrity mismatch'}
        result = solvee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)