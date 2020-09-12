from builtins import str
def _create(parms):
    
    ERROR1 = 'error: invalid level'
    ERROR2 = 'error: invalid operation'
    op1 = parms['op']
    newDic = {}
    grid_1 = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, 
              -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, 
              -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
    
    grid_2 = [0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 
              0, 0, -9, 0, -1, -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 0, -7, 0, 0, 0, 0, -4, 
              -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8]
    
    grid_3 = [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, 
              -5, 0, 0, -6, 0, -4, 0, -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, -5, 0, 0, -9, 0, 
              0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, -1, -7, 0, -5, 0, 0]
    
    grid_4 = [0, -6, -7, 0, -2, 0, 0, 0, -3, 0, -8, 0, -7, 0, -3, 0, 0, -6, -1, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, 
              -3, 0, 0, 0, -8, -8, 0, 0, 0, -4, 0, 0, 0, -1, -4, 0, 0, 0, -6, 0, 0, -5, 0, -3, 0, 0, 0, 0, 0, 0, 0, -2, 
              -6, 0, 0, -2, 0, -4, 0, -3, 0, -5, 0, 0, 0, -9, 0, -8, -4, 0]
    
    grid_5 = [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 
              0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, 
              -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]
    stat = 'ok'
    inte_1 = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
    inte_2 = '39a4fbe2283d82b8dff98f36e6fcb09e6071653a77795e9527b26f90b4ad0d26'
    inte_3 = 'b594924588d873f60df054a64a7bfaa1d4196ab1d2000f1788a453c1765b05b8'
    inte_4 = '0ea83ad27c27241477102e2377f1bb14cc2f8c6125fbc85fab972c9ab0661319'
    inte_5 = '110a79143bc7c2b66faff5e8fe895320d402e4f91dbbe6b969931228abb84242'
    #grid1str = str(grid_1)
    
    if (op1 == 'create'):
    
        if not('level' in parms):
            newDic['grid'] = grid_3
            newDic['integrity'] = inte_3
            newDic['status'] = stat
        
        elif (parms['level'] == '1'):
            newDic['grid'] = grid_1
            newDic['integrity'] = inte_1
            newDic['status'] = stat
            
        elif (parms['level'] == '2'):
            newDic['grid'] = grid_2
            newDic['integrity'] = inte_2
            newDic['status'] = stat
            
        elif (parms['level'] == '3'):
            newDic['grid'] = grid_3
            newDic['integrity'] = inte_3
            newDic['status'] = stat
            
        elif (parms['level'] == '4'):
            newDic['grid'] = grid_4
            newDic['integrity'] = inte_4
            newDic['status'] = stat
            
        elif (parms['level'] == '5'):
            newDic['grid'] = grid_5
            newDic['integrity'] = inte_5
            newDic['status'] = stat
        
        else:
            newDic['status'] = ERROR1
    
    else:
        newDic['status'] = ERROR2
    
    
    return newDic
