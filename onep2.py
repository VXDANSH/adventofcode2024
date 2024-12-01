arr1 = []
arr2 = []

finalsum = 0;

finalans = 0

with open("oneinput") as file:
    letters = file.read().splitlines()

for line in letters:
    arr1.append(int(line.split()[0]))
    arr2.append(int(line.split()[1]))

arr1.sort()
arr2.sort()

for num in arr1:
    counter = 0;
    for i in range(0, len(arr2)):
        if arr2[i] == num:
            counter += 1
    finalsum += num*counter

print(finalsum)