# Set 100 cars
cars = 100

# Define space in a car as being 4
space_in_a_car = 4.0

# There are 30 drivers
drivers = 30

# There are 90 passengers
passengers = 90

# We can subtract drivers from cars to find how many cars won't be driven
cars_not_driven = cars - drivers

# Every car being driven needs a driver and vice versa
cars_driven = drivers

# We can find spare capacity by multiplying cars driven by space
carpool_capacity = cars_driven * space_in_a_car

# We can find average number of passengers in a car by dividing passengers by cars.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# ec4.0
# On line 8 you originally tried to reference car_pool_capacity which doesn't exist.
# it should instead be carpool_capacity.

# ec4.1
# No, its not necessary in this case. Output is the same.

# ec4.2 4.4 4.5 4.6
# Done.
