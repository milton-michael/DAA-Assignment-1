def insertion_sort(arr):
    # Iterate from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Shift elements of the sorted segment that are greater than the key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key

# Sample Input and Output
my_array = [12, 11, 13, 5, 6]
print("Input Array :", my_array)

insertion_sort(my_array)
print("Sorted Array:", my_array)
