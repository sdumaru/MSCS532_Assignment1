# Create an array of 10 numbers
arr = [12, 6, 50, 35, 26, 44, 1, 39, 16, 44]
n = len(arr)                                        # total number of elements in an array

# Do the insertion sorting
for i in range(1, n):
    key = arr[i]                                    # key element that will be used to compare with the elements before it in that array
    j = i - 1                                       # index before the key element for easier comparison
    while j >= 0 and arr[j] < key:                  # keeps the loop running until the elements in the array before key element runs out 
                                                    # and until an element is found which is in bigger value than key element
        arr[j+1] = arr[j]                           # move the element one position right if it is smaller in value than the key element
        j = j - 1                                   # reduce the index to keep comparing the value until it reached the first element in array
    arr[j+1] = key                                  # once a bigger value element than the key element is found, the while loop breaks and
                                                    # the key element is put right after that element making it in decreasing order


# Verify the output 
for element in arr:
    print(element)