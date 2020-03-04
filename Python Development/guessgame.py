import random

n = random.randrange(1,101)

print("I'm between 1 and 100, Can you find me?")

while True:
    try:
         g = int(input('Guess!, Enter the Number: '))
         g = int(g)
         if not 100 > g > 0:
             print("It's in between 0 and 100!")
    except ValueError:
         print("Enter an Integer")
    if g == n:
        print ("Congratulations!")
        break
    if g < n:
     print("You getting Closer")
    
    if g > n:
     print("Comeback! - You getting there")