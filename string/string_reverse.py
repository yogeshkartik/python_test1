# Program to read a string and display it in reverse order - display one character per line.
# Do not create a reverse string, just display in reverse order.

text = input("Please enter text : ")
print("The reverse order of ", text, "is :")
size = len(text)
for a in range(-1, (-size - 1), -1):
    print(text[a])
