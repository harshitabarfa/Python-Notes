# Arithmetic operators :
a = 2
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# Comparison operators :

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

# Assignment operators :

x = 5
x += 3
x -= 2
x *= 2
x /= 2
x %= 2
x **= 2
print(x)

# Logical operators :

print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))

# Bitwise operators :

print(a&b)
print(a|b)
print(a^b)
print(a>>b)
print(a<<b)

# Membership operators :

y = ["apple", "banana"]
print("banana" in y)
print("pineapple" not in y)

# Identity operators :

e = ["apple", "banana"]
f = ["apple", "banana"]
g = e

print(e is g)
# Returns True because g is the same object as e

print(e is f)
# Returns False because e is not the same object as f, even if they have the same content