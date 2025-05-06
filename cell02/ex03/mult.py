#!/usr/bin/env python3
first_number = int(input("enter the first number"))
second_number = int(input("enter the second number"))
result = first_number * second_number
print((first_number), "x" ,(second_number), "=" ,(result))
if result > 0:
    print("the result is positive")
elif result < 0:
    print("the result is negative")
else:
    print("the result is zero")