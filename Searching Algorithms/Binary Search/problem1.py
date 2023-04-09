# Problem 1: Find first and last occurance of a number with binary search algorithm.

def binarySearch_firstOccurance(arr, size, num):
    start = 0
    end = size-1
    result = -1

    while(start <= end):
        mid = int(start + (end - start)/2)
        if(num == arr[mid]):
            result = mid
            end = mid - 1
        elif(num < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return result

def binarySearch_lastOccurance(arr, size, num):
    start = 0
    end = size-1
    result = -1

    while(start <= end):
        mid = int(start + (end - start)/2)
        if(num == arr[mid]):
            result = mid
            start = mid + 1
        elif(num < arr[mid]):
            end = mid - 1
        else: 
            start = mid + 1
    return result

# Finding first_occurance and last_occurance in a single function
def find_first_last_occurance(arr, size, num, boolean):
    start = 0
    end = size - 1
    result = -1

    while(start <= end):
        mid = int(start + (end - start)/2)
        if(num == arr[mid]):
            result = mid
            if(boolean):
                end = mid - 1
            else:
                start = mid + 1
        elif(num < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return result


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 8, 8, 10, 12]
    arr_size = len(arr)
    num = 8

    # finding first occurance of a number
    # first_occurance = binarySearch_firstOccurance(arr, arr_size, num)
    # print(f"First occurance of number {num}  = {first_occurance}")

    # finding last occurance of a number
    # last_occurance = binarySearch_lastOccurance(arr, arr_size, num)
    # print(f"Last occurance of number {num}  = {last_occurance}")

    
    #  finding first occurance of a number with 3rd function
    first_occurance = find_first_last_occurance(arr, arr_size, num, 1)
    print(f"First occurance of number {num}  = {first_occurance}")

    # finding last occurance of a number with 3rd function
    last_occurance = find_first_last_occurance(arr, arr_size, num, 0)
    print(f"Last occurance of number {num}  = {last_occurance}")