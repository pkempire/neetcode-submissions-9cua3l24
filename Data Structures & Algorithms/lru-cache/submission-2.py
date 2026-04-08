class Node: 
    def __init__(self,key=0,val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_n = node.prev
        next_n = node.next
        prev_n.next = next_n
        next_n.prev = prev_n

    def add(self,node):
        prev_n = self.tail.prev
        prev_n.next = node
        node.prev = prev_n
        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache.get(key)  
            self.remove(node)
            self.add(node)
            return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            self.remove(node)
            self.add(node)
            node.val = value 
        else:
            new = Node(key,value)
            self.cache[key] = new
            self.add(new)


        if len(self.cache) > self.cap:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]

