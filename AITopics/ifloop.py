a = 10
b = 20
c = 30

if a > b :
    print("a is greater than b")
elif b > c :
    print("b is greater than c")
else:
    print("c is greater than a and b")



if a > b :
    print("a is greater than b")
else:
    print("b is greater than a")

d = 40  
if d > 0:
    print("d is positive number")

uname = "admin"

if uname:  #  if the string is not empty it will return True and if it is empty it will return False
    print("username is not empty") 

if uname == "admin" or uname == "superuser":
    print("welcome admin")

number = 30
if number % 2 == 0 and number > 0:
    print("number is even and positive")

for i in range(1,20):
    if i % 2 == 0 and i % 5 == 0:
        print(f"{i} is divisible by 2 and 5")

name ="john"
for letter in name:
    if letter in "aeiou":
        print(f"{letter} is a vowel")
        print(letter.upper())
    else:
        print(f"{letter} is a consonant")

l1 = [1,2,3,4,5,6,7,8,9,10]
for num in l1:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


# upper, lower, startswith, endswith, split, strip

user_name = " john "
if user_name.strip()== "john":
    print("user logged in is john")

filename = [ "data.csv", "image.png", "loops.txt"]

for i in filename:
    if i.endswith(".txt"):
        print(f"found the text file {i}")

word = "PYTHON"
if word.isupper():
    print("word is in capital letter")

phone_number = "555-343-4240"
clean_phone_number = phone_number.replace("-","")

if phone_number.replace("-","").isdigit():
    print(f"The phone number is {phone_number}")

if not clean_phone_number.startswith("0") and clean_phone_number.isdigit() and len(clean_phone_number) == 10:
    print("This is a valid US phone number",clean_phone_number)



if  clean_phone_number.isdigit() and len(clean_phone_number) == 10:
    if not clean_phone_number.startswith("0"):
        print("This is a valid US phone number",clean_phone_number)


