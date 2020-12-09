""" Program to print elements of list [q,w,e,r,t,y] in separate lines along with element's
bot indexes (positive and negative)."""

inlist1 = (input("Please enter a string : "))
list1 = list(inlist1)
print(inlist1, 'will be printed in both indexes.')
l_lnght = (len(inlist1))
for a in range(l_lnght):
    print("At index : ", a, "and", (a - l_lnght), "is : ", inlist1[a])
