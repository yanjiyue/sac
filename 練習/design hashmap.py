#Design a HashMap without using any built-in hash table libraries.

#To be specific, your design should include these functions:

#put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
#get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
#remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

#Example:

#MyHashMap hashMap = new MyHashMap();
#hashMap.put(1, 1);          
#hashMap.put(2, 2);         
#hashMap.get(1);            // returns 1
#hashMap.get(3);            // returns -1 (not found)
#hashMap.put(2, 1);          // update the existing value
#hashMap.get(2);            // returns 1 
#hashMap.remove(2);          // remove the mapping for 2
#hashMap.get(2);            // returns -1 (not found) 

#Note:

#All keys and values will be in the range of [0, 1000000].
#The number of operations will be in the range of [1, 10000].
#Please do not use the built-in HashMap library.

class ListNode():
    def __init__(self, key, value):
        self.k = key
        self.v = value
        self.next = None


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = [None]*10000
    
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        i = key%10000
        if self.nodes[i] == None:
            self.nodes[i] = ListNode(key, value)
        elif self.find(key):
            node=self.nodes[i]
            while node:
                if node.k==key:
                    node.v=value
                    return
                node=node.next
        else:
            new=ListNode(key,value)
            new.next=self.nodes[i]
            self.nodes[i]=new
        
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        i = key%10000
        node=self.nodes[i]
        if self.nodes[i] == None:
            return -1
        while node:
            if node.k==key:
                return node.v
            node=node.next
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        while self.find(key):
            i = key%10000
            node=self.nodes[i]
            if self.nodes[i] == None:
                return False
            pre=None
            if node.k==key:
                self.nodes[i]=node.next
                return
            while node:
                if node.k==key:
                    pre.next=node.next
                    return
                pre=node
                node=node.next
            return False
        
    def find(self,key):
        i=key%10000
        node=self.nodes[i]
        while node:
            if node.k==key:
                return True 
            node=node.next
        return False

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
