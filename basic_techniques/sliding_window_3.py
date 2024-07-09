from collections import Counter

def missingNumbers(arr, brr):
    arr_freq = Counter(arr)
    brr_freq = Counter(brr)
    
    return sorted(list((brr_freq-arr_freq).keys()))

# Example usage
if __name__ == "__main__":
    arr = [203, 204, 205, 206, 207, 208]
    brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 204, 205, 206]
    result = missingNumbers(arr, brr)
    print(result)  # Expected output: [204, 205, 206]
