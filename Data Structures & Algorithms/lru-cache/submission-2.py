class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next= None


class LRUCache:
    def __init__(self, capacity: int):
        self.tail, self.head = None, None
        self.mp = {}
        self.limit = capacity
        self.cur = 0
        
    def addMRU(self, node):
        if self.head is None or self.tail is None:
            self.tail = self.head = node
            node.next = node.prev = None
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        # if node.key not in self.mp:
        #     self.mp[node.key] = node

    
    def remove(self, node):
        nextNode = node.next
        prevNode = node.prev
        if prevNode:
            prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode
        

        if self.head and self.head.key == node.key:
            self.head = self.head.next
        if self.tail and self.tail.key == node.key:
            self.tail = self.tail.prev
        
        node.prev = None
        node.next = None
        return node



    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        curNode = self.remove(self.mp[key])
        self.addMRU(curNode)

        return self.mp[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.mp: # update value
            curNode = self.mp[key]
            curNode.val = value

            curNode = self.remove(curNode)
            self.addMRU(curNode)
            return


        if self.cur >= self.limit:
            del self.mp[self.head.key]
            self.remove(self.head)   
        else:
            self.cur += 1

        newNode = Node(key, value)
        self.mp[key] = newNode
        self.addMRU(newNode)
                


        
        
