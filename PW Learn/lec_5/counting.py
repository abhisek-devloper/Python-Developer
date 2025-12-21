from typing import List

class Solution:
    def countingSort(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        max_val = max(nums)
        min_val = min(nums)
        range_val = max_val - min_val + 1

        # Initialize count array
        count = [0] * range_val

        # Store the count of each element
        for num in nums:
            count[num - min_val] += 1

        # Build the sorted array
        index = 0
        for i in range(range_val):
            while count[i] > 0:
                nums[index] = i + min_val
                index += 1
                count[i] -= 1

        return nums


sol = Solution()
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = sol.countingSort(arr)
print("Sorted:", sorted_arr)

