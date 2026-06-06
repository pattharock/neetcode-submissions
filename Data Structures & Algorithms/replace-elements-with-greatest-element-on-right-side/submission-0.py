class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_to_right = -1

        for i in range(len(arr) - 1, -1, -1):
            cached_val = arr[i]
            arr[i] = greatest_to_right
            greatest_to_right = max(greatest_to_right, cached_val)

        return arr