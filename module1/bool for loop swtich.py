change_num = True #establish bool switch True
for i in f: #for element in sequence
    if i == '/': # if element is comapred to /
        change_num = False # switch bool False
    if change_num: # if bool is switch is triggered
        num = num * 10 + int(i) # num var = var * 10 + an integer of the element in f
    else: #otherwise
        denom = denom * 10 + int(i) # var2 = var2 * 10 + integer of the element in f
    
