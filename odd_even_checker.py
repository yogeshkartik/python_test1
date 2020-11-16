# To find  whether number is odd or even.
# Code starts...

print("#" * 50)
print("ODD EVEN NUMBER CHECKER")
print('-' * 50)
usernum = int(input('Please enter a number : '))
if usernum % 2 == 0:
    print(usernum, "is even number.")
else:
    print(usernum, "is odd number.")
userconfirm = input('Do you want to check for another number (y/n)... ')
while userconfirm == 'y':
    usernum = int(input('Please enter a number : '))
    if usernum % 2 == 0:
        print(usernum, "is even number.")
        userconfirm = input('Do you want to check for another number (y/n)... ')
    else:
        print(usernum, "is odd number.")
        userconfirm = input('Do you want to check for another number (y/n)... ')
print('-' * 50)
print('Program over !')
print('#' * 50)
