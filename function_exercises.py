# FUNCTION EXERCISES

# 1. Define a function named is_two. 
#    It should accept one input and return True if the passed input is either 
#    the number or the string 2, False otherwise.
def is_two(t):
    if t in [2, '2']:
        return True
    else:
        return False
is_two(2)
is_two('2')
is_two(54)

# 2. Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.
def is_vowel(string):
    if string.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
is_vowel('a')
is_vowel('l')
is_vowel('i')

# 3. Define a function named is_consonant. 
#    It should return True if the passed string is a consonant, False otherwise. 
#    Use your is_vowel function to accomplish this.
def is_consonant(string):
    if is_vowel(string) == False:
        return True
    else:
        return False
is_consonant('a')
is_consonant('l')
is_consonant('i')

# 4. Define a function that accepts a string that is a word. 
#    The function should capitalize the first letter of the word 
#    if the word starts with a consonant.
def capitalized_if_consonant(word):
    if is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        return word
capitalized_if_consonant('consonant')
capitalized_if_consonant('axolotl')
capitalized_if_consonant('butterfly')

# 5. Define a function named calculate_tip. 
#    It should accept a tip percentage (a number between 0 and 1) and the bill total, 
#    and return the amount to tip.
def calculate_tip(tip_percentage, bill_total):
    tip_amount = round(tip_percentage * bill_total, 2)
    return f'Tip this much: ${tip_amount}'
calculate_tip(0.28, 104)
calculate_tip(0.15, 29)
calculate_tip(0.32, 12)

# 6. Define a function named apply_discount. 
#    It should accept a original price, and a discount percentage, and 
#    return the price after the discount is applied.
def apply_discount(og_price, discount_percentage):
    price_after_discount = round(og_price - (og_price * discount_percentage), 2)
    return f'The discounted price is: ${price_after_discount}'
apply_discount(110, 0.25)
apply_discount(16, 0.08)
apply_discount(1999.99, .1776)

# 7. Define a function named handle_commas. 
#    It should accept a string that is a number that contains commas in it as input, 
#    and return a number as output.

# I interpreted this as returning the string without commas and as an int type
def handle_commas(string):
    string_without_commas =  string.replace(',', '')
    return int(string_without_commas)
handle_commas('1,000')
handle_commas('1,000,354')
handle_commas('9,542,126,038')

# 8. Define a function named get_letter_grade. 
#    It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(num_grade):
    if num_grade >= 90:
        return 'A'
    elif 80 <= num_grade < 90:
        return 'B'
    elif 70 <= num_grade < 80:
        return 'C'
    elif 60 <= num_grade < 70:
        return 'D'
    else:
        return 'F'
get_letter_grade(90)
get_letter_grade(84)
get_letter_grade(27)

# 9. Define a function named remove_vowels 
#    that accepts a string and returns a string with all the vowels removed.


# 10. Define a function named normalize_name. 
#     It should accept a string and return a valid python identifier, that is:
#     - anything that is not a valid python identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores
#     - for example:
#       - Name will become name
#       - First Name will become first_name
#       - % Completed will become completed


# 11. Write a function named cumulative_sum that 
#     accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#     - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#     - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]