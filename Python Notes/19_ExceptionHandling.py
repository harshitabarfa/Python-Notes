# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid input!")


# The try block lets you test a block of code for errors. 
try:
    num = int(input("Enter an integer: "))
    a = [6,3]
    print(a[num])
# The except block lets you handle the error.
except ValueError:
    print("Numbere entered is not an integer.")
except IndexError:
    print("Index error!")
