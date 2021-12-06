"""

"""

class HashMap:
    def __init__(self, MAX: int= 100):
        self.MAX = MAX
        self.arr = [None for i in range(self.MAX)]
    
    def generate_hash(self, key: str=""):
        """
        Generate hash of key:str
        Args:
            `key`: str
        """
        if isinstance(key, list):
            key = ''.join(key)            
        hash = sum([ord(char) for char in key]) % self.MAX
        return hash
        
    def set(self, key: str= "", value: str= ""):
        """
        """
        hash = self.generate_hash(key=key)
        self.arr[hash] = value
    
    def __sethash__(self, key: str ="", value: str= ""):
        """"""
        hash = self.generate_hash(key=key)
        self.arr[hash]=value
        
    def get(self, key: str= ""):
        hash = self.generate_hash(key=key)
        if not self.arr[hash]:
            raise KeyError(f"{str(key)} is not a proper key")
        return self.arr[hash]    

    def __getitem__(self, key):
        hash = self.generate_hash(key=key)
        return self.arr[hash]

    # def delete(self, key: str=""):
    #     pass

    # def get_length(self):
    #     pass

    # def get_keys(self):
    #     """
    #     Get list of keys in hash map
    #     """
    #     pass
    
    # def get_values(self):
    #     """
    #     Get list of values in hash map
    #     """
    #     pass

    # def get_items(self):
    #     """
    #     Get all key-value pairs
    #     """
    #     pass
    
    def fetch(self):
        """
        Fetch all values in hash map
        """
        return [element for element in self.arr if element is not None]
        

if __name__ == "__main__":
    hm = HashMap()
    hm.set(key="key", value="value")
    print(hm.fetch())




    
# ht = HashMap()
# ht.set(key="key", value="value")
# # keys = ht.get(key="ke")
# print(ht['asdf'])
# print(keys)


