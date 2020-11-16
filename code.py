# This is my first python project in pycharm after long time.
"""
print("#" * 75)
print('\t\t\tHELLO WORLD')
print("#" * 75)
name = (input("Please enter your name :"))
dob = (input("Please enter your dob (dd/mm/yyyy) :"))
_class = (int(input("Please enter your class :")))
# name_print = ("name :{0:8,s}"   "dob :{1:12,s}" .format(name, dob))

# print("Hello {0:>20s}. Your dob is :{1:>55s}".format(name, dob), end="")
print("-" * 75)
print("NAME\t\t\t\t\tCLASS\t\t\t\t\tDOB")
print("{0:s}{1:>13d}{2:>30s}".format(name, _class, dob))"""
# print("-" * 75)

print("#" * 90)
print("\t\t\t\t\t\t\t\t\tSTUDENTS DATABASE")
print("-" * 90)
total_student = int(input("Please enter total number of student : "))
text = (input("please enter different name (space-separated) :"))
roll = (input("Please enter roll no. of student (space-separated) :"))
text = text.split()
roll = roll.split()
print("."*90)
print("\t\t\t\t\t\t\tNAME\t\t\t\tROLL")
print("")
for i in range(total_student):
    print("\t\t\t\t\t\t\t{0:s}{1:>20s}".format(text[i], roll[i]))
print("-" * 90)
print("\t\t\t\t\t\t\t\t\t\tTHANK YOU")
print("#" * 90, end="")
