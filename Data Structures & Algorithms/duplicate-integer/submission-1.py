class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        repeats = [i for i in nums if i in seen or seen.add(i)]
        if repeats:
            return True
        return False


        