a = 10
print(type(a))  
b = 2.5
print(type(b))
c = 3j
print(type(c))
d = "Hello"
print(type(d))

# ctrl + / to comment multiple lines of code
l1 = [1,2,3,4,5]
print(type(l1))
# l2 = [1, "Hello", 3.5, [1,2,3], (1,2,3), {"name": "John", "age": 30}, True]
# print(type(l2))

# list -- add, remove, modify,reverse, sort 
# list - append, insert, extend, remove, pop, clear, reverse, sort
#list - mutable, ordered, allows duplicate values, can contain different data types
l2 = [10,20,30,40,50]    # index value 0,1,2,3,4  index value -5,-4,-3,-2,-1
l2.append(60)
print(l2)
print(l2[0])
print(l2[0:3])  # upto 3 --- 0,1,2
l2.insert(2, 25)  # insert value 25 at index 2  l2.insert(index, value)
print(l2)
l2.extend([70,80,90])  # extend the list with another list
print(l2)
l2.extend(l1)
print(l2)
l2.remove(30)  # remove the first occurrence of the value 30
print(l2)
l2.pop()  # remove the last element of the list
print(l2)
l2.reverse()  # reverse the list
print(l2)   
l2.sort()  # sort the list in ascending order
print(l2)
l2.sort(reverse=True)  # sort the list in descending order
print(l2)
print(l2[0])

#tuples - immutable, ordered, allows duplicate values, can contain different data types
#tuples - we cannot add, modify , delete ( immutable)
t1 = (1,2,3,4,5)  
userinfo = ("admin", "root", "superuser")  # index value 0,1,2,3  index value -4,-3,-2,-1
print(type(t1))
print(t1)
print(userinfo[0])