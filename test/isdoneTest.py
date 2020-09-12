from unittest import TestCase
import sudoku.isdone as sudoku 
from sudoku.isdone import _isdone as isdonee

class InsertTest(TestCase):
    TestCase.maxDiff = None
    def setUp(self):
        self.inputDicthionary = {}

        
    def setGrid(self, grd):
        self.inputDicthionary['grid'] = grd
        
    def setIntegrity(self, intgty):
        self.inputDicthionary['integrity'] = intgty
        
    def testInsert100_010(self):
        self.setGrid('[4,-5,-8,-9,3,-1,-6,7,2,-2,3,7,-5,-8,6,9,-4,-1,-9,6,1,7,4,2,3,-5,8,-3,9,-6,-1,-5,7,8,-2,4,-1,-4,5,3,-2,8,-7,6,-9,7,8,2,4,-6,9,-5,1,3,6,-1,-3,-2,9,5,-4,-8,-7,8,2,-4,6,7,-3,1,9,5,-5,7,9,-8,-1,4,-2,3,6]')
        self.setIntegrity('e33e2de2fdbb25aacf25b299e101cccfdd2e1be4284acc257bcdc76737272af6')
        testDictionary = {'status':'solved'}
        result = isdonee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert100_020(self):
        self.setGrid('-8, -1, -5, -7, -6, -9, -3, -2, 4, -4, -9, 2, 3, 1, -5, -8, -7, 6, 3, 7, -6, 2, -4, -8, 1, -9, -5, 6, -8, -1, 9, 7, -3, 5, 4, -2, 2, -5, 4, -1, -8, 6, -9, 3, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 3, 6, 5, -7, 2, -1, -8, -5, -2, 7, -8, -9, 1, -4, -6, -3, -1, -6, 8, -4, -3, -2, -7, 5, 9]')
        self.setIntegrity('5d3bfc4209683f988d09888d0ef6e0d1e9cfe541fbc8c82bf0590889ee462dcf')
        testDictionary = {'status':'solved'}
        result = isdonee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
   
    def testInsert100_030(self):
        self.setGrid('[1, 6, -3, 8, 4, -7, 9, -2, 5, -4, 9, -7, 2, 1, -5, -3, 6, 8, 2, 5, -8, -9, 3, -6, -7, 4, -1, -8, 3, -2, -5, 9, 1, -6, 7, -4, 9, -7, 6, 4, -8, 3, -1, -5, 2, -5, 4, 1, -7, -6, 2, 8, 3, -9, 7, 8, -5, 3, 2, -9, 4, 1, -6, 3, -1, 9, -6, 5, 4, -2, -8, 7, 6, -2, -4, -1, -7, 8, -5, 9, 3]')
        self.setIntegrity('ec6c0462503c83794dab7b293bda2f35fdfa1a858f975a5d293fa8f3d70015ca')
        testDictionary = {'status':'solved'}
        result = isdonee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert100_040(self):
        self.setGrid('[-2, 4, 8, 7, -5, 3, -9, -1, 6, -6, 3, 1, 9, 4, -8, 2, 7, 5, 9, 7, 5, 1, 6, 2, 4, -3, 8, 5, -2, -4, 3, 7, 9, 8, 6, 1, 1, 8, 6, -4, 2, 5, 3, 9, -7, 7, -9, -3, 8, -1, 6, -5, 2, 4, 3, 6, 9, 5, 8, -7, 1, 4, -2, 8, -1, 7, 2, -3, 4, 6, -5, 9, -4, 5, 2, -6, 9, 1, 7, 8, 3]')
        self.setIntegrity('21bc00d8038232acc79ff372bd3047617d6e4bafb47e2f77896c08b56ca26503')
        testDictionary = {'status':'solved'}
        result = isdonee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
        
    def testInsert100_050(self):
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'incomplete'}
        result = isdonee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
        
    def testInsert100_060(self):
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,8,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('fb50f09c24b3af3d2633b4b6648ea412785c9d2a9ef117e7fecb3d2993456d0e')
        testDictionary = {'status':'warning'}
        result = isdonee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
        
    def testInsert900_010(self):
        self.setGrid('[a,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'error: invalid grid'}
        result = isdonee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
        
    def testInsert900_020(self):
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('0000000000000000000000000000000000000000000000000000000000000000')
        testDictionary = {'status':'error: integrity mismatch'}
        result = isdonee(self.inputDicthionary)
        self.assertEqual(result, testDictionary)