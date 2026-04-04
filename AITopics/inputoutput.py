# name = str(input("What is your name? "))
a = 10 # global variable 
# age = int(input("What is your age? "))

# print("your name is " + name + " and you are age is " + str(age) )
# print(f"your name is {name} and you are age is {age} ")     # print statement with f string
# print("your name is {} and you are age is {}".format(name, age))
# print("your name is %s and you are age is %d" % (name, age))   

# name1, age1 = map(str, input("Enter your name and age separated by space: ").split())
# print(f"your name is {name1} and you age is {age1} ")
# a,b,c = map(int, input("Enter three numbers separated by space: ").split())
# print(f"the three numbers are {a}, {b} and {c}")

# "Enter your name and age separated by space: John 30" # string input 

# data = eval(input("Enter your data:"))
# print(type(data))
# print(data)
# print("sam", "john", "michael", sep="-")  # sep is used to separate the values with a specific character
# print("Hello",end="!")  # end is used to specify what to print at the end of the statement, by default it is a newline character
# print("Hello word", file=open("output.txt", "w"))  # file is used to specify the file to which the output should be written, by default it is sys.stdout


#variables : Local variables, Global Variables
# Local variable is a variable that is defined inside a function and can only be accessed within that function.
# Global variable is a variable that is defined outside of any function and can be accessed from anywhere in the code.
print(a)

def func1():
    print(a)
    b = 20  # local variable
    print(b)


func1()

print(a)
print("variable used outside of function:",b)