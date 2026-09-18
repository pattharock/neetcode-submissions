class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = {}

        for c in s:
            if c in count_map:
                count_map[c] += 1
            else:
                count_map[c] = 1
        
        for c in t:
            if c not in count_map:
                return False
            count_map[c] -= 1
        
        for _, value in count_map.items():
            if value != 0:
                return False
        
        return True
            