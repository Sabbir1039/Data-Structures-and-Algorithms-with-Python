# Hash map collision handling with chaining method

class Hashmap:
    def __init__(self) -> None:
        self.max_size = 10
        self.arr = [[] for _ in range(self.max_size)]
        
    def hash_key(self, key) -> int:
        sum = 0
        for ch in key:
            sum += ord(ch)
        return sum % self.max_size
    
    def __setitem__(self, key, value):
        index = self.hash_key(key)
        found = False
        
        for idx, item in enumerate(self.arr[index]):
            if len(item) == 2 and item[0] == key:
                self.arr[index][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[index].append((key, value))
            
    def __getitem__(self, key):
        index = self.hash_key(key)
        for item in self.arr[index]:
            if item[0] == key:
                return item[1]
            
    def __delitem__(self, key):
        index = self.hash_key(key)
        
        for idx, item in enumerate(self.arr[index]):
            if item[0] == key:
                del self.arr[index][idx]


if __name__ == "__main__":
    map = Hashmap()
    map['march 6'] = 27
    map['march 6'] = 29
    map['march 17'] = 28
    
    print(map.arr)
    
    