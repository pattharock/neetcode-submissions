from heapq import heappush, heappop
from typing import List

def transform(x: int) -> int:
    return -x

def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []    
    for num in nums:
        heappush(max_heap, transform(num))
    l = []
    while max_heap:
        l.append(transform(heappop(max_heap)))
    return l





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
