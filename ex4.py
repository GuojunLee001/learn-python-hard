# _*_ coding : utf-8 _*_

# 变量是用于制定对象，避免重复劳动
cars = 100
space_in_a_car = 4.0
drivers = 30 
passengers = 90 
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# 文本一定要用“”，变量可以不用“” ，此处是因为变量不是文本
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
  