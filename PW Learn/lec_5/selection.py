def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find index of minimum element in the remaining list
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example
arr3 = [29, 10, 14, 37, 13]
selection_sort(arr3)
print("Selection Sort:", arr3)

