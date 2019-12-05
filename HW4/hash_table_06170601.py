from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, name):
        h=MD5.new()
        h.update(name.encode("utf-8"))
        key=int(h.hexdigest(),16)
        n=key%self.capacity
        node=self.data[n]
        newnode=ListNode(key)
        newnode.next=self.data[n]
        self.data[n]=newnode
        
    def remove(self, name):
        h=MD5.new()
        h.update(name.encode("utf-8"))
        key=int(h.hexdigest(),16)
        while self.contains(name):
            n=key%self.capacity
            node=self.data[n]
            before=None
            if node is None:
                print(False)
                return
            elif node.val==key:
                self.data[n]=node.next
            else:
                before=None
                while node:
                    if node.val==key:
                        before.next=node.next
                        return
                    before=node
                    node=node.next
        
            
    def contains(self, name):
        h=MD5.new()
        h.update(name.encode("utf-8"))
        key=int(h.hexdigest(),16)
        n=key%self.capacity
        node=self.data[n]
        while node:
            if node.val==key:
                return True
            node=node.next
        return False
    
#https://www.cnblogs.com/kumata/p/9157738.html
#https://www.cs.wcupa.edu/rkline/ds/hash-sets.html
#https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.g790b8351ca_0_290
#https://blog.csdn.net/wycgi/article/details/85063342
#https://blog.csdn.net/qq_39469688/article/details/81477131
#https://baike.baidu.com/item/哈希表/5981869?fr=aladdin
#https://www.bilibili.com/video/av74571805?from=search&seid=10335285457457210103
#https://www.bilibili.com/video/av17500428?from=search&seid=10335285457457210103
#https://blog.csdn.net/yyyljw/article/details/80903391
