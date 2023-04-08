def binarySearch(arr, start, end, value):
    if(end < start):
        return -1
    mid = int(start + (end - start)/2)
    
    if(value == arr[mid]):
        return mid
    elif(value < arr[mid]):
        end = mid-1
        return binarySearch(arr, start, end, value)
    else:
        start = mid + 1
        return binarySearch(arr, start, end, value)


if __name__ == "__main__":
    list_input = input("Array items: ")
    value = int(input("Item to search: "))

    arr = []

    for x in list_input.split(" "):
        arr.append(int(x))

    start = 0
    end = len(arr)-1

    index = binarySearch(arr, start, end, value)
    
    if(index == -1):
        print("Not found")
    else:
        print("Found at index: ", index)    