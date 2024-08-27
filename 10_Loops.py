# For loop : Used to iterate through a sequence like list, tuple, or string.

a = [1,2,3]
for item in a:
    print(item)

    if(item == 2):
        print("Something special!")

for k in range(5):
    print(k+1)

for k in range(1, 201):
    print(k)

for k in range(1, 12, 3):
    print(k)

# While loop : We can execute a set of statements asa long as a condition is true.

i = 1
while (i < 6):
    print(i)
    i+=1
