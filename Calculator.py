print("Simple Calculator:\n")
print("1.Addition")
print("2.Subtraction")
print("3.Multication")
print("4.Division")
print("5.Power\n")
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Give index Number for Operation:"))
if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a*b)
elif(c==4):
    if(b>0):
        print(a/b)
    else:
        print("Zero Division Error")
elif(c==5):
    print(pow(a,b))

else:
    print("Invalid Number")
