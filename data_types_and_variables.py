# Data Types and Variables Exercises
# Write some Python code, that is, variables and operators, to describe the following scenarios.

# You have rented some movies for your kids: 
# - The little mermaid (for 3 days), 
# - Brother Bear (for 5 days, they love it), and 
# - Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

price_per_day = 3
little_mermaid = 3
brother_bear = 5
hercules = 1
total_cost = price_per_day * (little_mermaid + brother_bear + hercules)
print('The total cost will be $' + str(total_cost))


# Suppose you're working as a contractor for 3 companies: 
# - Google, Amazon and Facebook, they pay you a different rate per hour. 
# - Google pays 400 dollars per hour, 
# - Amazon 380, and 
# - Facebook 350. 
# How much will you receive in payment for this week? 
# - You worked 10 hours for Facebook, 
# - 6 hours for Google and 
# - 4 hours for Amazon.

google_wage = 400
amazon_wage = 380
facebook_wage = 350
google_hours = 6
amazon_hours = 4
facebook_hours = 10
total_payment = (facebook_hours * facebook_wage) + (google_hours * google_wage) + (amazon_hours * amazon_wage)
print('This week\'s payment will be $' + str(total_payment))


# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

class_is_not_full = True
conflicting_with_schedule = False
student_can_enroll = class_is_not_full and not conflicting_with_schedule
print(student_can_enroll)


# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a specific amount of products.

items_bought = 1
bought_more_than_2_items = items_bought >= 2
offer_has_not_expired = True
is_a_premium_member = True
can_apply_product_offer = (is_a_premium_member or bought_more_than_2_items) and offer_has_not_expired
print(can_apply_product_offer)


# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

is_at_least_5_characters = len(password) >= 5
is_less_than_21_characters = len(username) <= 20
is_not_same_as_username = password != username
not_start_or_end_with_whitespace = username == username.strip() and password == password.strip()