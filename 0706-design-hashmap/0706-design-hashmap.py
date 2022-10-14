class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        if key not in self.table:
            n = ListNode(key, value)
            self.table[key] = n
        else:
            existN = self.table[key]
            existN.value = value

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        else:
            return self.table[key].value

    def remove(self, key: int) -> None:
        if key in self.table:
            del self.table[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)