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
n = int(input('Please enter a number:'))
for i in range(1, 11):
    print(n, 'x', i, '=', (n*i))

#     ii. Create a for loop that uses print to create the output shown below.
for i in range(1, 10):
    print(i*str(i))

#   c. break and continue
#     i. Prompt the user for an odd number between 1 and 50.
#        Use a loop and a break statement to continue prompting the user if they enter invalid input. 
#        (Hint: use the isdigit method on strings to determine this).
#        Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
#        except for the number the user entered.
user_num_input = input('Please enter an odd number between 1 and 50:')
while True:
    if user_num_input.isdigit() != True:
        print('Invalid input')
        user_num_input = input('Please enter an odd number between 1 and 50:')
        continue
    elif int(user_num_input) not in range(1, 51, 2):
        print('Invalid input')
        user_num_input = input('Please enter an odd number between 1 and 50:')
    else: break
print()
print('The number to skip is:',user_num_input)
print()
for i in range(1, 51):
    if i % 2 == 0:
        continue
    elif i == int(user_num_input):
        print('Yikes! Skipping this number:', i)
    else:
        print('Here is an odd number:', i)

# The input function can be used to prompt for input and use that input in your python code. 

#   d. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#      (Hints: first make sure that the value the user entered is a valid number, 
#      also note that the input function returns a string, so you'll need to convert this to a numeric type.)
user_pos_input = input('Please enter a number between 1 and 50: ')
while True:
    if user_pos_input.isdigit() != True:
        print('Invalid input')
        user_pos_input = input('Please enter a number between 1 and 50:')
        continue
    elif int(user_pos_input) <= 0:
        print('Invalid input')
        user_pos_input = input('Please enter a number between 1 and 50:')
    elif int(user_pos_input) > 50:
        print('Invalid input')
        user_pos_input = input('Please enter a number between 1 and 50:')
    else:
        break
for n in range(-1, int(user_pos_input)):
    n = n + 1
    print(n)


#   e. Write a program that prompts the user for a positive integer. 
#      Next write a loop that prints out the numbers from the number the user entered down to 1.
user_pos_input = input('Please enter a positive integer: ')
while True:
    if user_pos_input.isdigit() != True:
        print('Invalid input')
        user_pos_input = input('Please enter a positive integer: ')
        continue
    elif int(user_pos_input) <= 0:
        print('Invalid input')
        user_pos_input = input('Please enter a positive integer: ')
    else:
        break
for n in range(0, int(user_pos_input)):
    n = int(user_pos_input) - n
    print(n)

# 3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

# 4. Display a table of powers.
#   - Prompt the user to enter an integer.
#   - Display a table of squares and cubes from 1 to the value entered.
#   - Ask if the user wants to continue.
#   - Assume that the user will enter valid data.
#   - Only continue if the user agrees to.
sq_input = input('Please enter an integer: ')
y_n_input = input('Would you like to see its powers? y/n ')
if y_n_input.lower() == 'y':
    print('\nHere they are!\n')
    print(f'Number|\tSquare|\tCube')
    print(f'------|\t------|\t----')
    for n in range(1, int(sq_input) + 1):
        print(f'{n:6}|\t{(n ** 2):6}|\t{(n ** 3):4}')

# 5. Convert given number grades into letter grades.
#   - Prompt the user for a numerical grade from 0 to 100.
#   - Display the corresponding letter grade.
#   - Prompt the user to continue.
#   - Assume that the user will enter valid integers for the grades.
#   - The application should only continue if the user agrees to.
#   - Grade Ranges:
#     - A : 100 - 88
#     - B : 87 - 80
#     - C : 79 - 67
#     - D : 66 - 60
#     - F : 59 - 0
#   Bonus: Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

grade_input = input('Please enter a grade (0-100)')
cont_input = input('Would you like to continue? Y/N ')
while cont_input.upper() == 'Y':
    if int(grade_input) in range(0, 60):
        if int(grade_input) in range(0, 2):
            print('F-')
        elif int(grade_input) in range(58,60):
            print('F+')
        else:
            print('F')
        break
    elif int(grade_input) in range(60, 67):
        if int(grade_input) in range(60, 62):
            print('D-')
        elif int(grade_input) in range(65,67):
            print('D+')
        else:
            print('D')
        break
    elif int(grade_input) in range(67, 80):
        if int(grade_input) in range(67, 69):
            print('C-')
        elif int(grade_input) in range(78,80):
            print('C+')
        else:
            print('C')
        break
    elif int(grade_input) in range(80, 88):
        if int(grade_input) in range(80, 82):
            print('B-')
        elif int(grade_input) in range(86,88):
            print('B+')
        else:
            print('B')
        break
    else:
        if int(grade_input) in range(88, 90):
            print('A-')
        elif int(grade_input) in range(99,101):
            print('A+')
        else:
            print('A')
        break

# 6. Create a list of dictionaries where each dictionary represents a book that you have read.
#    Each dictionary in the list should have the keys title, author, and genre.
#    Loop through the list and print out information about each book.
#   - Prompt the user to enter a genre, then loop through your books list and 
#     print out the titles of all the books in that genre.
book1 = dict(title = 'The Hitchhiker\'s Guide to the Galaxy', 
             author = 'Douglas Adams', 
             genre = ['science fiction', 'comedy'])
book2 = dict(title = 'Wuthering Heights',
             author = 'Emily Bronte',
             genre = ['romance', 'tragedy'])
book3 = dict(title = 'Dracula',
             author = 'Bram Stoker',
             genre = ['horror', 'gothic fiction'])
book4 = dict(title = 'Frankenstein',
             author = 'Mary Shelley',
             genre = ['horror', 'science fiction', 'gothic fiction', 'tragedy'])
fiction_books = [book1, book2, book3, book4]
for book in fiction_books:
    print('Title: ',book['title'], '\nAuthor: ',book['author'], '\nGenres: ',book['genre'],'\n')
print()
genre_input = input('Please enter a book genre: ')
titles = [book['title'] for book in fiction_books if genre_input.lower() in book['genre']]
print(f'{genre_input.title()} book(s):', titles)