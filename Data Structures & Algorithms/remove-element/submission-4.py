class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums or (len(nums) == 1 and nums[0] == val):
            return 0
        
        end = len(nums) - 1

        while (end >= 0 and nums[end] == val):
            end -= 1
        
        i = 0

        while (i <= end):
            if (nums[i] == val):
                # swap then decrement end to next non-val
                nums[i], nums[end] = nums[end], nums[i]
                while(end >= 0 and nums[end] == val):
                    end -= 1
            else:
                i += 1
        return i