#Second Day Exercises

#Exercise 1
print('EXERCISE 1') 
msg = """This is the Greatest!
Enter two numbers, and the greatest will be returned
First number>>> """
firstNum = int(input(msg))
secondNum = int(input('Second number >>> '))
if firstNum > secondNum:
	result = firstNum
elif firstNum < secondNum:
	result = secondNum
else: result = 'NONE. They are even'
print('The GREATEST number is ' + str(result))
print('\n\n')
#==============================================================================
#Exercise 2
print('EXERCISE 2')
msg = """This is Multiplication Table!
Enter a number and its multiplication table will be returned
Number >>> """
num = int(input(msg))
for count in range(1,11):
	toPrint = str(num) + ' x ' + str(count) + ' = ' + str(num * count)
	print(toPrint)
print('\n\n')
#==============================================================================
#Exercise 3
print('EXERCISE 3')
star = '*'
rows = int(input('Enter the number of required rows >>> '))
for row in range(-rows+1, rows):
	toPrint = star * (rows - abs(row))
	print(toPrint)
print('\n\n')
#==============================================================================
#Exercise 4
#The output would be x, y, z, b
print('EXERCISE 4')
letters = ['x', 'y', 'z', 'a', 'b', 'c']
for letter in letters:
	if letter == 'a': continue
	elif letter == 'c': break
	print(letter)
print('\n\n')
#==============================================================================
#Exercise 5
#The output would be 12, 15, 18, 21, 14
print('EXERCISE 5')
for num in range(12, 25, 3):
	print(num)
print('\n\n')
#==============================================================================
#Exercise 6
#The output would be 1, 2, 3
print('EXERCISE 6')
count = 1
while count < 6:
	print(count)
	if count == 3: break
	count += 1
print('\n\n')
#==============================================================================
#Exercise 7
print('EXERCISE 7')
msg = """This is SUM!
Enter a number, and the summation of all numbers between 0 and the selected number will be returned
Number >>> """
num = int(input(msg))
result = sum(range(0, num+1))
print(result)
print('\n\n')
#==============================================================================
#Exercise 8
print('EXERCISE 8')
msg = """This is ODD or EVEN!
Enter a number, and you will be told if it was Odd or Even
Number>>>"""
num = int(input(msg))
result = 'Even' if num % 2 == 0 else 'Odd'
print(str(num) + ' is ' + result) 
print('\n\n')
#==============================================================================
#Exercise 9
print('EXERCISE 9')
space = ' '
diamonds = int(input('Enter a number less than or equal 9 to draw a diamond>>> '))
toPrint = ''
numbers = ''
for diamond in range(-diamonds+1, diamonds):
	for num in range(1, diamonds-abs(diamond)+1):
			numbers += str(num) 	
			spaces = diamonds - num
	numbers += numbers[-2::-1]
	print(space * spaces + numbers)
	numbers = ''
print('\n\n')
#==============================================================================
#Exercise 10
print('EXERCISE 10')
while 1:
	try:
		num = int(input("Enter an integer>>> "))
		break
	except ValueError:
		print("It is not an integer and you know it! again!")
print("Now that is an integer!")
print('\n\n')
#==============================================================================
#Exercise 11
#The output would be Error Occurred and Handled
print('EXERCISE 11')
try:
	a = 3
	if a < 4:
		b = a/(a-3)
	print('Value of b = ', b)
except(ZeroDivisionError, NameError):
	print('\nError Occurred and Handled')
print('\n\n')