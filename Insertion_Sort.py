# Create an array of 10 numbers
arr = [12, 6, 50, 35, 26, 44, 1, 39, 16, 44]
n = len(arr)

# Do the insertion sorting
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] < key:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key


# Verify the output 
for x in arr:
    print(x)