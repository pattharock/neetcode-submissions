class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_ones = 0
        max_consecutive_ones = 0
        for num in nums:
            if num == 1:
                num_ones += 1
            else:
                num_ones = 0
            max_consecutive_ones = max(max_consecutive_ones, num_ones)
        
        return max_consecutive_ones