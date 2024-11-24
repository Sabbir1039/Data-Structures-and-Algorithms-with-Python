# leetcode problem 128: longest consecutive subsequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# brute force O(n*n*n)
def solution_one(arr):
    longest_len = 0
    
    for num in arr:
        curr_len = 1
        next_num = num + 1
        
        k = 0
        
        while (k < len(arr)):
            for i in arr:
                if i == next_num:
                    curr_len += 1
                    next_num += 1
            k += 1
        longest_len = max(longest_len, curr_len)
    
    return longest_len

# using sort O(n log n)
def solution_two(arr):
    arr.sort()
    n = len(arr)
    longest_len = 0
    
    i = 0
    while i < n:
        curr_len = 1
        next_num = arr[i] + 1
        
        j = i+1
        while j < n:
            while j < n and arr[j] == arr[j-1]: # handling duplicates edge case
                j += 1
            if arr[j] == next_num:
                curr_len += 1
                next_num += 1
                j += 1
            else:
                break
        i = j
        longest_len = max(longest_len, curr_len)
    return longest_len

# optimized solution O(n) using hashmap
def solution_three(arr):
    longest_len = 0
    mymap = {x: False for x in arr};
    
    for num in arr:
        curr_len = 1
        
        next_num = num + 1
        while (next_num in mymap) and (mymap[next_num] == False):
            curr_len += 1
            mymap[next_num] = True
            next_num += 1
        
        prev_num = num - 1
        while (prev_num in mymap) and (mymap[prev_num] == False):
            curr_len += 1
            mymap[prev_num] = True
            prev_num -= 1
    
        longest_len = max(longest_len, curr_len)
    return longest_len

if __name__ == "__main__":
    arr = [0, 3, 7, 2, 5, 8, 4, 6, 1, 9, -1, -2, 11, 13, 0, 1]
    # arr = [1, 2, 3]
    
    result1 = solution_one(arr)
    print(result1)
    
    result2 = solution_two(arr)
    print(result2)
    
    result3 = solution_three(arr)
    print(result3)