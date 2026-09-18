class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()

        left, right = 0, len(A) - 1

        while left < right:
            s = A[left][0] + A[right][0]

            if s < target:
                left+=1
            elif s > target:
                right-=1
            else:
                return [min(A[left][1], A[right][1]),
                        max(A[left][1], A[right][1])]
        return []




            
