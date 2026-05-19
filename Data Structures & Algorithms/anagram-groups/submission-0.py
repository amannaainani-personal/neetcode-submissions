class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        subGroup = defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            subGroup[key].append(str)

        return list(subGroup.values())
