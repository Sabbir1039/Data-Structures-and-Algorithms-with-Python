def linearSearch(arr, item):
    for idx,x in enumerate(arr):
        if item == x:
            return idx

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    item = 8
    index = linearSearch(arr, item)
    print(index)