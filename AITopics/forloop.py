#range(0, stop, 1)  stop value = upto that value but not include that value 
for i in range(10):
    print(i)

for word in range(30,40):  # i, f , n, word, sample, str, dgt
    print(word)

score = 10
print("passed") if score >= 35 else print("Failed")

even = [n for n in range(20) if n % 2 == 0]
odd = [n for n in range(20) if n % 2 != 0]
print(even)
print(odd)
