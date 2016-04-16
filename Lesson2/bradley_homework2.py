#Colt Bradley
#1.14.16
#Python Homework 2: Basics

#Name input, then convert to string
name = raw_input('What is your name? ')
name = str(name)
#Birth year input, convert to integrer
year = raw_input('What year were you born? ')
year = int(year)
# hight input, convert to float and combine
feet,inches = raw_input('What is your height in feet and inches? (seperate the two numbers by a space) ').split()
feet = float(feet)
inches = float(inches)
height_in = feet*12 + inches

#Calculate age
import datetime
now = datetime.datetime.now()
year_c = now.year
year_c = int(year_c)
age = year_c - year
#Calculate height
conversion = .0254
height_m = height_in*conversion

#Print answer with calculated values
print "Hello World, my name is {} and I am {} years old. I am {} meters tall." .format(name, age, height_m)