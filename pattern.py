# Program that prints the patterns without using any nested loop.
# User will have to define object and height of pattern.
# _____PLEASE RUN THIS PROGRAM BEFORE READING FURTHER._____
# You can also add any other variable and pattern to your design.

# ------CODE STARTS------ #
user_char = input("Please input any character from which you want to make pattern : ")
user_char2 = input("Please input any other character from which you want to make pattern : ")
# user_char3 = input("Please input any other character from which you want to make pattern : ")
# ***** Please remove '#' before user_char3 to get different result.
#  ---other variable goes here---
height = int(input("Please input total height of pattern in number : "))
pattern = ""
pattern2 = ""
# pattern3 = ""
# Please remove '#' if you have removed it from user_char3.
x = 1
while x != height + 1:
    pattern += user_char
    pattern2 += user_char2
    # pattern3 += user_char3
    # ++++**IMPORTANT***++++ Please remove '#' before pattern3 if you already removed it from user_char3.

    # If you have added other variable , then please add to this block.
    """ 
    ex-->> If you have added user_char4 and pattern4
    then add here like "pattern4 += user_char4" and also pass pattern4 to print function.    
    """
    print(pattern, pattern2)
    # ~~~~~IMPORTANT~~~~~
    # If you had removed '#' from user_char3 and pattern3 then please also remove it from following line.
    # print(pattern, pattern2, pattern3)
    """
    You can modify EOL to see different patterns and styles.
    Example--->> print(pattern, pattern2, end="")
    You can write any thing in EOL like you can add tab or spaces and many more.
    """
    x += 1
