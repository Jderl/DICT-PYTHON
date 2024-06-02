#input function 
#input (Prompt)
#int function

name = input ("Enter your name: ")
print (" My name is ", name)

#int and input
num1 = int(input("Please Enter num  1: "))
num2 = int(input("Please Enter num  2: "))

print(num1 + num2)

#with def function 
def addNum(num1, num2):
    total = num1 + num2 
    return (total)


num3 = int(input("Please Enter num  3: "))
num4 = int(input("Please Enter num  4: "))

print("Total: ", addNum(num3, num4 ))