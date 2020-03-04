#if statement to check numbers
y = int(input ("What is your first selection?  : "))
x = int(input ("What is your second selection? : "))

z = 0

if y > x:
   z = y * x
elif y < x:
   z = x - y
else:
   z = y + x
print(z)