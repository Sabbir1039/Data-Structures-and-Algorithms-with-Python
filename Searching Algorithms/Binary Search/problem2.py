# Problem 2: Find count of a number in a sorted list

def findOccurance(arr, size, num, boolean):
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

def findCount(arr, size, num):
    first = findOccurance(arr, size, num, 1)
    print("first = ", first) 
    last = findOccurance(arr, size, num, 0)
    print("last = ", last) 
    count = last-first + 1
    return count

if __name__ == '__main__':

    arr = [1, 3, 5, 7, 7, 7, 7, 7, 7, 9]
    size = len(arr)
    num = 7

    count = findCount(arr, size, num)
    print(count)