# CONTROL STRUCTURES EXERCISES

# 1. Conditional Basics
#   a. prompt the user for a day of the week, print out whether the day is Monday or not
user_input = input('Please enter a day of the week:')
if user_input.lower() == 'monday':
    print('The day is Monday')
else:
    print('The day is not Monday')

#   b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
user_input = input('Please enter a day of the week:')
if user_input.lower() in ['saturday', 'sunday']:
    print('The day is a weekend')
else:
    print('The day is a weekday')

#   c. create variables and make up values for
#     - the number of hours worked in one week
#     - the hourly rate
#     - how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours
hours_worked = 45
hourly_rate = 20
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    hours_worked = hours_worked - overtime_hours
else: overtime_pay = 0
paycheck_amount = (hours_worked * hourly_rate) + overtime_pay
print('This week\'s paycheck will be $' + str(paycheck_amount))


# 2. Loop Basics

#   a. While
#     - Create an integer variable i with a value of 5.
#     - Create a while loop that runs so long as i is less than or equal to 15
#     - Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i = i + 1

#     - Create a while loop that will count by 2's starting with 0 and ending at 100. 
#       Follow each number with a new line.
i = 0
while i <= 100:
    print(i, end = '\n')
    i = i + 2

#     - Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i = i - 5

#     - Create a while loop that starts at 2, and displays the number squared on each line 
#       while the number is less than 1,000,000.
i = 2
while i < 1000000:
    print(i)
    i = i ** 2

#     - Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i = i - 5

#   b. For Loops
#     i. Write some code that prompts the user for a number, 
#       then shows a multiplication table up through 10 for that number.

#     ii. Create a for loop that uses print to create the output shown below.

