# Program to accept three integer and print the largest of the three.
max = x = y = z = 0
x = int(input('Please enter first number : '))
y = int(input('Please enter second number : '))
z = int(input('Please enter third number : '))
if x > z:
    if x > y:
        max = x
if y > z:
    if y > x:
        max = y
if z > x:
    if z > y:
        max = z
print("The largest number is : ", max)
