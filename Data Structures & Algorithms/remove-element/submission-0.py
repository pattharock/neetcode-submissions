class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_occurances = 0

        for i in range(len(nums)):
            if nums[i] == val:
                num_occurances+=1
            else:
                nums[i-num_occurances] = nums[i]
        
        return len(nums) - num_occurances