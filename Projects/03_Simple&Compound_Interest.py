p = float(input("Enter the principal amount: "))

r = float(input("Enter the interest rate: "))

t = int(input("Enter the number of time: "))

# Simple interest
simple_interest = p*r*t/100

# Compound interest
compound_interest = p * (1 + (r/100)) ** t - p

print("Compound Interest: ", compound_interest)
print("simple_interest", simple_interest)