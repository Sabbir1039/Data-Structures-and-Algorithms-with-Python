# problem: Maximum number of vowels in a string of size k

def count_vowels(sub_string):
    vowels = set("aeiou")
    count = 0
    for char in sub_string:
        if char in vowels:
            count += 1
    return count

# Brute force solution | time: O(nk)
def bf_max_number_of_vowels(string, k):
    max_count = 0
    
    for i in range(len(string)-k+1):
        count = count_vowels(string[i:i+k])
        # print(f"count for i[{i}] : {count}") # for debug
        max_count = max(count, max_count)
    return max_count

# optimize solution with slidding window | time: O(n)
def sw_max_numbers_of_vowels(string, k):
    vowels = set("aeiou")
    curr_count = count_vowels(string[:k])
    max_count = curr_count
    
    for i in range(len(string)-k):
        if string[i] in vowels:
            curr_count -= 1
        if string[i+k] in vowels:
            curr_count += 1
        # print(f"count for i[{i}] : {curr_count}")
        max_count = max(curr_count, max_count)
    return max_count

if __name__ == "__main__":
    string = "bacacbefaobeacfeaieou"
    k = 5
    result = bf_max_number_of_vowels(string, k)
    print(result)
    
    res = sw_max_numbers_of_vowels(string, k)
    print(res)