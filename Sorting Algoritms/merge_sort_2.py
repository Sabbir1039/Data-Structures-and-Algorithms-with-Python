# not in-place merge sort
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    return merge(left_arr, right_arr)

def merge(left_arr: List[int], right_arr: List[int]) -> List[int]:
    result = []
    i = j = 0
    
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j+=1
    result.extend(left_arr[i:])
    result.extend(right_arr[j:])
    
    return result

if __name__ == "__main__":
    arr = [2, 4, 1, 6, 8, 5, 3, -1, -1]
    sorted_list = merge_sort(arr)
    print(sorted_list)