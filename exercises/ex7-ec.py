# print a string
print("Mary had a little lamb.")
# print a string then append a format string containing "snow"
print("Its fleece was white as {}.".format('snow'))
# print a string
print("And everywhere that Mary went.")
# print . 10 times
print("." * 10) # what'd that do?

# set a bunch of vars to spell out CheeseBurger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# Print "Cheese" by concatenating the first 6 vars, and add a blank space at the end
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# Print "Burger" by concatenating the last 6 vars.
print(end7 + end8 + end9 + end10 + end11 + end12)
