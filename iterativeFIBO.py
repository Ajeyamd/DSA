n = int(input("Please Enter the number for Fibonacci series : "))
first,second=0,1
print("Fibonacci series are : ")
print("0")
print("1")
for i in range(0,n):
    if i<=1:
        result=i
    else:
      result = first + second;
      first = second;
      second = result;
      print(result)