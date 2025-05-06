#!/usr/bin/env python3
number = int(input("enter a number less than 25: "))
if number >= 25:
    print("error")
else:
    while number <= 25:
        print("inside the loop, my variable is",number)
        number += 1