class Solution:
    def prefixOfTwo(self, s: str, t:str) -> int:
        if len(s) > len(t):
            s, t = t, s
    
        i = 0

        while (i < min(len(s), len(t))):
            if s[i] == t[i]:
                i += 1
            else:
                break
        return i

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            prefix_bound = self.prefixOfTwo(prefix, strs[i])
            prefix = prefix[:prefix_bound]
        
        return prefix
            
