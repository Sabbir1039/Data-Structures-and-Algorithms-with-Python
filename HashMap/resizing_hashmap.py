class Hashmap:
    def __init__(self, initial_capacity, threshold = .75) -> None:
        self.capacity = initial_capacity
        self.threshold = threshold
        self.size = 0
        self.map = [None for _ in range(self.capacity)]
        
    def hash_function(self, key) -> int:
        total = 0
        for char in key:
            total += ord(char)
        return total % self.capacity
    
    def resize(self, new_capacity):
        old_map = self.map
        self.capacity = new_capacity
        self.map = [None for _ in range(self.capacity)]
        self.size = 0
        
        for entry in old_map:
            if entry is not None:
                self[entry[0]] = entry[1] # like hash[entry[0]] = entry[1]
        
    def __setitem__(self, key, value):
        if (self.size + 1)/self.capacity > self.threshold:
            self.resize(2 * self.capacity)
            
        index = self.hash_function(key)
        
        while self.map[index] is not None:
            if self.map[index][0] == key:
                self.map[index] = (key, value)
                break
            index = (index+1) % self.capacity
            
        if self.map[index] == None:
            self.map[index] = (key, value)
            self.size += 1
    
    def __getitem__(self, key):
        index = self.hash_function(key)
        while self.map[index] is not None:
            if self.map[index][0] == key:
                return self.map[index][1]
            index = (index+1) % self.capacity
        raise KeyError(key)
    
    def __delitem__(self, key):
        index = self.hash_function(key)
        while self.map[index] is not None:
            if self.map[index][0] == key:
                self.map[index] = None
                return
            index = (index+1) % self.capacity
        raise KeyError(key)
    
if __name__ == '__main__':
    hash = Hashmap(10)
    
    hash['march 1'] = 50
    hash['march 5'] = 100
    hash['march 6'] = 150
    hash['march 7'] = 250
    hash['march 17'] = 350
    hash['march 17'] = 450
    
    print(f'first : {hash.map}')
    print(f'first capacity: {hash.capacity}')
    
    hash['march 18'] = 550
    hash['march 19'] = 650
    hash['march 20'] = 700
    hash['march 21'] = 800
    hash['march 22'] = 900
    
    print(f'second : {hash.map}')
    print(f'second capacity: {hash.capacity}')
    