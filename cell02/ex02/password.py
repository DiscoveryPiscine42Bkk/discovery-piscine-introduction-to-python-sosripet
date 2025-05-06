#!/usr/bin/env python3

correct_password = "Python is awesome"
entered_password = input("Please enter your password: ")
if entered_password == correct_password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
