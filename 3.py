str1 = input("Enter first string :")
str2 = input("Enter second string :")
n1 = len(str1)
n2 = len(str2)
concat = ''
if n1 != n2:
    print("The two strings are not rotation of each other")
else:
    concat = str1+str1
    if str2 in concat:
        print("The two strings are rotation of each other")
    else:
        print("The two strings are not rotation of each other")