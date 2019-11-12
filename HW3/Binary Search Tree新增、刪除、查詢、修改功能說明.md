# Binary Search Tree新增、刪除、查詢、修改功能說明 :bulb: 


| 1.新增 | 2.查詢 | 3.刪除  | 4.修改 |
| ------ | ------ | --- | --- |


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
