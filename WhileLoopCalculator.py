# Ben Readman
# While loop Calculator
x = 0
go = 'y'
num = int(input("Please enter the first number: "))
minnum = num
maxnum = num
while go == 'y':
    num2 = int(input("Please enter the next number: "))
    avrg = num + num2
    num = num2
    if minnum > num2:
        minnum = num2
    else:
        minnum = minnum
    if maxnum < num2:
        maxnum = num2
    else:
        maxnum = maxnum
    print()
    go = input("Would you like to enter another number (y/n)? ")
    x +=1
if go == 'n':
    avrg = avrg/x
    print()
    print("Okay, the minimum is ",minnum,"\nThe maximum is ",maxnum,"\nThe average is ",avrg,sep='')
else:
    go = input("Please enter a valid answer (y/n): ")
