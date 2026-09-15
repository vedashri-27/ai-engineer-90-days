numbers = [1, 5, 8, 10, 12]
target = 13

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])