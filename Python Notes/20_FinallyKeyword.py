try:
    l = [1, 2, 5, 7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred!")

# The finally block lets you execute code, regardless of the result of the try and except blocks.
finally:
    print("I am always excecuted!")