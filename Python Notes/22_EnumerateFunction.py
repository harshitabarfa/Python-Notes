marks = [12, 34, 56, 78, 90, 4, 8]

index = 0
for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("End")
    # index += 1