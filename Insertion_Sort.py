""" Monotically Decreasing Insertion Sort """

def insertion_sort(array):
    """ Function that will take array as an input and return sorted array. """
    arr_size = len(array)

    for i in range(1, arr_size):
        key = array[i]                      # key element that will be used to compare with the elements before it in that array
        j = i - 1                           # index before the key element for easier comparison
        while j >= 0 and array[j] < key:    # keeps the loop running until the elements in the array before key element runs out 
                                            # and until an element is found which is in bigger value than key element
            array[j+1] = array[j]           # move the element one position right if it is smaller in value than the key element
            j = j - 1                       # reduce the index to keep comparing the value until it reached the first element in array
        array[j+1] = key                    # once a bigger value element than the key element is found, the while loop breaks and
                                            # the key element is put right after that element making the array in decreasing order
    return array

# Empty array to store the numbers inputted by user
unsorted_list = []

# Take inputs from the user for the size of array
array_size = int(input("Enter the size of array: "))

# Take inputs from the user for the list of numbers
print("Enter the number you want in the array: ")
for index in range(array_size):
    inputted_number = input(str(index + 1) + ". ")
    unsorted_list.append(inputted_number)

print("List of numbers provided: ")
print(unsorted_list)

# Sort the list provided by user using insertion_sort function and print it
print("Sorted list: ")
print(insertion_sort(unsorted_list))
