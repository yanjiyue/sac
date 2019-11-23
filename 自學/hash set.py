#Design a HashSet without using any built-in hash table libraries.

#To be specific, your design should include these functions:

#add(value): Insert a value into the HashSet. 
#contains(value) : Return whether the value exists in the HashSet or not.
#remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

#Example:

#MyHashSet hashSet = new MyHashSet();
#hashSet.add(1);         
#hashSet.add(2);         
#hashSet.contains(1);    // returns true
#hashSet.contains(3);    // returns false (not found)
#hashSet.add(2);          
#hashSet.contains(2);    // returns true
#hashSet.remove(2);          
#hashSet.contains(2);    // returns false (already removed)

#Note:

#All values will be in the range of [0, 1000000].
#The number of operations will be in the range of [1, 10000].
#Please do not use the built-in HashSet library.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:

    def __init__(self,capacity=100):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key: int) -> None:
        idx = key % self.capacity
        node = self.data[idx]
        while node:
            if node.val == key:
                return
            node = node.next
        new_node = ListNode(key)
        new_node.next = self.data[idx]
        self.data[idx] = new_node
    def remove(self, key: int) -> None:
        idx = key % self.capacity
        node = self.data[idx]
        if node and node.val == key:
            self.data[idx] = node.next
            return
        pre = None
        while node:
            if node.val == key:
                pre.next = node.next
                return
            pre = node
            node = node.next


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.capacity
        node = self.data[idx]
        while node:
            if node.val == key:
                return True
            node = node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
