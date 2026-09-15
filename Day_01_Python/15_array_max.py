numbers = [12, 5, 8, 20, 3, 15]
maximum = numbers[0]
for n in numbers:
    if n > maximum:
        maximum = n

print("The maximum number in the array is:", maximum)