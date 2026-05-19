class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        unique_sorted = sorted(set(nums))
        max_len = 1
        current_len = 1
        for i in range(len(unique_sorted) - 1):
            if unique_sorted[i + 1] == unique_sorted[i] + 1:
                current_len += 1
            else:
                current_len = 1
            max_len = max(max_len, current_len)
        return max_len