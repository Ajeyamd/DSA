def unique(list):
    a =[]
    for i in list:
        if i in a:
            return False
        else:
            a.append(i)
    return True
    
arr=[1,2,3,4,4,6,7,8,9]
print(unique(arr))