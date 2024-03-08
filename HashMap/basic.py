# Basic implementation of hash table/map without collision handling in py

class HashMap:
    def __init__(self) -> None:
        self.max_size = 10
        self.arr = [None] * self.max_size
    
    def hash_key(self, key) -> int:
        sum = 0
        for ch in key:
            sum += ord(ch)
        index = (sum % self.max_size)
        return index
    
    def __setitem__(self, key, value) -> None:
        index = self.hash_key(key)
        self.arr[index] = value
        
    def __getitem__(self, key):
        index = self.hash_key(key)
        return self.arr[index]
    
    def __delitem__(self, key) -> None:
        index = self.hash_key(key)
        self.arr[index] = None
        return

if __name__ == "__main__":
    hash = HashMap()
    
    #add key value pair to hash table
    hash['Sabbir'] = 27.5
    hash['Rohan'] = 26
    hash['Moshsheb'] = 28
    hash['Promita'] = 27
    
    print(hash['Promita'])
    print(hash['Sabbir'])
    
    del hash['Sabbir']
    print(hash['Sabbir'])