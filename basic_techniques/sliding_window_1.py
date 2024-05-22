# Problem: Find the maximum sum of a subarray of size k

# Brute force solution | time: O(nk)
def max_sum(arr, k):
    max_total = 0
    for i in range(len(arr)-k+1):
        total = sum(arr[i:i+k])
        # print(f"for i[{i}] = {total}") # for debugging
        max_total = max(total, max_total)
    return max_total

# sliding window solution | time: O(n)
def sliding_window_max_sum(arr, k):
    total = sum(arr[:k])
    max_total = total
    for i in range(len(arr)-k):
        total -= arr[i]
        total += arr[i+k]
        # print(f"for i[{i}] = {total}") # for debugging
        max_total = max(total, max_total)
    return max_total


if __name__ == "__main__":
    arr = [3, 4, 1, 5, 7, 9, 0, 1, 6, 9, 2, 0]
    k = 4
    bf_sum = max_sum(arr, k)
    print(bf_sum)
    sw_sum = sliding_window_max_sum(arr, k)
    print(sw_sum)