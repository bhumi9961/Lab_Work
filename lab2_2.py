#Question 1 
a = int(input("Enter First number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a > b):
    if(a > c):
        print("First number is the largest number")
    else:
        print("third number is the largest number")
else:
    if(b > c):
        print("Second number is largest number")
    else:
        print("third number is largest number")


#question 2
a = int(input("Enter First number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a < b):
    if(a < c):
        print("First number is the smallest number")
    else:
        print("third number is the smallest number")
else:
    if(b < c):
        print("Second number is smallest number")
    else:
        print("third number is smallest number")

#question 3
a = int(input("Enter First number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a > b):
    if (a > d):
        if(a > c):
            print(" First number is maximum")
        else: 
            print("Third number is maximum")
    else:
        if(d > c):
            print("Fourth number is maximum")
        else:
            print("Third number is maximum")
else:
    if(b > c):
        if(b > d):
            print("Second number is maximum")
        else:
            print("Fourth number is maximum")
    else: 
        if(c > d):
            print("Third number is maximum")
        else:
            print("Fourth number is maximum")

#Question 4
a = int(input("Please enter first number: "))
b = int(input("please enter second number: "))

operator = input("please enter the operator of your choice: ")

match operator:
    case '+' :
        d = a + b
        print(f"a + b = {d}")
    case '-' :
        d = a - b
        print(f"a - b = {d}")
    case '*' :
        d = a * b
        print(f"a * b = {d}")
    case '/' :
        d = a / b
        print(f"a / b = {d}")
    case _ :
        print("invalid Operators")

#Question 5
print("Welcome to fast food order system")
print("Press 1 for Sandwich")
print("Press 2 for Pizza")
print("Press 3 for Burger")

menu = input("please select the menu option you want to order: ")

match menu: 
    case '1': 
        print("you have placed order for Sandwitch")
        print("Press 1 for mayo sandwich")
        print("Press 2 for vegetable sandwich")
        submenu = input("please select the type of Sandwich you want to order: ")
        match submenu:
            case '1': 
                print("you have placed order for mayo Sandwich")
            case '2': 
                print("you have placed order for vegetable Sandwich")
            case _:
                print("invalid order")
    case '2': 
        print("You have placed order for Pizza")
        print("Press 1 for Thin crust Pizza")
        print("Press 2 for Thik crust Pizza")
        submenu = input("please select the type of Pizza you want to order: ")
        match submenu:
            case '1': 
                print("you have placed order for Thin crust Pizza")
            case '2': 
                print("you have placed order for Thik crust Pizza")
            case _:
                print("invalid order")
    case '3': 
        print("You have placed order for Burger")
        print("Press 1 for Aloo patty Burger")
        print("Press 2 for Cheese corn Burger")
        submenu = input("please select the type of Burger you want to order: ")
        match submenu:
            case '1': 
                print("you have placed order for Aloo patty Burger")
            case '2': 
                print("you have placed order for Cheese corn Burger")
            case _:
                print("invalid order")
    case _:
        print("Invalid order entry")


#Question 6
print("Welcome to Telecom calling system")
print("Press 1 for English")
print("Press 2 for Hindi")
print("Press 3 for Gujarati")

language = input("please select the language: ")

match language: 
    case '1': 
        print("you have selected English")
        print("Press 1 for Balance Inquiry")
        print("Press 2 for Recharge")
        print("Press 3 for Customer Care")

        submenu = input("please select the appropriate option: ")
        match submenu:
            case '1': 
                print("your Balance is $100")
            case '2': 
                print("Recharge service selected")
            case '3':
                print("connecting customer care agent")
            case _:
                print("invalid English menu choice")
    case '2': 
        print("You have selected Hindi")
        print("1 दबाएं बैलेंस जानकारी के लिए")
        print("2 दबाएं रिचार्ज के लिए")
        print("3 दबाएं कस्टमर केयर के लिए")
        submenu = input("अपना विकल्प दर्ज करें: ")
        match submenu:
            case '1': 
                print("आपका बैलेंस ₹100 है")
            case '2': 
                print("रिचार्ज सेवा चुनी गई है")
            case '3': 
                print("कस्टमर केयर से जोड़ा जा रहा है")
            case _:
                print("गलत विकल्प")
    case '3': 
        print("You have selected Gujarati")
        print("બેલેન્સ જાણવા માટે 1 દબાવો")
        print("રીચાર્જ માટે 2 દબાવો")
        print("કસ્ટમર કેર માટે 3 દબાવો")
        submenu = input("તમારો વિકલ્પ દાખલ કરો: ")
        match submenu:
            case '1':
                print("તમારું બેલેન્સ ₹100 છે")
            case '2':
                print("રીચાર્જ સેવા પસંદ કરી")
            case '3':
                print("કસ્ટમર કેર સાથે જોડાઈ રહ્યા છે")
            case _:
                print("અમાન્ય વિકલ્પ")
    case _:
        print("Invalid language entry")
            
        
 

