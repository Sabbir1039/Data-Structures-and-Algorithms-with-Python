class Hashmap:
    
    def __init__(self, size) -> None:
        self.size = size
        self.item_count = 0
        self.arr = [None for _ in range(self.size)]
        
    def hash_function(self, key):
        total = 0
        for ch in str(key):
            total += ord(ch)
        return total % self.size
    
    def __setitem__(self, key, value):
        position = self.hash_function(key)
        
        while self.arr[position] is not None:
            if self.arr[position][0] == key:
                self.arr[position] = (key, value)
                return
            position = (position + 1) % self.size
        
        if self.arr[position] is None:
            self.arr[position] = (key, value)
            self.item_count += 1
    
    def __getitem__(self, key):
        position = self.hash_function(key)
        
        while self.arr[position] is not None:
            if self.arr[position][0] == key:
                return self.arr[position][1]
            position = (position + 1) % self.size
        
        raise KeyError(key)
    
    def __delitem__(self, key):
        position = self.hash_function(key)
        
        while self.arr[position] is not None:
            if self.arr[position][0] == key:
                del self.arr[position]
                return
            position = (position + 1) % self.size
    
        raise KeyError(key)
if __name__ == '__main__':
    hash = Hashmap(10)

    hash['march 1'] = 100
    hash['march 6'] = 300
    hash['march 7'] = 500
    hash['march 9'] = 700
    hash['march 17'] = 1500
    hash['march 18'] = 2500
    hash['march 19'] = 350
    hash['march 20'] = 550
    hash['march 21'] = 650
    # hash['march 22'] = 759
    
    print(hash.arr)
    
    del hash['march 17']
    
    print(hash.arr)