import random

upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_char = upper_char.lower()
symbols = "!@#$%^&*()[]{}:;,?/"
numbers = "0123456789"

upper, lower, syms, nums = True, True, True, True

all = ""
if upper:
    all += upper_char
if lower:
    all +=lower_char
if nums:
    all += numbers
if syms:
    all += symbols


password_length = int(input("How long would you like your password to be?: "))
password_times = int(input("How many passwords should I generate: "))
        
for x in range(password_times):
    password = "".join(random.sample(all,password_length))
    print(f"here's your password: {password} ")