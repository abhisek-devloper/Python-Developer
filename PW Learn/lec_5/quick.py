from typing import List

class Solution:
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]  # Choose the last element as pivot
        i = low - 1         # Index of smaller element

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]  # Swap

        # Place pivot at correct position
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quickSort(self, nums: List[int], low: int, high: int):
        if low < high:
            # Partitioning index
            pi = self.partition(nums, low, high)

            # Recursively sort elements before and after partition
            self.quickSort(nums, low, pi - 1)
            self.quickSort(nums, pi + 1, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums


sol = Solution()
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = sol.sortArray(arr)
print("Sorted:", sorted_arr)

