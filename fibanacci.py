n = int(input("Enter any number:"))
a = 0
b = 1
print(a)
print(b)
sum = a+b
for i in range(n):
    if(n<0):
        print("Enter any value greater than 0:")
    elif(n == 0):
        print(a)
    else:
        print(sum)
        a = b
        b = sum
        sum = a+b
    
    
