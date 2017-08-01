# set var types_of_people to 10
types_of_people = 10

# evaluate f-string then set var x to it
x = f"There are {types_of_people} types of people."

# set var binary to string "binary"
binary = "binary"
# set var do_not to string "don't"
do_not = "don't"

# evaluate f-string then set var y to it
# string inside a string #1 and #2
y = f"Those who know {binary} and those who {do_not}."

# output contents of x
print(x)
# output contents of y
print(y)

# output a sentence containing x
# string inside a string #3
print(f"I said: {x}")
# output a sentence containing y, adding quotes around it
# string inside a string #4
print(f"I also said: '{y}'")

# set var hilarious to "False"
hilarious = False
# set var joke_evaluation to a string containing an object
joke_evaluation = "Isn't that joke so funny?! {}"

# print joke_evaluation and cast the object to hilarious which is set to false
print(joke_evaluation.format(hilarious))

# set var w to half of a string
w = "This is the left side of..."
# set var e to the other half of a string
e = "a string with a right side."

# print them together making them a single string
print(w + e)

# ec6.4: because + can mean addition when dealing with numbers, but when dealing with strings
# it means concatenation.
