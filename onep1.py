arr1 = []
arr2 = []

nums = []

finalsum = 0;

finalans = 0

with open("oneinput") as file:
    letters = file.read().splitlines()

for line in letters:
    arr1.append(int(line.split()[0]))
    arr2.append(int(line.split()[1]))

arr1.sort()
arr2.sort()

for j in range(0, len(arr1)):
    finalsum += abs(arr1[j]-arr2[j])

print(finalsum)