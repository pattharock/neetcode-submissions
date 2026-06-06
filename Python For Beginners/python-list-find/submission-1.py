from typing import List

def find_index(nums: List[int], target: int) -> int:
    found = False

    for i, n in enumerate(nums):
        if n == target:
            return i
    
    raise ValueError


# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

