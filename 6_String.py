# String : String represent a sequence of character.

# Types :
# Single quoted string : 'Harshita'
# Double quoted string : "Harshita"
# Triple quoted string : '''Harshita'''

a = "Hello"
print(a)

# Indexing
print(a[0])

# String length
print(len(a))

# Slicing
print(a[2:4])

# Slice from the start
print(a[:3])

# slice from the last
print(a[2:])

# Negative indexing
print(a[-4:-1])

# Check string
print("free" in a)
print("Hello" in a)

# Loop through a string
for a in "Hello":
    print(a)

# UpperCase
print(a.upper())

# LowerCase
print(a.lower())

# Remove whitespace
b = " Harshita  "
print(b.strip())

# Replace string
print(a.replace("H","C"))

# Split string
c = "Hello, World"
print(c.split(','))

# Concatenation string
d = a+b
print(d)

# String format
name = "Harshita"
age = 19
txt = f"My name is {name}, and I am {age} year old"
print(txt)

# Placeholders and modifires
price = 59
text = f"The price is{price : .2f} dollars"
print(text)

p = f"The price is {20*59} dollars"
print(p)