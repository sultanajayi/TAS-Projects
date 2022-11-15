# Python program to check
# if a string is palindrome
# or not

x = "radar"

w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")
