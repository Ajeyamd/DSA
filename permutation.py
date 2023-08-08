def g(y):
    b = 0
    while y >= 3:
        (y,b) = (y/3,b+1)
    return(b)

print(g(728))