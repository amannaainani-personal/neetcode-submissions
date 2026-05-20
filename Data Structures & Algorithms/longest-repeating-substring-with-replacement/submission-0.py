class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        tracker = defaultdict(int)
        max_freq = 0
        answer = 0

        for i in range(len(s)):
            tracker[s[i]] += 1
            max_freq = max(max_freq, tracker[s[i]])

            while(i - left + 1) - max_freq > k:
                tracker[s[left]] -= 1
                left += 1
            
            answer = max(answer, i - left + 1)
        
        return answer
        