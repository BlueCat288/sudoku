import hashlib
import functools
import re
from builtins import set

def _isdone(parms):
    integrit = parms['integrity']
    integritys = integrit.replace(' ','')
    grids = parms['grid']
    gridre = grids.replace(' ','')
    gridremove = gridre.replace('[','')
    gridremove2 = gridremove.replace(']','')
    gridsL = list(gridremove2.split(',')) 
    ERROR1 = 'incomplete'
    ERROR2 = 'warning'
    ERROR3 = 'error: invalid grid'
    ERROR4 = 'error: integrity mismatch'
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
        checkRow = splitList(gridsL, 9)
        for i in range(9):
            poslist = checkRow[i]
            for j in range(9):
                poslist[j] = abs(int(poslist[j]))
            sl = list(set(poslist))
            sl += [0] * (poslist.count(0) - 1)
            if len(poslist) != len(sl):
                return False
        return True       

    def if_column():
        list1 = colMajor()
        check = splitList(list1, 9)
        for i in range(9):
            poslist = check[i]
            for j in range(9):
                poslist[j] = abs(int(poslist[j]))
            sl = list(set(poslist))
            sl += [0] * (poslist.count(0) - 1)
            if len(poslist) != len(sl):
                return False
        return True
    
    def if_33grid():
        li = splitList(gridsL, 27)
        lil = splitList(li, 9)
        out1 =  []
        for x in range(3):
            for y in range(9):
                out1.append(lil[y][x])    
        out2 = functools.reduce(lambda x,y:x+y, out1)
        out3 = splitList(out2, 9)
        for i in range(9):
            poslist = out3[i]
            for j in range(9):
                poslist[j] = abs(int(poslist[j]))
            sl = list(set(poslist))
            sl += [0] * (poslist.count(0) - 1)
            if len(poslist) != len(sl):
                return False
        return True
    
    
    def if_zero():
        if '0' in gridsL:
            return False
        else:
            return  True
    
    if (if_grid()):
        if integritys == ToIntegrity():
            if ((if_33grid())&if_row())&(if_column()):
                if (if_zero()):
                    newDicthion['status'] = 'solved'
                else:
                    newDicthion['status'] = ERROR1
            else:
                newDicthion['status'] = ERROR2
        else:
            newDicthion['status'] = ERROR4
    else:
        newDicthion['status'] = ERROR3
        
    
    return newDicthion
