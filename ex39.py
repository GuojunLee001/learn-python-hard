#coding:utf-8

# 定义字典，一个冒号，一个逗号的形式
# create a mapping of to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# 定义字典，一个冒号，一个逗号的形式
# create a basic set of states and some cities in then
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksnville'
}

# 字典的另外一种定义方法
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
# 最基本查找对应1
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
# 最基本查找对应2
print "Michigan's abbreviation is: ",states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by uesing the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: " , cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviation %s" % (state, abbrev)

# print evey city in state 
print '-' * 10
for abbrew, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])
		
print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."
	
# get a city with a default values
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'YX' is: %s" % city
