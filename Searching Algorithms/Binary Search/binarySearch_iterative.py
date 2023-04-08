def binarySearch(arr, size, value):
    start = 0
    end = size-1
    
    while(start <= end):
        mid = int((start + end)/2)
        if(value == arr[mid]):
            return mid
        elif(value < arr[mid]):
            end = mid-1
        else:
            start = mid + 1
    return -1

if __name__ == "__main__":
    list_input = input("Array items: ")
    value = int(input("Item to search: "))
    arr = []
    for x in list_input.split(" "):
        arr.append(int(x))
    index = binarySearch(arr, len(arr), value)
    if(index == -1):
        print("Not found")
    else:
        print("Found at index: ", index)