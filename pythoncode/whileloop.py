# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == 5:
#         print("We have met the condition and exiting the loop")
#         break

# while True:
#     cmd = input("Enter your value or type exit to come out: ")
#     if cmd =='exit':
#         break

# login_attemp = 0
# while login_attemp < 3:
#      if login():
#         break
#      login_attemp += 1
import getpass

Secret_pass = "Kumar$123"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    login_user = getpass.getpass(f"Enter password ({max_attempts - attempts} tries left):") 
    if login_user == Secret_pass:
        print("Successfully loged into your account")
        break
    else:
        attempts += 1
        print("Incorrect password entered")
if attempts == max_attempts:
    print("Account Locked ,Please contact your administrator")
    
