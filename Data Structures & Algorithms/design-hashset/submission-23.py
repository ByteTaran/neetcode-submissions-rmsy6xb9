class MyHashSet:

    def __init__(self):
        self.hashSet = [False] * 1000001

    def add(self, key: int) -> None:
        if not self.hashSet[key]:
            self.hashSet[key] = True
        return None

    def remove(self, key: int) -> None:
        if self.hashSet[key]:
            self.hashSet[key] = False

    def contains(self, key: int) -> bool:
        return self.hashSet[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)