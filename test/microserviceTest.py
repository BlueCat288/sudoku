from unittest import TestCase
import http.client
from urllib.parse import urlencode
import json
import sudoku.dispatch as sudoku
from sudoku.insert import _insert as insertt

class MicroserviceTest(TestCase):
    def setUp(self):
        self.PATH = '/sudoku?'
        self.PORT = 5000
        self.URL = 'localhost'
        self.inputDicthionary = {}
        
    def microservice(self, parm = ""):
        '''Issue HTTP Get and return result, which will be JSON string'''
        try:
            theParm = urlencode(parm)
            theConnection = http.client.HTTPConnection(self.URL, self.PORT)
            theConnection.request("GET", self.PATH + theParm)
            theStringResponse = str(theConnection.getresponse().read(), "utf-8")
        except Exception as e:
            theStringResponse = "{'diagnostic': '" + str(e) + "'}"
            
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = theStringResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element], str)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result
        
# Happy path
#    Test that each dispatched operation returns a status element
    def test100_010ShouldVerifyInstallOfCreate(self):
        parms = {}
        parms['op'] = 'create'
        result = self.microservice(parms)
        self.assertIn('status', result)
        #self.assertIn('create', result['status'])
 
    def test100_020ShouldVerifyInstallOfInsert(self):
        parms = {}
        parms['op'] = 'insert'
        result = self.microservice(parms)
        #self.assertIn('status', result)
        #self.assertIn('insert', result['status'])
        
    def test100_030ShouldVerifyInstallOfIsdone(self):
        parms = {}
        parms['op'] = 'isdone'
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertIn('isdone', result['status'])
        
    def test100_040ShouldVerifyInstallOfSolve(self):
        parms = {}
        parms['op'] = 'solve'
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertIn('solve', result['status'])
        
# Sad path
#    Verify status of 
#        1) missing parm
#        2) non-dict parm
#        3) missing "op" keyword
#        4) empty "op" keyword
#        5) invalid op name

    def test100_910ShouldErrOnMissingParm(self):
        result = self.microservice()
        self.assertIn('status', result)
        self.assertEquals(result['status'], sudoku.ERROR01)
        
    def test100_920ShouldErrOnNoOp(self):
        parms = {}
        parms['level'] = 3
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertEquals(result['status'], sudoku.ERROR01)
                
    def test100_930ShouldErrOnEmptyOp(self):
        parms = {}
        parms['op'] = ''
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertEquals(result['status'], sudoku.ERROR03)
        
    def test100_940ShouldErrOnUnknownOp(self):
        parms = {}
        parms['op'] = 'nop'
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertEquals(result['status'], sudoku.ERROR03)
        
#Insert

    
    def setCell(self, cel):
        self.inputDicthionary['cell'] = cel
        
    def setValue(self, vlu):
        self.inputDicthionary['value'] = vlu
        
    def setGrid(self, grd):
        self.inputDicthionary['grid'] = grd
        
    def setIntegrity(self, intgty):
        self.inputDicthionary['integrity'] = intgty
    #Happy path
    #    100_010: Insert 3 into row 3 column 1 with R3C1
    #    100_020: Insert 3 into row 3 column 1 with r3c1
    #    100_030: Remove row 3 column 1 with R3C1
    #    100_050: Insert a value thats only conflict in 3x3 box
    #    100_060: Insert a value thats only conflict in column
    #    100_070: Insert a value thats only conflict in row
    #
    #Sad path
    #    900_010: Insert a value into an invalid column with 0
    #    900_012: Insert a value into an invalid column with value < 0
    #    900_013: Insert a value into an invalid column with letter input
    #    900_020: Insert a value into an invalid row
    #    900_030: Insert a value with no location given
    #    900_040: Insert a value into a cell designated as fixed
    #    900_050: provide an invalid grid
    #    900_060: provide an integrity value that doesn't match the grid
    def testInsert100_010(self):
        self.setCell('R3C1')
        self.setValue('3')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 
                                   0, 0, -5, -8, -7, 0, 3, 0, -6, 0, -4, -8, 0, 
                                   -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 
                                   0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, 
                                   -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 
                                   0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 
                                   0],'integrity': '96484cb0a36217f3a7500c50b5b7d3b6012b336be9a1cae83abab27e48c7a627', 'status':'ok'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert100_020(self):
        self.setCell('r3c1')
        self.setValue('3')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 
                                   0, 0, -5, -8, -7, 0, 3, 0, -6, 0, -4, -8, 0, 
                                   -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 
                                   0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, 
                                   -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 
                                   0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 
                                   0],'integrity': '96484cb0a36217f3a7500c50b5b7d3b6012b336be9a1cae83abab27e48c7a627', 'status':'ok'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert100_030(self):
        self.setCell('R3C1')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 
                                   0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, 
                                   -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 
                                   0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, 
                                   -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 
                                   0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 
                                   0],'integrity': '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5', 'status':'ok'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)

    def testInsert100_050(self):
        self.setCell('R2C4')
        self.setValue('6')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 
                                   6, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, 
                                   -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 
                                   0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, 
                                   -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 
                                   0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 
                                   0],'integrity': 'eb5437d4b23266f2e4deda92f850dc11994ded6e1c9e4e6427612a07a264055a', 'status':'warning'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert100_060(self):
        self.setCell('R4C1')
        self.setValue('4')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 
                                   0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, 
                                   -9, -5, 4, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 
                                   0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, 
                                   -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 
                                   0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 
                                   0],'integrity': 'c101472b713bb8130866b58d1a614513bd6c3a9955574313d86a5a69cd3e2a48', 'status':'warning'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert100_070(self):
        self.setCell('R2C3')
        self.setValue('7')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'grid': [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 7, 
                                   0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, 
                                   -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 
                                   0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, 
                                   -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 
                                   0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 
                                   0],'integrity': '66e8bd7e6d2222b387ad95e39a858dd7c9c36ad88c72fcc7e9c82038166767c5', 'status':'warning'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    #
    #
    #Sad paths
    def testInsert900_010(self):
        self.setCell('R3C0')
        self.setValue('3')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'error: invalid cell reference'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert900_011(self):
        self.setCell('R3C1')
        self.setValue('-3')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'error: invalid input value'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert900_012(self):
        self.setCell('R3C1')
        self.setValue('j')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'error: invalid input value'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
        
    
    def testInsert900_020(self):
        self.setCell('R0C3')
        self.setValue('3')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'error: invalid cell reference'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
        
    def testInsert900_030(self):
        self.setValue('3')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'error: missing cell reference'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert900_040(self):
        self.setCell('R1C1')
        self.setValue('3')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'error: attempt to change fixed hint'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert900_050(self):
        self.setCell('R3C2')
        self.setValue('3')
        self.setGrid('[a,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5')
        testDictionary = {'status':'error: invalid grid'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)
    
    def testInsert900_060(self):
        self.setCell('R3C1')
        self.setValue('3')
        self.setGrid('[-8,-1,-5,-7,-6,-9,-3,-2,0,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0]')
        self.setIntegrity('0000000000000000000000000000000000000000000000000000000000000000')
        testDictionary = {'status':'error: integrity mismatch'}
        result = insertt(self.inputDicthionary)
        self.assertEqual(result, testDictionary)