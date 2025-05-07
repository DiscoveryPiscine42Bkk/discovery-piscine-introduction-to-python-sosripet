#!/usr/bin/env python3
import sys
greet = input("please tell me your age :")
age_int = int(greet)
if age_int<0:
    print("Age must be a positive number. Please try again.")
    sys.exit()
print(f"you are currently {age_int} years old.")
i = 10
while i <= 30:
    print(f"in{i}years, you will be {age_int + i}year sold")
    i += 10    


