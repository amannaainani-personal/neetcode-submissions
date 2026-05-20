class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums) #sort the array to use two-pointer technique and handle duplicates
        # count = collections.Counter(sorted_nums)
        result = []

        for i in range(len(sorted_nums)): 
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left = i + 1
            right = len(sorted_nums) - 1
            target = -sorted_nums[i]

            while left < right:
                current_sum = sorted_nums[left] + sorted_nums[right]
                if current_sum < target: 
                    left = left + 1
                elif current_sum > target: 
                    right = right - 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    unique = set(tuple(x) for x in result) 
                    result = [list(x) for x in unique]
                    left += 1
                    right -= 1

        return result

        