class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1+count.get(n, 0)
        for n, c in count.items(): #Return key-value pairs added to the count dict
            freq[c].append(n) #at index 'count', append to that list with value 'n' (value 'n' occurs 'c' numbers of times)

        res = [] #getting the top-K element
        for i in range(len(freq) - 1, 0, -1): #-1 is the last index, go all the way up until 0, -1 is in desc order
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        