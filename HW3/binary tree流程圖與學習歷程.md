# HW3_Binary tree流程圖與學習歷程


| 1.流程圖 | 2.學習歷程 | 3.參考網址 |
| -------- | -------- | -------- |
## :one:流程圖 :walking: 
![](https://i.imgur.com/9Gq47Ri.jpg)

![](https://i.imgur.com/fJaaal3.jpg)
![](https://i.imgur.com/fvLUtMZ.jpg)
## :two:學習歷程 :racehorse: 
參考了這些網站：
> https://blog.csdn.net/weixin_41503009/article/details/82356000
> https://blog.csdn.net/wzngzaixiaomantou/article/details/81294915
> https://blog.csdn.net/qq_29681777/article/details/83903003
> https://www.cnblogs.com/anzhengyu/p/11083568.html
> https://blog.csdn.net/w17688977481/article/details/88581622
> https://www.laurentluce.com/posts/binary-search-tree-library-in-python/
#
後,根據Linked list
（https://blog.csdn.net/liaoshenglan/article/details/100594507）![](https://i.imgur.com/caFvoTt.jpg)
![](https://i.imgur.com/6HHYexJ.jpg)
![](https://i.imgur.com/1RSW61X.jpg)
![](https://i.imgur.com/lTO9FZu.jpg)
![](https://i.imgur.com/Nkm6xig.jpg)
首先改變如下：
![](https://i.imgur.com/XmJzAVv.jpg)
![](https://i.imgur.com/94rq9dT.jpg)
![](https://i.imgur.com/dePLcpz.jpg)
![](https://i.imgur.com/CwWx5GE.jpg)
雖然語法沒有錯誤，但是運行不了，如下：
![](https://i.imgur.com/xGjVvlq.jpg)
於是想另尋解決辦法，參考了該網站（https://www.bilibili.com/video/av19992545?from=search&seid=7930082564365361589）
的教學視頻的方式，開始思考是否可以用list的方式呈現binary tree，如下形式：
> [root,						#根節點
> [left root,[left childtree,[],[]],		#左子樹
> [right root,[right childtree,[],[]]]]	#右子樹

於是根據這種形式，寫出了二叉樹的**添加**
![](https://i.imgur.com/ldDvB5H.jpg)
Node形式為[root,[],[]]，每增加一個節點即增加一個node；將node加入還空著的節點，如果節點已有node存在，則一直向下找，直到找到可以插入的節點。

和**查找**：
![](https://i.imgur.com/9Yjz4Py.jpg)
如果查到的是根節點，則離根節點最近的treenode就是根節點與根節點的左節點和右節點；

如果不是根節點，則離根節點最近的節點為目標節點的父節點與目標節點與目標節點的兄弟節點，所以如果目標不是根節點，則需保留目標節點的父節點的treenode，所以建立函數searchid來處理這類情況，同時將目標節點與父節點的treenode放入函數searchid中；
找到目標節點後，返回父節點，目標節點與目標節點的兄弟節點

接著是**刪除**，首先是刪除位置的替代問題，如下：
![](https://i.imgur.com/9ELJuHO.jpg)
先排除不存在的情況

接著是找尋，若找到且只有一個子樹，則用該子樹代替父樹；否則就用如下代碼：
![](https://i.imgur.com/VyOasFR.png)
找到左子樹中的最大值，並讓最大值的左子樹代替其位置（因為該值為最大所以不存在右子樹）；

用最大值代替目標節點。

但此時並不能將所有目標數值刪除，所以思考如何讓程式可以重複進行；

於是想到用遍歷，將所有數值放入一個list中，再計算目標數的個數，以確定重複次數![](https://i.imgur.com/E48Is8Q.png)
而後再用循環語句讓刪除動作重複
![](https://i.imgur.com/Fbavgyr.jpg)
將原本的刪除動作放入附屬函數中![](https://i.imgur.com/3yW8mnz.jpg)
如此達到刪除所有目標數值的目的

接著是**修改**

修改需面臨的問題，除了有重複進行的問題，還有順序保持的問題（如果根節點為10，左子節點為2，將2改成20時，出現左節點大於根節點的情況，破壞了二叉樹的結構）

結合如上，同時吸取刪除函數的經驗，先遍歷，將所有數值放入一個list，接著改變list中所有目標數值的數值，然後再將list中的數值依次放入二叉樹中，如此可以保證二叉樹的結構不被破壞。
![](https://i.imgur.com/ZyZk6h2.jpg)
#
但是依助教的格式，不能如此寫，所以再根據如上思路改為助教要求的格式，寫成的**增**：
```python=
    def insert(self,node,item):#新增
        if node.val is None:
            node=TreeNode(item)
        else:
            if node.val>=item:
                if node.left is None:
                    node.left=TreeNode(item)  
                else:
                    newnode=node.left
                    self.insert(newnode,item)
            else:
                if node.right is None:
                    node.right=TreeNode(item)
                else:
                    newnode=node.right
                    self.insert(newnode,item)
                
        return node
```
邏輯與前面用數組寫成的大致相同
# 
**改**：
```python=
     def modify(self,node,item,change):#修改
        if node.val is None:return False
        c=0
        a=self.preorder(node)
        m=[0]*len(a)
        for i in range(len(a)):
                if a[i]==item:
                    c+=1
                    m[i]=change 
                else:
                    m[i]=a[i]
        if c<=0:return False
        else:
            node1=TreeNode(m[0])
            for n in range(1,len(m)):
                self.insert(node1,m[n])
            return node1
    
    def preorder(self, root):  #先序遍歷    
        if root is None:            
            return []        
        result = [root.val]        
        left_item = self.preorder(root.left)        
        right_item = self.preorder(root.right)        
        return result + left_item + right_item

```
同樣利用遍歷取出所有數值後修改後，逐個放到新樹中
#
接下來是**查**：
```python=
    def search(self,node,item):#查
        if (node.val is None) or (item<node.val and node.left is None) or (item>node.val and node.right is None):return False
        elif node.val==item:return node
        elif item<=node.val:
            newnode=node.left
            return self.search(newnode,item)
        else:
            newnode=node.right
            return self.search(newnode,item)
```
**刪**：
```python=
    def delete(self,node,item):#刪除
        c=0
        a=self.preorder(node)
        m=[]
        for i in range(len(a)-1):
                if a[i]==item:
                    c+=1
                else:m.append(a[i])
        if len(a)<1:
            return False
        else:
            if c==0:
                return False
            else:
                node1=TreeNode(m[0])
                for n in range(1,len(m)):
                    self.insert(node1,m[n])
                return node1 
            
    def preorder(self, root):  #先序遍歷    
        if root is None:            
            return []        
        result = [root.val]        
        left_item = self.preorder(root.left)        
        right_item = self.preorder(root.right)        
        return result + left_item + right_item
```
同樣先用遍歷將所有節點值抓出後，將要保留的數加入新list中，然後逐個放入新樹中。

## :three:參考網址 :school: 
:one:https://blog.csdn.net/weixin_41503009/article/details/82356000
#
:two:https://blog.csdn.net/wzngzaixiaomantou/article/details/81294915
#
:three:https://blog.csdn.net/qq_29681777/article/details/83903003
#
:four:https://www.cnblogs.com/anzhengyu/p/11083568.html
#
:five:https://blog.csdn.net/w17688977481/article/details/88581622
#
:six:https://www.laurentluce.com/posts/binary-search-tree-library-in-python/
#
:seven:https://blog.csdn.net/liaoshenglan/article/details/100594507
