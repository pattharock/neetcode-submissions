from typing import List
from copy import deepcopy


def remove_element(arr: List[int], element: int) -> List[int]:
    arr_copy = deepcopy(arr)
    push_back_by = 0

    for i in range(len(arr_copy)):
        if arr_copy[i] == element:
            push_back_by += 1
        else:
            arr_copy[i-push_back_by] = arr_copy[i]
    
    for _ in range(push_back_by):
        arr_copy.pop()
    
    return arr_copy



# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
