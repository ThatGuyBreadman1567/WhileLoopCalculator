# Ben Readman
# While loop Calculator
go = 'yes'
num = int(input("Please enter the first number: "))
min = num
max = num
while go == 'yes':
    num = int(input("Please enter the next number: "))
    if min > num:
        min = num