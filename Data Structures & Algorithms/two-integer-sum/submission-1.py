class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in complements and i != complements[to_find]:
                return [complements[to_find], i]
            
            complements[num] = i
        return []


            
