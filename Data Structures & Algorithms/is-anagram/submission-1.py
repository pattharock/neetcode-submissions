class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = [0] * 26

        for c in s:
            count_map[ord(c) - ord('a')] += 1
        
        for c in t:
            count_map[ord(c) - ord('a')] -= 1
        
        for num in count_map:
            if num != 0:
                return False
        return True
            