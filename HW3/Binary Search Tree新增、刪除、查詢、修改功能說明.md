# Binary Search Tree新增、刪除、查詢、修改功能說明 :bulb: 


| 1.新增 | 2.查詢 | 3.刪除  | 4.修改 |5.遍歷|
| ------ | ------ | --- | --- |---|


## :one: 新增 :cake: 
```python=
def insert(self,root,item):#新增
        if root==[]:
            node=[item,[],[]]
            root.extend(node)
            return root
```
:books:假如二叉樹是空的，則新建一個根二叉樹（包括根節點與空的左右子樹）;若根節點已有東西，則向下搜尋空缺處加入：
```python=
         else:     
            if item<=root[0]:
                newr=root[1]
                if len(newr)<1:
                    node=[item,[],[]]
                    root[1].extend(node)
                else:
                    self.insert(newr,item)
            
```
> 如果加入數小於根節點則進入左子樹中，如果左子樹為空，則再向下（左子樹的子樹）搜尋，直到找到空的節點，加入目標數。
>
>  同理可得當加入數大於根節點數的處理方式如下：
```python=
            else:
                newr=root[2]
                if len(newr)<1:
                    node=[item,[],[]]
                    root[2].extend(node)
                else:
                    self.insert(newr,item)
        return root
```
> 最後返回二叉樹 :tada: 

## :two: 查詢 :calling: 
```python=
def search(self,root,item):#查找
        if root==[] or (item<root[0] and root[1]==[]) or (item>root[0] and root[2]==[]):
            return False
        else:
            if root[0]==item:
                return root[0],root[1][0],root[2][0]
            else:
                root1=root
                if item<=root[0]:
                    newr=root[1]
                else:
                    newr=root[2]
                return self.searchid(root,newr,item)
```
:book: 首先排除肯定不存在的情況，即二叉樹為空，目標值小於根節點但左子樹為空，目標值大於根節點但右子樹為空的情況，若非如上情況，則進入查詢
>如果目標值就是根節點，則離根節點最近且包含子節點的treenode為根節點與其兩個子節點，由於此種情況有別於其他情況，所以單立一項處理
>
>如果不是此種情況，分別大小以後，藉助函數searchid來處理
>
>  由於這種情況，離根節點最近的treenode由目標函數的父節點與父節點的左右節點構成，所以需保留目標函數的上一層樹，所以searchid函數需輸入（父樹，父樹的子樹，目標值），如下：

```python=
def searchid(self,root,newr,item):
        if root==[] or (item<root[0] and root[1]==[]) or (item>root[0] and root[2]==[]):
            return False
        elif newr[0]==item:
            if root[1]!=[] and root[2]!=[]: 
                return root[0],root[1][0],root[2][0]
            elif root[1]==[] and root[2]!=[]:
                return root[0],root[1],root[2][0]
            elif root[2]==[] and root[1]!=[]:
                return root[0],root[1][0],root[2]
            else:
                return root[0],root[1],root[2]
        elif item<root[0]:
            nroot=newr
            newr=newr[1]
            return self.searchid(nroot,newr,item)
        else:
            nroot=newr
            newr=newr[2]
            return self.searchid(nroot,newr,item)
        
```
> 同search函數中一樣，首先排除肯定不存在的情況再進入查詢
> 
> 如果目標函數小於（大於）父樹的子樹的根節點，則進入父樹的子樹的左（右）子樹，同時保留新的父樹（即父樹的子樹的左（右）子樹的父樹），再次進入searchid函數進行查詢
> 
> 直到找到子樹的根等於目標節點，返回父樹與父樹的左右節點（如果父樹的左節點（右節點）空，則返回父節點與右節點（左節點））。 :paperclip: 

