class Hashmap:
    def __init__(self, initial_capacity, threshold=0.75) -> None:
        self.capacity = initial_capacity
        self.threshold = threshold
        self.size = 0
        self.map = [[] for _ in range(self.capacity)]
        
    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total%self.capacity
    
    def resize(self, new_capacity):
        old_map = self.map
        self.capacity = new_capacity
        self.size = 0
        self.map = [[] for _ in range(self.capacity)]
        
        for entry in old_map:
            for key, value in entry:
                self.__setitem__(key, value)
                
    def __setitem__(self, key, value):
        if (self.size+1) / self.capacity > self.threshold:
            self.resize(self.capacity * 2)
        index = self.hash_function(key)
        found = False
        
        for idx, item in enumerate(self.map[index]):
            if item[0] == key:
                self.map[index][idx] = (key, value)
                found = True
                break
        if not found:
            self.map[index].append((key, value))
            self.size += 1
        
            
    def __getitem__(self, key):
        index = self.hash_function(key)
        
        for item in self.map[index]:
            if item[0] == key:
                return item[1]
        raise KeyError
    
    def __delitem__(self, key):
        index = self.hash_function(key)
        
        for idx, item in enumerate(self.map[index]):
            if item[0] == key:
                del self.map[index][idx]
                return
        raise KeyError
                
if __name__ == "__main__":
    
    hash = Hashmap(10)
    
    hash['march 1'] = 0
    hash['march 3'] = 10
    hash['march 6'] = 20
    hash['march 9'] = 30
    hash['march 12'] = 40
    hash['march 14'] = 50
    hash['march 17'] = 60
    hash['march 20'] = 70
    hash['march 23'] = 80
    hash['march 26'] = 90
    
    print(hash.map)
    
    print(hash.size)
    
    print(hash['march 17'])