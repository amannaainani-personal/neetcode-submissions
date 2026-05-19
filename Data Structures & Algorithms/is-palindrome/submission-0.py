class Solution:
    def isPalindrome(self, s: str) -> bool:
        copiedS = ''.join(char for char in s if char.isalnum())
        reversedS = copiedS[::-1]
        if reversedS.lower() == copiedS.lower():
            return True
        return False
        