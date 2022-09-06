"""
Filename: Nesting.py
Author: Taliesin Reese
Version: 1.0
Date: 9/1/2022
Purpose: Nested if statements
"""
#imports
import lib
#presentation
lib.titlePrint("Welcome to The Nest: Club and Lounge")
print("""
       Built in the old building once
      inhabited by the Temp Converter,
      this club and lounge serves the
       very best in detecting whether
        numbers are divisible by 7
              and/or 11

            """)
#get number input
num = lib.inputFloat("Input your number, please")
#check if divisible by 11:
if num % 11 == 0:
	#check if divisble by 7:
    if num % 7 == 0:
		#win
        print(f"{num} is divisible by both 7 and 11.")
	#else:
    else:
		#lose
        print(f"{num} is not divisible by 7.")
elif num % 7 == 0:
    print(f"{num} is not divisible by 11.")
#else:
else:
	#lose
    print(f"{num} is not divisible by 11 or 7.")
print(">>END OF LINE<<")
