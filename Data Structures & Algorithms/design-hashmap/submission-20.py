class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashMap = [Node(0,0) for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        curr = self.hashMap[key % 10000]
        while curr.next:
            if curr.next.key == key and curr.next.value == value:
                return None
            elif curr.next.key == key:
                curr.next.value = value
                return None
            curr = curr.next
        curr.next = Node(key, value)
        return None

    def get(self, key: int) -> int:
        curr = self.hashMap[key % 10000]
        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.hashMap[key % 10000]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return None
            curr = curr.next
        return None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)