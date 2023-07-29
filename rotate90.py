#Rotating the matrix by 90degrees
#1 Transpose
#2 Rotate

import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

 #Create a Null Matrix
result=np.array([[0,0,0],[0,0,0],[0,0,0]])       

#STEP1 TRANSPOSE (ROW -> COLUMN)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        result[j][i] = arr[i][j]


#STEP 2 REVERSE THE ROW ELEMENTS
result=[row[::-1] for row in result]

for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j],end =" ")
    print()
    