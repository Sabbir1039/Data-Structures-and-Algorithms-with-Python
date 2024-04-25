# Find the missing number in an array of integers.

from functools import reduce

def findMissingNumber(arr):
    if arr is None:
        return
    exp_sum = 0
    
    for i in range(len(arr)+1):
        exp_sum = exp_sum + i
        
    curr_sum = reduce(lambda x, y: x + y, arr)
    
    return exp_sum-curr_sum
    

if __name__  == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    result = findMissingNumber(arr)
    
    print(result)
    