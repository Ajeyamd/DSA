n = int(input("please give a number for fibonacci series : "))
first,second=0,1
print("fibonacci series are : ")
for i in range(0,n):
    if i<=1:
        result=i
    else:
      result = first + second;
      first = second;
      second = result;
    print(result)