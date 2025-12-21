from typing import List

class Solution:
    def merge(self, nums: List[int], l: int, mid: int, r: int):
        # Create temp arrays
        left = nums[l:mid+1]
        right = nums[mid+1:r+1]

        i = j = 0
        k = l

        # Merge two sorted halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements from left (if any)
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements from right (if any)
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, nums: List[int], l: int, r: int):
        if l >= r:
            return

        mid = (l + r) // 2

        # Recursive calls for left and right halves
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)

        # Merge sorted halves
        self.merge(nums, l, mid, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums


sol = Solution()
arr = [5, 2, 3, 1]
sorted_arr = sol.sortArray(arr)
print("Sorted:", sorted_arr)

