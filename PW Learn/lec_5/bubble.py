def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Optimization: Track if a swap happened
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break  # List is already sorted

# Example
arr2 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr2)
print("Bubble Sort:", arr2)

