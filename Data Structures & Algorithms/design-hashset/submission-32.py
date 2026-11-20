class Node:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashSet = [Node(0) for _ in range(10000)]

    def add(self, key: int) -> None:
        curr = self.hashSet[key % 10000]
        while curr.next:
            if curr.next.key == key:
                return None
            curr = curr.next
        curr.next = Node(key)
        return None

    def remove(self, key: int) -> None:
        curr = self.hashSet[key % 10000]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return None
            curr = curr.next
        return None

    def contains(self, key: int) -> bool:
        curr = self.hashSet[key % 10000]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)