import hashlib
import functools
import re
def _insert(parms):
    integrit = parms['integrity']
    integritys = integrit.replace(' ','')
    grids = parms['grid']
    gridre = grids.replace(' ','')
    gridremove = gridre.replace('[','')
    gridremove2 = gridremove.replace(']','')
    gridsL = list(gridremove2.split(',')) 
    ERROR1 = 'error: invalid cell reference'
    ERROR2 = 'error: missing cell reference'
    ERROR3 = 'error: attempt to change fixed hint'
    ERROR4 = 'error: invalid grid'
    ERROR5 = 'error: integrity mismatch'
    ERROR6 = 'error: invalid input value'
    WARNING1 = 'warning'
    newDicthion = {}
    
    def splitList(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0
        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg
    
        return out
    
    def colMajor():
        Liss = splitList(gridsL, 9)
        out1 = []
        for x in range(9):
            for y in range(9):
                out1.append(Liss[y][x])
        return out1
        
    def ToIntegrity():
        lits = colMajor()
        str1 = ''
        for ele in lits:
            eles = str(ele)
            str1 += eles
        
        intgt = hashlib.sha256(str1.encode()).hexdigest()
        return intgt
    
    def if_grid():
        check = re.findall(r'\d+', gridremove2)
        res = list(map(int, check))
        if (len(res) == 81):
            return True 
        else:
            return False
    
    def if_row():
        values = parms['value'].replace(' ','')
        Nvalue = str(int(values) * -1)
        checkRow = splitList(gridsL, 9)
        r = row_num
        if Nvalue in checkRow[r - 1]:
            return False
        else:
            return True
    def if_column():
        values = parms['value'].replace(' ','')
        Nvalue = str(int(values) * -1)
        list1 = colMajor()
        check = splitList(list1, 9)
        c = column_num
        if Nvalue in check[c -1]:
            return False
        else:
            return True
            
    def if_33grid():
        values = parms['value'].replace(' ','')
        valueInt = int(values)
        Nvalue = str(valueInt * -1)
        li = splitList(gridsL, 27)
        lil = splitList(li, 9)
        out1 =  []
        for x in range(3):
            for y in range(9):
                out1.append(lil[y][x])    
        out2 = functools.reduce(lambda x,y:x+y, out1)
        out3 = splitList(out2, 9)
        
        if (column_num in range(1,4)):
            if(row_num in range(1,4)):
                if Nvalue in out3[0]:
                    return False
                else:
                    return True
            elif(row_num in range(4,7)):
                if Nvalue in out3[1]:
                    return False
                else:
                    return True
            elif(row_num in range(7,10)):
                if Nvalue in out3[2]:
                    return False
                else:
                    return True
        
        elif (column_num in range(4,7)):
            if(row_num in range(1,4)):
                if Nvalue in out3[3]:
                    return False
                else:
                    return True
            elif(row_num in range(4,7)):
                if Nvalue in out3[4]:
                    return False
                else:
                    return True
            elif(row_num in range(7,10)):
                if Nvalue in out3[5]:
                    return False
                else:
                    return True
        
        elif (column_num in range(7,10)):
            if(row_num in range(1,4)):
                if Nvalue in out3[6]:
                    return False
                else:
                    return True
            elif(row_num in range(4,7)):
                if Nvalue in out3[7]:
                    return False
                else:
                    return True
            elif(row_num in range(7,10)):
                if Nvalue in out3[8]:
                    return False
                else:
                    return True
        else:
            return True
    
    def is_number(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    if ('cell' in parms):
        cells = parms['cell']
        column_num = int(cells[3])
        row_num = int(cells[1])
        if ((row_num in range(1,9)) & (column_num in range(1,9))):
            Dicthion = splitList(gridsL, 9)   
            if not if_grid():
                newDicthion['status'] = ERROR4
            else:
                if integritys == ToIntegrity():
                    if ('value' in parms):
                        values = parms['value'].replace(' ','')
                        if Dicthion[row_num - 1][column_num - 1] < '0':
                            newDicthion['status'] = ERROR3
                        else:
                            if (is_number(values)):
                                if int(values) in range(1,9):
                                    if ((if_33grid())&if_row())&(if_column()):
                                        Dicthion[row_num - 1][column_num - 1] = values
                                        gridsL = []
                                        gridsL = functools.reduce(lambda x,y:x+y, Dicthion)
                                        newIntDic = []
                                        for i in range(81):
                                            newIntDic.append(int(gridsL[i]))
                                        newINteg = ToIntegrity()
                                        print(newINteg)
                                        newDicthion['grid'] = newIntDic
                                        newDicthion['integrity'] = newINteg
                                        newDicthion['status'] = 'ok'
                                        print(newIntDic)
                                        print('pass')
                                    else:
                                        Dicthion[row_num - 1][column_num - 1] = values
                                        gridsL = []
                                        gridsL = functools.reduce(lambda x,y:x+y, Dicthion)
                                        newIntDic = []
                                        for i in range(81):
                                            newIntDic.append(int(gridsL[i]))
                                        newINteg = ToIntegrity()
                                        newDicthion['grid'] = newIntDic
                                        newDicthion['integrity'] = newINteg
                                        newDicthion['status'] = WARNING1
                                        print(newIntDic)
                                        print(newINteg)
                                        print('false')
                                        
                                else:
                                    newDicthion['status'] = ERROR6
                            else:
                                newDicthion['status'] = ERROR6

                    else:
                        Dicthion[row_num - 1][column_num - 1] = '0'
                        gridsL = []
                        gridsL = functools.reduce(lambda x,y:x+y, Dicthion)
                        newIntDic = []
                        for i in range(81):
                            newIntDic.append(int(gridsL[i]))
                        newDicthion['grid'] = newIntDic
                        newDicthion['integrity'] = integritys
                        newDicthion['status'] = 'ok'
                    
                else:
                    newDicthion['status'] = ERROR5
        else:
            newDicthion['status'] = ERROR1 
    else:
        newDicthion['status'] = ERROR2
    
    return newDicthion