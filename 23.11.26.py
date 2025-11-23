"""


a = 1

b = 2

c = 0

if a < b:

 c = a * b

print(c)
#.......................................................




money = int(input("Enter the bankaccount balance please: "))

if money >= 75000:
    print("The course is aquired sucsessfuly!")
print("Have a nice day!")    
#.......................................................


number = int(input("Введите число: "))
if (number % 2 ) == 0:
    print("Число чётное")
#.......................................................




 
money = int(input("Enter the bankaccount amount please: "))

if money >= 75000:
    print("Congratulations ! The course was sucsessfuly aquired! the remaining amount is " , money - 75000)
else:
    print("Sorry! there is not enough money on your bankaccount")    
print("Have a nice day!")    
#.......................................................




firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
allegedAmmount = int(input("Enter the alledged result: "))

if firstNumber + secondNumber == allegedAmmount:
    print("Congratulations!! You are right!")
else:
    print("Sorry! You are not right")
    print("The right answer is: " , firstNumber + secondNumber)    

#.......................................................



print("Добро пожаловать в игру «Угадай число»!")
print("Настя загадывает число. Дима, не подглядывай!")
nastya_number = int(input("Введите число: "))
dima_number = int(input("Введите число: "))

if nastya_number == dima_number:
    print("Ура! Угадал!")
else:
    print("Нет, это не то, что я загадала.")

#.......................................................    




firstNumb = int(input("Enter your first number: "))
secondNumb = int(input("Enter your second number: "))
thirdNumb = int(input("Enter your third number: "))

maximum = 0
if firstNumb > secondNumb:
     maximum = firstNumb
else:
 maximum = secondNumb
 if maximum < thirdNumb:
    maximum = thirdNumb

print(maximum)
#.......................................................

"""

