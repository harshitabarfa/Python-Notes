# Print numbers from 1 to 100

# Solution :-
# for number in range(1, 101):
#     print(number)




# Print numbers from 100 to 1.

# Solution :-
# for number in range(100, 0, -1):
#     print(number)



# Print the multiplication table of a number n.

# Solution :-
# n = int(input("Enter the number : "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")




# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Solution :-
# def printValues():
#  l = list()
    
#  for i in range(1, 11):
#         l.append(i**2)
#  print(l)
# printValues()




# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

# Solution:-
# numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# def search_number(x, numbers):
#     for number in numbers:
#         if number == x:
#             return True
#     return False
# x = 3
# found = search_number(x, numbers)
# if found:
#     print(f"{x} is in the tuple.")
# else:
#     print(f"{x} is not in the tuple.")




# WAP to find the sum of first n numbers. (using while)

# Solution :-
# n = 10
# total_sum = 0
# current_number = 1

# while current_number <= n:
#     total_sum += current_number
#     current_number += 1
# print(f"The sum of the first {n} numbers is {total_sum}.")




# WAP to find the factorial of first n numbers. (using for)

# Solution :-
# n = 5
# factorials = []

# for i in range(1, n + 1):
#     factorial = 1
#     for j in range(1, i + 1):
#         factorial *= j
#     factorials.append(factorial)

# for i in range(1, n + 1):
#     print(f"Factorial of {i} is {factorials[i-1]}")
