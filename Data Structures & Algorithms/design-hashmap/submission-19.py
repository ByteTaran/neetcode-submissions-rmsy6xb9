class MyHashMap:

    def __init__(self):
        self.hashMap = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        if self.hashMap[key] != value:
            self.hashMap[key] = value
        return None

    def get(self, key: int) -> int:
        return self.hashMap[key]

    def remove(self, key: int) -> None:
        if self.hashMap[key] != -1:
            self.hashMap[key] = -1
        return None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)