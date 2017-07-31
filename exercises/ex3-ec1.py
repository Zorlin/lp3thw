# ec3.1
# print a message
print("I will now count my chickens:")

# print "Hens", then divide 30 by 6 and add 25 and print result
print("Hens", 25 + 30 / 6)

# print Roosters then subtract from 100 the modulo of (25 * 3) / 4
# modulo is basically like - if I divide 75 by 4, what is the remainder
# which in this case is 3
# so we take that and subtract from 100 to get 97...
print("Roosters", 100 - 25 * 3 % 4)

# print a message
print("Now I will count the eggs:")

# take modulo of 4 % 2 which turns into 0
# then take 1 and divide by 4 giving 0.25
# then calculate the rest and print it
# 3 plus 2 plus 1 minus 5 plus 0 minus 0.25 + 6
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# prints a statement
print("Is it true that 3 + 2 < 5 - 7?")

# Compares whether "3 + 2" is less than "5 - 7"
print(3 + 2 < 5 - 7)

# print a question and then the answer
# 3 plus 2
print("What is 3 + 2?", 3 + 2)
# 5 minus 7
print("What is 5 - 7?", 5 - 7)

# prints a statement
print("Oh, that's why it's False.")

# prints a question
print("How about some more.")

# compares if 5 is greater than -2
print("Is it greater?", 5 > -2)
# compares if 5 is greater than or equal to -2
print("Is it greater or equal?", 5 >= -2)
# compares if 5 is less than or equal to -2
print("Is it less or equal?", 5 <= -2)
