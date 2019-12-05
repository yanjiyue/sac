# hw4流程圖與學習歷程、原理 :clapper: 


| :one:流程圖 | :two:學習歷程 | :three:原理| :four:參考資料    |
| ----------- | ------------- | --------------- | --- |


## :one:流程圖 :tropical_drink: 
![](https://i.imgur.com/6aJ5n54.jpg)
![](https://i.imgur.com/2Bm9hzq.jpg)
![](https://i.imgur.com/kLcrXpT.jpg)

## :two:學習歷程 :lemon: 
由於之前在有關算法的書上看到過哈希表，知道哈希表是一個整體是array，而每一個單點又是一種鏈錶的結構，但只是有個簡單的了解，為了進一步深入學習，瀏覽了一下網址：
* https://www.cnblogs.com/kumata/p/9157738.html
* https://www.cs.wcupa.edu/rkline/ds/hash-sets.html
* https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.g790b8351ca_0_290
* https://blog.csdn.net/wycgi/article/details/85063342
* https://blog.csdn.net/qq_39469688/article/details/81477131
* https://baike.baidu.com/item/哈希表/5981869?fr=aladdin
* https://www.bilibili.com/video/av74571805?from=search&seid=10335285457457210103
* https://www.bilibili.com/video/av17500428?from=search&seid=10335285457457210103

首先，嘗試些**add**功能
![](https://i.imgur.com/PQLf31U.jpg)
但出現如下錯誤
![](https://i.imgur.com/60d3Cs7.jpg)
於是給capacity賦值
![](https://i.imgur.com/6pNryvK.png)
又出現如下錯誤
![](https://i.imgur.com/hUf05fQ.jpg)
瀏覽後發現，key不是ListNode形式，且self.data中的數在塞進去時，就應該是ListNode的形式，所以做如下更改
![](https://i.imgur.com/9WtkJcC.jpg)

接下來，為驗證是否加入成功，所以先寫**contains**：
![](https://i.imgur.com/Osclkcq.jpg)
運行結果如下：
![](https://i.imgur.com/s7iXlyZ.png)
顯然沒有成功；
重新檢視add，發現並沒有將key順利塞入其中，應當先將新node跟舊的連接後，再放入其中，修改**add**如下：
![](https://i.imgur.com/EivwsCv.jpg)
測試成功 
![](https://i.imgur.com/eA2cOG6.png)

然後是**remove**：
```python=
def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        n=key%self.capacity
        node=self.data[n]
        before=None
        while node:
            if node.val==key:
                before.next=node.next
                return
            before=node
            node=node.next
```
但這樣如果是那個位置的第一個節點時則無法處理，因為沒有前面的節點的原故，
所以先需先排除幾種情況，修改如下：
```python=
def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
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
```
驗證成功
![](https://i.imgur.com/KlWflPP.png)

後來發現**add**中的
```python=
while node:
            node=node.next
```
其實多餘，所以修改**add**如下：
```python=
    def add(self, key):
        n=key%self.capacity
        node=self.data[n]
        newnode=ListNode(key)
        newnode.next=self.data[n]
        self.data[n]=newnode
```
但後來發現此時remove存在一個問題，即如果有兩個重複值僅能刪除一個，所以增加一個判斷是否還存在目標值的條件，以實現重複刪除的功能，修改**刪除**如下：
```python=
    def remove(self, key):
        while self.contains(key):
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
```
而此時，只能實現int的增，刪，查；文字的尚不能實現，故另設計可存儲文字的hash table如下：
```python=
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.data = [None] * capacity
        
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
```
其實只需比存int形式的目標多一步轉換，其餘邏輯與存int的相同
但需先導入
```python=
from Crypto.Hash import MD5
```
才可以對文字進行加密
## :three: 原理 :bookmark: 
| :one:__init __ | :two:add | :three:remove | :four:contains | :five:升級 | :six:原理  | 
| -------------- | -------- | ------------- | -------------- | -------------- | --- | 

* **註：前四個部分為對於存數值形式的功能解釋，第五部分為對存str形式的說明，由於邏輯基本相同，存str只有少部分不同，所以第五部分僅對新增部分進行說明**

### :one:  __init __  :ice_cream: 
```python=
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.data = [None] * capacity
```
capacity代表array的長度（非鏈錶），所以用capacity構建self.data這個array
### :two:add :telephone_receiver: 
```python=
    def add(self, key):
        n=key%self.capacity
        node=self.data[n]
        newnode=ListNode(key)
        newnode.next=self.data[n]
        self.data[n]=newnode
```
求key除self的array長度的餘數以決定key要放的位置，求餘數可以保證key一定有位置放，因為餘數不會大於被除數；
而後將key包裝為ListNode，將array上[n]上原本的鏈錶接到newnode後面，再用newnode代替array上[n]的位置上原來的鏈錶
### :three: remove :goat: 
```python=
    def remove(self, key):
        while self.contains(key):
```
判斷是否存在目標值
```python=
            n=key%self.capacity
            node=self.data[n]
```
找到array中的存放點
```python=
            before=None
            if node is None:
                print(False)
                return
            elif node.val==key:
                self.data[n]=node.next
```
首先處理集中特殊情況：存放點的開頭就是目標、存放點沒有東西
```python=
            else:
                before=None
                while node:
                    if node.val==key:
                        before.next=node.next
                        return
                    before=node
                    node=node.next
```
設置一個before代表向鏈錶下搜尋時的當前點的前一個點，以備找到後，可以直接將目標後面的東西接到目標的前面
找到後將目標後面的東西接到目標的前面
### :four: contains :cocktail: 
```python=
    def contains(self, key):
        n=key%self.capacity
        node=self.data[n]
```
找到目標的存放點後向鏈錶下搜尋
```python=
        while node:
            if node.val==key:
                return True
            node=node.next
        return False
```
如果找到，返回True；如果找遍鏈錶都沒有找到目標，則返回False
### :five:升級 :bicyclist:
以下為可存儲文字版的hashset：
```python=
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.data = [None] * capacity
        
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
```
現對如下代碼進行解釋：
```python=
        h=MD5.new()
        h.update(name.encode("utf-8"))
        key=int(h.hexdigest(),16)
```
由於輸入的參數為文字，所以先對文字進行轉換，以方便對其進行求餘數的處理（為確定存放位置）；
由於剩下的功能與前面的程式碼相同，所以在此省略。
### :six: 原理 :bread: 
> 哈希表（Hash table，也叫散列表），是根據關鍵碼值(Key value)而直接進行訪問的數據結構。也就是說，它通過把關鍵碼值映射到表中一個位置來訪問記錄，以加快查找的速度。這個映射函數叫做散列函數，存放記錄的數組叫做散列表。(摘抄自https://blog.csdn.net/yyyljw/article/details/80903391)

以下是我理解後的哈希表的幾個**特征**：
**1.有序性：** 哈希表結構形如字典，其key即為索引；這種結構將元素有序的置於表中，是一種結構有序的表。
**2.array與鏈表的結合：** 哈希表是一個將array和鏈表結合起來的結構，其主體為array，而每一個index存放一個鏈表。

由於其有序的結構，哈希表能夠通過關鍵字（key）快速定位，查找目標；

由於哈希表是結合了數組和鏈錶的結構形式，所以其具有二者的優點，同時能夠彌補二者的缺點：能夠比array更快的刪除，比鏈表更快的查找。

**構建哈希表的方式** ：
首先構建一個一定長度的array，再將每一個要放進去的元素放入一個鏈表的單位結構裡；

通過將元素數值化，再求餘（數值化後的元素除以array長度），確定存放的index，再將包裝成鏈表單位結構後的元素插入該index處的鏈表中。

## :four:參考資料 :blue_book: 
* https://www.cnblogs.com/kumata/p/9157738.html
* https://www.cs.wcupa.edu/rkline/ds/hash-sets.html
* https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.g790b8351ca_0_290
* https://blog.csdn.net/wycgi/article/details/85063342
* https://blog.csdn.net/qq_39469688/article/details/81477131
* https://baike.baidu.com/item/哈希表/5981869?fr=aladdin
* https://www.bilibili.com/video/av74571805?from=search&seid=10335285457457210103
* https://www.bilibili.com/video/av17500428?from=search&seid=10335285457457210103
* https://blog.csdn.net/yyyljw/article/details/80903391
