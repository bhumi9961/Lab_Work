#Question 2
print("square of the number")
for i in range(1,11):
    print(i*i)

#Question 4
print("odd numbers only")
for i in range(1,21,2):
    print(i)

#Question 5
print("multiple of 5")
for i in range(5,51,5):
    print(i)

#Question 6
print("reverse the count")
for i in range(10,0,-1):
    print(i)

#Question 7
for i in range(1,51):
    if(i%6==0):
        print(f"{i} is Divisible by 2 and 3 both")
    elif(i%3== 0):
        print(f"{i} is Divisible by 3")
    elif(i%2==0):
        print(f"{i} is Divsible by 2")
    else:
        print(f"{i} is not divisible by 2, 3 or both")
              
        