"""


a = int(input("Introduce the first number: "))
b = int(input("Introduce the second number: "))
print(a+b)


#.......................................................................


a = int(input("Introduce the first number: "))
b = int(input("Introduce the second number: "))
c = int(input("Introduce the third number: "))
d = int(input("Introduce the forth number: "))

answer = 2 * (c + 5 + ((a*b) / (4*b))) * (d - (2 * ((a**3) / 30))) - 10

print(answer)
#.......................................................................


a = '2'
b = '5'
c = '3'
num = 6 ** int(a) + (7 - int(b)) * int(c)
print(num)
#.......................................................................



tons_OF_apples = 41
box_tons_capacity = 3


boxes_being_loaded = tons_OF_apples // box_tons_capacity
tons_of_apples_left = tons_OF_apples % box_tons_capacity

print( "We can load: ", boxes_being_loaded , "boxes")
print("There will be ", tons_of_apples_left , "tons of apple left")
#.......................................................................




number = int(input("Insert the number please: ")) 

appartmentNumber = number // 10
houseNumber = number % 10


print("House number is: ", houseNumber)
print("Appartment number is: ", appartmentNumber)

#.......................................................................

"""

