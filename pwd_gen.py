import random

print("\n##################################")
print("#       Password Generator       #")
print("##################################\n")

# ( Letters + Digits + Symbols ) 
digits              ="123456789"
symbols             ="!@#$%^&*()_+-=[{]}|\:;<,>.?/`~"
uppercase_letters   ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters   =uppercase_letters.lower()

# Switches
upper,lower,nums,syms = True , True , True , True

# Password
collector=""

# User input (Length + Amount )
length              =int(input("Give the password length : "))
amount              =int(input("Give the amount of generated passwords : "))
# Switches Manager
upper_request       =int(input("\nDo you want uppercase letters to your password ? ( Press 0 for No , 1 for Yes ) "))
lower_request       =int(input("Do you want lowercase letters to your password ? ( Press 0 for No , 1 for Yes ) "))
digits_request      =int(input("Do you want digits  to your password ? ( Press 0 for No , 1 for Yes ) "))
symbols_request     =int(input("Do you want symbols  to your password ? ( Press 0 for No , 1 for Yes ) "))
print("\n")

# Switches Checker
if upper_request==1:
    collector+=uppercase_letters
if lower_request:
    collector+=lowercase_letters
if digits_request:
    collector+=digits
if symbols_request:
    collector+=symbols

# Print generated passwords
counter=1
for x in range(amount):
    gen_pass="".join(random.sample(collector,length))
    print(str(counter)+". "+gen_pass)
    counter+=1

input("\nPress any key to exit...")