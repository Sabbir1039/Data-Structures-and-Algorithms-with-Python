# Popular two sum problem with two pointers technique

def two_sum(nums, target) -> list:
    first = 0
    last = len(nums) - 1
    
    while first < last:
        if nums[first] + nums[last] == target:
            return [first, last]
        elif nums[first] + nums[last] < target:
            first += 1
        else:
            last -= 1
    return None

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 9
    result = two_sum(nums, target)
    print(result)