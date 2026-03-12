# question 1
number = int(input("please enter any number: "))
if(number%2==0):
    print(f"The number you enter {number} is even number")
else:
    print(f"The number you enter {number} is odd number")

#Question 2
age = int(input("please enter your age: "))
if(age >= 0):
    if(age < 60):
        if (age >= 13 and age <= 19):
            print("you are a teenager")
        else:
            if(age <= 12):
                print("you are a child")
            else:
                print("you are an adult")
    else:
        print("you are senior")
else:
    print("Invalid Age")


#Question 3
number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second number: "))
number3 = int(input("Enter Third number: "))

if((number1>=number2) and (number1>=number3)):
    print(f"{number1} is largest number")
elif((number2>=number1) and (number2>=number3)):
    print(f"{number2} is largest number")
else:
    print(f"{number3} is largest number")


#Question 4
number = int(input("Enter a number: "))

if number == 0:
    print("The number is a neutral number for addition and multiplication")
elif number == 1:
    print("The number is a neutral number for only multiplication")
else:
    print("The number is not a neutral number")
