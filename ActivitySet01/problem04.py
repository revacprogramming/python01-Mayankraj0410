# Conditional Execution
'''Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.'''


hrs =input("enter the hours:")
h = float(hrs)
rate =input("Enter the rate:")
r = float(rate)
if h<=40:
  print(hrs*rate)
elif h>40:
  print (40*r+(h-40)*1.5*r)

'''
score = input("Enter Score: ")
s =  float(score)
x = 'Error'
if s >= 0.9:
	x = 'A'
elif s >=0.8:
	x='B'
elif s >=0.7:
	x='C'
elif s >= 0.6:
	x='D'
elif s < .6:
	x ='F'
else:
	x ="Out of Range"
print (x)

'''