# a = [i for i in range(101)]

a = 12

if a % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")


even = []

for i in range(101):
    if i % 2 == 0:
        even.append(i)

print(even)


even_1 = [i for i in range(101) if i%2 == 0]
print(even_1)





