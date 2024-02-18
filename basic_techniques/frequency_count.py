# general approach time = O(n)
def frequency_count(items) -> dict:
    d = {}
    for item in items:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d

# Another approach
def freq_count2(item) -> dict:
    d = {}
    
    for i in item:
        d[i] = d.get(i, 0) + 1
        
    return d

# using collections module
from collections import Counter

def freq_count3(items):
    return Counter(items)
    
    
    
if __name__ == "__main__":
    
    nums = [1, 2, 1, 3, 4, 5, 3, 5]
    f_count = frequency_count(nums)
    
    # print(f_count)
    
    string = "Sabbir"
    # print(freq_count2(string))
    
    count = freq_count3(nums)
    print(count.get(1, "Not found"))