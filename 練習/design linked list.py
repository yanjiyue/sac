class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
       #建立Node
        
class MyLinkedList:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=0
        self.head=None
        self.tail=None
#初始化
 
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index>=self.size or index<0:
            return -1 #假如index超過self長度或index<0，則無效，輸出-1
        else:
            node=self.getIdNode(index)#調用後面的功能取得需要的index位置的值
            return node.val  

        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            self.tail=newNode #假如self.head為None，則self為空，則令head及tail都=val
        else:
            newNode.next=self.head #在newNode的後面放self.head
            self.head.prev=newNode #在self.head的前面放newNode
            self.head=newNode   #讓head為val
        self.size += 1 #增加self的長度

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            self.tail=newNode #假如self.head為None，則self為空，則令head及tail都=val
        else:
            newNode.prev=self.tail #讓newNode的前面指向self.tail
            self.tail.next=newNode #讓self的原tail指向newNode
            self.tail=newNode #賦值
        self.size += 1  #增加self的長度

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index<=0:
            self.addAtHead(val) #引用前面的功能
        elif index==self.size:
            self.addAtTail(val) #引用前面的功能
        elif index>self.size:
            return #此為無效，故不處理
        else:
            newNode=Node(val)
            n=self.getIdNode(index) #引用後面功能，取得要插入的位置的原來東西
            newNode.prev=n.prev #val前面是原來位置的前面的東西
            newNode.next=n #val的後面是原來位置的東西
            n.prev.next=newNode #原來位置的前面的後面是val
            n.prev=newNode #原來的東西現在前面是val
            self.size +=1 #增加self的長度

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0 or index>=self.size:
            return #無效，不處理
        if index==0:
            self.deleteHead() #調用後面功能
        elif index==self.size-1:
            self.deleteTail() #調用後面功能
        else:
            n=self.getIdNode(index) #取得要刪除的東西
            n.prev.next=n.next #在index前面的後面插入index+1的東西
            n.next.prev=n.prev #在index後面的前面插入index-1的東西
            del n #刪除要刪的東西
        self.size -=1 #減少self的長度

    def getIdNode(self,x):
        n=self.head
        for a in range(x):
            n=n.next
        return n #讓n進入回圈直到取得需要的位置
    
    def deleteHead(self):
        n=self.head
        if self.size==1:
            self.head==None
            self.tail==None #若self只有一個東西，則直接清空self
        else:
            self.head.next.prev=None #在head後插入None
            self.head=self.head.next #讓head變為None
        del n #刪除head
            
            
    def deleteTail(self):
        n=self.tail
        if self.size==1:
            self.head==None
            self.tail==None #若self只有一個東西，則直接清空self
        else:
            self.tail.prev.next=None #讓tail的前面的後面為None
            self.tail=self.tail.prev #讓現在的tail等於前面的東西，也就是None
        del n #刪除tail
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