## :three:刪除 :tea: 
:first_quarter_moon_with_face: 首先用遍歷（詳見第五點）所有數放入一個list中
```python=
def delete(self,root,item):#刪除
        c=0
        check=[]
        a=self.preorder(root,check)
        for i in range(len(a)-1):
                if a[i]==item:
                    c+=1
```
> 排除沒有必要進行刪除動作的情況：
```python=
        if len(a)<1:
            return False
```
> 再處理刪除根的情況：
```python=
        elif len(a)==1:
            if root[0]!=item:
                return root
            else:
                root.clear()
```
> 若都不是，則判斷目標數有幾個，無則返回False；有則進行相應次數的刪除動作（調用delhelp函數）：
```python=
        else:
            if c==0:
                return False
            else:
                self.delhelp(root,item)
                while c>=0:
                    self.delhelp(root,item)
                    c-=1
```  
> 如果樹為空，或目標值大於（小於）根節點，但右（左）子樹為空，則知無目標值，返回False（其實如果有此情況，依在函數delete中被排除，但為使邏輯通暢，故予以保留）
```python=
def delhelp(self,root,item):
        if root==[] or (item<root[0] and root[1]==[]) or (item>root[0] and root[2]==[]):            
                return False 
```
> 假如根節點為目標值，則找到目標值；
```python=
        elif item==root[0]:
```
> 如果左右子樹為空，則將整棵樹清空
```python=
            if root[1]==[] and root[2]==[]:
                root.clear()
```
> 如果左（右）子樹存在，右（左）子樹不存在，則用左（右）子樹代替原樹
```python=
            elif root[1]==[]:
                root[:]=root[2]
            elif root[2]==[]:
                root[:]=root[1]
```
> 如果左右子樹都存在，則找到左子樹中最大值取代目標數值（保證目標值左右子樹結構：左子樹小於根節點，右子樹大於根節點）
```python=
            else:
                max=self.getmax(root[1])
                root[0]=max
```
> 如果還沒找到，則繼續向子樹中取找
> 大於根節點，往右子樹找；反之往左子樹找
```python=
        elif item<root[0]:
            return self.delhelp(root[1],item)
        else:
            return self.delhelp(root[2],item)  
 ```
>> 以下為取得最大值的函數
>> 如果右子樹為空，則為樹中最大值
```python=
def getmax(self,root):
        if root[2]==[]:
            m=root[0]
```
> >此時此值已被取走
> >若此值左子樹為空，則清空樹
```python=
            if root[1]==[]:
                root.clear()
```
> >否則用左子樹取代該位置
```python=
            else:
                root[:]=root[1]
            return m
```
> >若還沒找到目標數，則向右子樹中繼續找：
```python=
        else:return getmax(root[2])
```
## :four: 修改 :package: 
首先排除樹為空的情況：
```python=
def modify(self,root,item,change):#修改
        if root==[]:
            return False
```
> 用遍歷，將所有數值列為list後，判斷需要修改幾個數
```python=
        c=0
        check=[]
        a=self.preorder(root,check)
        for i in range(len(a)):
                if a[i]==item:
                    c+=1
                    a[i]=change 
                else:
                    a[i]=a[i]
```
> 如果沒有目標數，則返回False：
```python=
        if c<=0:
            return False
```
> 否則，將list中的數依次加入新樹中，這種方法可以防止二叉樹結構被破壞（小數在右子樹或大數在左子樹） :zap: 
```python=
        else:
            result=[]
            for n in range(len(a)):
                m=a[n]
                self.insert(result,m)
            return result
```
## :five: 遍歷 :taxi: 
先序遍歷順序為根左右
建立一個空list用以存儲樹中的元素
依次將根節點、左節點、右節點加入list中
最後返回list :pizza: 
```python=
def preorder(self, root,check):  #先序遍歷    
        if root==[]:            
            return []        
        check.append(root[0])
        checkl=[]
        checkr=[]
        check.extend(self.preorder(root[1],checkl))
        check.extend(self.preorder(root[2],checkr))
        return check
```
