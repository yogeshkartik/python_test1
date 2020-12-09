# Program which will print any string in both original order and reverse order.

str1 = input("Please enter any text : ")
strl = (len(str1))
i = 0
print(str1, "will be written in both ordered and reverse form.")
for a in range(-1, (-strl - 1), -1):
    print(str1[i], "\t", str1[a])
    i += 1
