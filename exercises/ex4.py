cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
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
