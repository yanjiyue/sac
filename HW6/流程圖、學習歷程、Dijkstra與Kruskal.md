# hw6流程圖、學習歷程、原理 :christmas_tree: 


| :one:流程圖 | :two:學習歷程 | :three:原理 | :four:參考資料 |
| ----------- | ------------- | ----------- | --- |


## :one:流程圖 :snowflake: 


| 1.Dijkstra | 2.kruskal | 
| -------- | -------- | 

### 1.Dijkstra
![](https://i.imgur.com/K7uVhcU.jpg)

### 2.Kruskal
![](https://i.imgur.com/VjEn0YO.jpg)


## :two:學習歷程 :ship: 
首先參考了
https://www.cnblogs.com/skywang12345/p/3711496.html
和
https://blog.csdn.net/sm20170867238/article/details/89988982
了解了兩個最佳路徑搜尋的概念後，開始嘗試Dijkstra
```python=
     def Dijkstra(self, s): 
        result=dict()
        e=str(s)
        result[e]=0
        check=self.graph[s]
        need=[]
        need.append(s)
        while len(self.graph)!=len(need):
            z=0
            for i in range(len(check)-1):
                if check[z]!=0 and check[z]>check[i]:
                    z=i
            check1=[]
            print(z)
            need.append(z)
            y=str(z)
            result[y]=check[z]
            for n in range(len(self.graph[z])):
                p=result[y]+self.graph[z][n]
                check1.append(p)
            for m in range(len(check)):
                if check[m]!=0 and check1[m]!=0 and check1[m]<check[m]:
                    check[m]=check1[m]
            
        return  result 
```
用課件提供之測資：
```
g=Graph(9)
g.graph=[[0,4,0,0,0,0,0,8,0],
        [4,0,8,0,0,0,0,11,0],
        [0,8,0,7,0,4,0,0,2],
        [0,0,7,0,9,14,0,0,0],
        [0,0,0,9,0,10,0,0,0],
        [0,0,4,14,10,0,2,0,0],
        [0,0,0,0,0,2,0,1,6],
        [8,11,0,0,0,0,1,0,7],
        [0,0,2,0,0,0,6,7,0]
        ];
        
print("dijkstra",g.Dijkstra(0))
```
測試，
但結果為
```
dijkstra {'0': 0}
```
說明程式並沒有往下跑；
故做如下修改：
```python=
    def Dijkstra(self, s): 
        result=dict()
        e=str(s)
        result[e]=0
        check=self.graph[s]
        need=[]
        need.append(s)
        while len(self.graph)!=len(need):
            z=0
            for i in range(len(check)-1):
                if z==i and z==0:
                    z=1
                elif z==i:
                    z=z
                elif check[z]!=0 and check[i]!=0 and check[z]>check[i]:
                    z=i
            check1=[]
            print(z)
            need.append(z)
            y=str(z)
            result[y]=check[z]
            for n in range(len(self.graph[z])):
                p=result[y]+self.graph[z][n]
                check1.append(p)
            for m in range(len(check)):
                if check[m]!=0 and check1[m]!=0 and check1[m]<check[m]:
                    check[m]=check1[m]
            
        return  result 
```
結果如下：
```
dijkstra {'0': 0, '1': 4}
```
說明只跑了第一步，
所以再做修改如下：
```python=
    def Dijkstra(self, s): 
        result=dict()
        e=str(s)
        result[e]=0
        check=self.graph[s]
        quiz=[None]*len(check)
        for i in range(len(check)-1):
            quiz[i]=i+1
        need=[]
        need.append(s)
        while len(need)<=(len(check)+1):
            for t in range(len(quiz)-1):
                if quiz[t]!=0:
                    z=t
                    break
                else:continue
            for i in range(len(check)-1):
                if quiz[i]!=0: 
                    if check[z]!=0 and check[i]!=0 and check[z]>check[i] and z not in need:
                        z=i
            quiz[z]=0       
            need.append(z)
            y=str(z)
            result[y]=check[z]
            check1=[]
            for n in range(len(self.graph[z])):
                p=result[y]+self.graph[z][n]
                check1.append(p)
            for m in range(len(check)):
                if m not in need:
                    if check[m]!=0 and check1[m]!=0 and check1[m]<check[m]:
                        check[m]=check1[m]
            print(check1)
            print(check)
            print(need)
            print(result)
        return  result 
```
結果如下：
```
dijkstra {'0': 0, '1': 4, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1}
```
發現除了前兩位的值正確，其他都錯誤；
後來將每一個循環後的check、check1、need和result打印出來，如下：
```
[0, 4, 0, 0, 0, 0, 0, 8, 0]
[0, 4, 0, 0, 0, 0, 0, 8, 0]
[0, 0]
{'0': 0}
[8, 4, 12, 4, 4, 4, 4, 15, 4]
[0, 4, 0, 0, 0, 0, 0, 8, 0]
[0, 0, 1]
{'0': 0, '1': 4}
[0, 8, 0, 7, 0, 4, 0, 0, 2]
[0, 4, 0, 0, 0, 0, 0, 8, 0]
[0, 0, 1, 2]
{'0': 0, '1': 4, '2': 0}
[0, 0, 7, 0, 9, 14, 0, 0, 0]
[0, 4, 0, 0, 0, 0, 0, 8, 0]
[0, 0, 1, 2, 3]
{'0': 0, '1': 4, '2': 0, '3': 0}
[0, 0, 0, 9, 0, 10, 0, 0, 0]
[0, 4, 0, 0, 0, 0, 0, 8, 0]
[0, 0, 1, 2, 3, 4]
{'0': 0, '1': 4, '2': 0, '3': 0, '4': 0}
[0, 0, 4, 14, 10, 0, 2, 0, 0]
[0, 4, 0, 0, 0, 0, 0, 8, 0]
[0, 0, 1, 2, 3, 4, 5]
{'0': 0, '1': 4, '2': 0, '3': 0, '4': 0, '5': 0}
[0, 0, 0, 0, 0, 2, 0, 1, 6]
[0, 4, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 1, 2, 3, 4, 5, 6]
{'0': 0, '1': 4, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
[9, 12, 1, 1, 1, 1, 2, 1, 8]
[0, 4, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 1, 2, 3, 4, 5, 6, 7]
{'0': 0, '1': 4, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1}
[9, 12, 1, 1, 1, 1, 2, 1, 8]
[0, 4, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 1, 2, 3, 4, 5, 6, 7, 7]
{'0': 0, '1': 4, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1}
[9, 12, 1, 1, 1, 1, 2, 1, 8]
[0, 4, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 1, 2, 3, 4, 5, 6, 7, 7, 7]
{'0': 0, '1': 4, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1}
dijkstra {'0': 0, '1': 4, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 1}
```
發現need中第一的因素重複了一次，且後面不停重複第一次採用的行，
後進行排誤修改如下：
```python=
    def Dijkstra(self, s): 
        result=dict()
        e=str(s)
        result[e]=0
        check=self.graph[s]
        quiz=[None]*len(check)
        for i in range(len(check)-1):
            quiz[i]=i+1
        quiz[s]=0
        need=[]
        need.append(s)
        while len(need)<=(len(check)+1):
            for t in range(len(quiz)-1):
                if quiz[t]!=0:
                    z=t
                    break
                else:continue
            for i in range(len(check)-1):
                if quiz[i]!=0: 
                    if check[z]!=0 and check[i]!=0 and check[z]>check[i] and z not in need:
                        z=i
            quiz[z]=0       
            need.append(z)
            y=str(z)
            result[y]=check[z]
            check1=[]
            for n in range(len(self.graph[z])-1):
                if self.graph[z][n]!=0:
                    p=result[y]+self.graph[z][n]
                    check1.append(p)
                else:
                    check1.append(self.graph[z][n])
            for m in range(len(check)-1):
                if m not in need:
                    if check[m]==0:
                        check[m]=check1[m]
                    if check[m]!=0 and check1[m]!=0 and check1[m]<check[m]:
                        check[m]=check1[m]
            for m in range(len(check)-1):
                if quiz[m]==0:
                    check[m]=0
            print(check)
            print(check1)
            print(need)
        return  result 
```
結果如下：
```
dijkstra {'0': 0, '1': 4, '7': 8, '6': 9, '5': 11, '2': 12, '3': 19, '4': 0}
```
缺失了'8',還有'4'的值錯誤
將check、check1和need依次打印如下：
```
[0, 0, 12, 0, 0, 0, 0, 8, 0]
[8, 0, 12, 0, 0, 0, 0, 15]
[0, 1]
[0, 0, 12, 0, 0, 0, 9, 0, 0]
[16, 19, 0, 0, 0, 0, 9, 0]
[0, 1, 7]
[0, 0, 12, 0, 0, 11, 0, 0, 0]
[0, 0, 0, 0, 0, 11, 0, 10]
[0, 1, 7, 6]
[0, 0, 12, 25, 21, 0, 0, 0, 0]
[0, 0, 15, 25, 21, 0, 13, 0]
[0, 1, 7, 6, 5]
[0, 0, 0, 19, 21, 0, 0, 0, 0]
[0, 20, 0, 19, 0, 16, 0, 0]
[0, 1, 7, 6, 5, 2]
[0, 0, 0, 0, 21, 0, 0, 0, 0]
[0, 0, 26, 0, 28, 33, 0, 0]
[0, 1, 7, 6, 5, 2, 3]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 30, 0, 31, 0, 0]
[0, 1, 7, 6, 5, 2, 3, 4]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 9, 0, 10, 0, 0]
[0, 1, 7, 6, 5, 2, 3, 4, 4]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 9, 0, 10, 0, 0]
[0, 1, 7, 6, 5, 2, 3, 4, 4, 4]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 9, 0, 10, 0, 0]
[0, 1, 7, 6, 5, 2, 3, 4, 4, 4, 4]
dijkstra {'0': 0, '1': 4, '7': 8, '6': 9, '5': 11, '2': 12, '3': 19, '4': 0}
```
發現當check中僅剩一個元素（其他已歸零），則會重複幾次後，此位的值歸零（'4':0的原因）；且need的長度為11，超出了應該的長度；
做修改如下：
```python=
    def Dijkstra(self, s): 
        result=dict()
        e=str(s)
        result[e]=0
        check=self.graph[s]
        quiz=[None]*len(check)
        for i in range(len(check)):
            quiz[i]=i+1
        quiz[s]=0
        need=[]
        need.append(s)
        while len(need)<(len(check)):
            for t in range(len(quiz)):
                if quiz[t]!=0 and check[t]!=0:
                    z=t
                    break
                else:continue
            for i in range(len(check)):
                if quiz[i]!=0: 
                    if check[i]!=0 and check[z]>check[i] and z not in need:
                        z=i
                 
            need.append(z)
            y=str(z)
            result[y]=check[z]
            check1=[]
            quiz[z]=0 
            for n in range(len(self.graph[z])):
                if self.graph[z][n]!=0:
                    p=result[y]+self.graph[z][n]
                    check1.append(p)
                else:
                    check1.append(0)
            for m in range(len(check)):
                if check[m]==0:
                    check[m]=check1[m]
                elif check1[m]!=0 and check1[m]<check[m]:
                    check[m]=check1[m]
                else:check[m]=check[m]
            for m in range(len(check)-1):
                if quiz[m]==0:
                    check[m]=0
        want=dict()
        for i in range(len(self.graph[0])):
            l=str(i)
            want[l]=result[l]
        return  want 
```
結果正確：
```
dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}
```
接下來寫Kruskal，首先參考：
1.https://www.bilibili.com/video/av79186816?from=search&seid=17195856858988781128
2.https://www.bilibili.com/video/av36884622/?spm_id_from=333.788.videocard.5
3.https://www.bilibili.com/video/av36885495/?spm_id_from=333.788.videocard.2
4.https://www.bilibili.com/video/av36884375?from=search&seid=718402740995726549
5.https://www.bilibili.com/video/av26403085?from=search&seid=718402740995726549
首先寫addEdge：
```python=
    def addEdge(self,u,v,w): 
        new=node(u,v,w)
        self.graph.append(new)
```
需構建另一個class以製造node：
```python=
class node:
    def __init__(self,begin,target,weight):
        self.b=begin
        self.t=target
        self.w=weight
```
構建完成後，開始寫Kruskal；
首先要根據weight進行排序，所以引用HW1——https://github.com/yanjiyue/sac/blob/master/HW1/quicksort.ipynb
中的quicksort（做了一些改動）：
```python=
    def quicksort(self,data):
        if len(data)<2:
            return data
        else:
            mid=data[len(data)-1]
            left=[]
            right=[]
            data.remove(mid)
            for a in data:
                if a.w>=mid.w:
                    right.append(a)
                else:
                    left.append(a)
            return self.quicksort(left)+[mid]+self.quicksort(right)
```
然後可以從小到大（根據weight）進行路徑探索，同時防止閉環形成，
程式如下：
```python=
    def Kruskal(self):
        result=dict()
        g=self.graph
        arr=self.quicksort(g)
        if len(arr)==1:
            one=arr[0]
            f=str(one.b)+'-'+str(one.t)
            result[f]=one.w
            return result
        an=[]
        for n in arr:
            if n.b not in an:
                an.append(n.b)
            if n.t not in an:
                an.append(n.t)
        an=sorted(an)
        for n in range(len(an)):
            a=[an[n]]
            an[n]=a
        one=arr[0]
        two=arr[1]
        f=str(one.b)+'-'+str(one.t)
        s=str(two.b)+'-'+str(two.t)
        result[f]=one.w
        result[s]=two.w
        i=2
        an[one.b].append(one.t)
        an.remove(an[one.t])
        for n in range(len(an)):
            if two.b in an[n]:
                x=n
            if two.t in an[n]:
                y=n
        if x!=y:
            an[x].extend(an[y])
            an.remove(an[y])
        while len(an)!=1:
            for n in range(len(an)):
                if arr[i].b in an[n]:
                    x=n
                if arr[i].t in an[n]:
                    y=n
            if x!=y:
                an[x].extend(an[y])
                an.remove(an[y])
                t=str(arr[i].b)+'-'+str(arr[i].t)
                result[t]=arr[i].w
            else:
                i+=1
        return result
```
用課件中測資：
```
g=Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)

print("kruskal",g.Kruskal())
```
結果成功：
```
kruskal {'2-3': 4, '0-3': 5, '0-1': 10}
```           
## :three: 原理 :tiger2: 
 
| 1.Dijkstra程式碼解釋 |2.Dijkstra原理| 3. Kruskal程式碼解釋| 4.Kruskal原理|
| -------- | -------- | -------- |---|

### 1.Dijkstra程式碼解釋 
```python=
    def Dijkstra(self, s): 
        result=dict()
```
構建字典result存放結果
```python=
        e=str(s)
        result[e]=0
```
先將起點存入result中
```python=
        check=self.graph[s]
        quiz=[None]*len(check)
        for i in range(len(check)):
            quiz[i]=i+1
        quiz[s]=0
        need=[]
        need.append(s)
```
建立quiz(用以尋找第一的未處理的數的位置）、check（用以存放當前處理的距離）、need（用來判斷是否處理完畢）來做暫存處理
```python=
        while len(need)<(len(check)):
```
判斷是否已處理所用節點
```python=
            for t in range(len(quiz)):
                if quiz[t]!=0 and check[t]!=0:
                    z=t
                    break
                else:continue
```
尋找第一個未處理的節點的位置
```python=
            for i in range(len(check)):
                if quiz[i]!=0: 
                    if check[i]!=0 and check[z]>check[i] and z not in need:
                        z=i
```
尋找未處理且距離最小的節點的位置
```python=
            need.append(z)
            y=str(z)
            result[y]=check[z]
```
將找出的節點放入result，同時放入need
```python=
            check1=[]
            quiz[z]=0
```
check1為check的輔助變量，幫助check過度到下一階段；
在quiz中將處理完畢的節點的位置歸零
```python=
            for n in range(len(self.graph[z])):
                if self.graph[z][n]!=0:
                    p=result[y]+self.graph[z][n]
                    check1.append(p)
                else:
                    check1.append(0)
```
check1 為在加入新節點後的新距離列表
```python=
            for m in range(len(check)):
                if check[m]==0:
                    check[m]=check1[m]
                elif check1[m]!=0 and check1[m]<check[m]:
                    check[m]=check1[m]
                else:check[m]=check[m]
```
判斷check中各個距離，是否需要被check1中的相應位置的數代替
```python=
            for m in range(len(check)-1):
                if quiz[m]==0:
                    check[m]=0
```
判斷是否節點已處理，如已處理則歸零
```python=
        want=dict()
        for i in range(len(self.graph[0])):
            l=str(i)
            want[l]=result[l]
        return  want 
```
整理結果順序，讓結果依節點名稱按順序排列。

### 2.Dijkstra原理
一種最短路徑的算法
> 用於計算一個節點到其他所有節點的最短路徑。主要特點是以起始點為中心向外層層擴展，直到擴展到終點為止。Dijkstra演算法能得出最短路徑的最優解，但由於它遍曆計算的節點很多，所以效率低。可以用堆優化。

（引用自 https://baike.baidu.com/item/最短路径/6334920?fr=aladdin）

> 演算法思想：設G=(V,E)是一個帶權有向圖，把圖中頂點集合V分成兩組，第一組為已求出最短路徑的頂點集合（用S表示，初始時S中只有一個源點，以後每求得一條最短路徑 , 就將加入到集合S中，直到全部頂點都加入到S中，演算法就結束了），第二組為其餘未確定最短路徑的頂點集合（用U表示），按最短路徑長度的遞增次序依次把第二組的頂點加入S中。在加入的過程中，總保持從源點v到S中各頂點的最短路徑長度不大於從源點v到U中任何頂點的最短路徑長度。此外，每個頂點對應一個距離，S中的頂點的距離就是從v到此頂點的最短路徑長度，U中的頂點的距離，是從v到此頂點只包括S中的頂點為中間頂點的當前最短路徑長度。
> 
（引用自 https://blog.csdn.net/yalishadaa/article/details/55827681）

算法步驟如下：
> (1) 初始時，S只包含起點s；U包含除s外的其他頂點，且U中頂點的距離為"起點s到該頂點的距離"[例如，U中頂點v的距離為(s,v)的長度，然後s和v不相鄰，則v的距離為∞]。
(2) 從U中選出"距離最短的頂點k"，並將頂點k加入到S中；同時，從U中移除頂點k。
(3) 更新U中各個頂點到起點s的距離。之所以更新U中頂點的距離，是由於上一步中確定了k是求出最短路徑的頂點，從而可以利用k來更新其他頂點的距離；例如，(s,v)的距離可能大於(s,k)+(k,v)的距離。
(4) 重複步驟(2)和(3)，直到遍曆完所有頂點。

（引用自 https://blog.csdn.net/yalishadaa/article/details/55827681）

用於計算從一個節點到圖中所有節點的最短距離。
### 3. Kruskal程式碼解釋
首先編寫addEdge用以構建符合條件的關係圖，同時創造一個node結構以存放起終點和weight
```python=
    def addEdge(self,u,v,w): 
        new=node(u,v,w)
        self.graph.append(new)
```    
```python=
class node:
    def __init__(self,begin,target,weight):
        self.b=begin
        self.t=target
        self.w=weight
```
接下來開始編寫Kruskal：
```python=
    def Kruskal(self):
        result=dict()
```
創造字典result存放結果
```python=
        g=self.graph
        arr=self.quicksort(g)
```
先對所有邊依weight進行排序，
此處改寫HW1中的quicksort完成排序：
> ```python=
>    def quicksort(self,data):
>        if len(data)<2:
>             return data
>        else:
>             mid=data[len(data)-1]
>             left=[]
>             right=[]
>             data.remove(mid)
>             for a in data:
>                 if a.w>=mid.w:
>                     right.append(a)
>                 else:
>                     left.append(a)
>             return self.quicksort(left)+[mid]+self.quicksort(right)
> ```
(以下繼續Kruskal函數)
```python=
        if len(arr)==1:
            one=arr[0]
            f=str(one.b)+'-'+str(one.t)
            result[f]=one.w
            return result
```
只有兩個節點的情況
```python=
        an=[]
        for n in arr:
            if n.b not in an:
                an.append(n.b)
            if n.t not in an:
                an.append(n.t)
        an=sorted(an)
        for n in range(len(an)):
            a=[an[n]]
            an[n]=a
```
an用來放樹，以備後面防止迴圈產生
```python=
        one=arr[0]
        two=arr[1]
        f=str(one.b)+'-'+str(one.t)
        s=str(two.b)+'-'+str(two.t)
        result[f]=one.w
        result[s]=two.w
```
把前兩條邊放進result
```python=
        i=2
```
i為arr的位置
```python=
        an[one.b].append(one.t)
        an.remove(an[one.t])
        for n in range(len(an)):
            if two.b in an[n]:
                x=n
            if two.t in an[n]:
                y=n
        if x!=y:
            an[x].extend(an[y])
            an.remove(an[y])
```
判斷邊兩端節點是否在一棵樹中（是否在一個集合裡），如果不在一起，就放在一起，以下混圈中的相同操作的原理一樣
```python=
        while len(an)!=1:
```
直到所有節點都進入一個集合才停止（最小生成樹形成）
```python=
            for n in range(len(an)):
                if arr[i].b in an[n]:
                    x=n
                if arr[i].t in an[n]:
                    y=n
            if x!=y:
```
只有邊兩端的節點不在一個集合裡，才不會產生循環樹,才進行操作
```python=
                an[x].extend(an[y])
                an.remove(an[y])
                t=str(arr[i].b)+'-'+str(arr[i].t)
                result[t]=arr[i].w
            else:
                i+=1
```
否則，看下一條邊
```python=
        return result
```
完成後返回result。  
    
### 4.Kruskal原理
一種計算最小生成樹的算法
> 假設 WN=(V,{E}) 是一個含有 n 個頂點的連通網，則按照克魯斯卡爾演算法構造最小生成樹的過程為：先構造一個只含 n 個頂點，而邊集為空的子圖，若將該子圖中各個頂點看成是各棵樹上的根結點，則它是一個含有 n 棵樹的一個森林。之後，從網的邊集 E 中選取一條權值最小的邊，若該條邊的兩個頂點分屬不同的樹，則將其加入子圖，也就是說，將這兩個頂點分別所在的兩棵樹合成一棵樹；反之，若該條邊的兩個頂點已落在同一棵樹上，則不可取，而應該取下一條權值最小的邊再試之。依次類推，直至森林中只有一棵樹，也即子圖中含有 n-1條邊為止
> 
（引用自 https://baike.baidu.com/item/最小生成树/5223845?fr=aladdin）

步驟為：
> 1.對所有邊權進行排序。
2.如果最小邊的兩個端點不在一個連通圖中則將該邊佔領，否則則放棄。
3.結束條件：無可以插入邊或者總頂點數達到要求。

> 是基於邊權做的優化。

（引用自 https://www.jianshu.com/p/4377fa388ab9）

用最短路徑連接所有節點

## :four: 參考資料 :sheep: 

* https://www.cnblogs.com/skywang12345/p/3711496.html
* https://blog.csdn.net/sm20170867238/article/details/89988982
* https://github.com/yanjiyue/sac/blob/master/HW1/quicksort.ipynb
* https://blog.csdn.net/aivenzhong/article/details/93648557
* https://www.bilibili.com/video/av79186816?from=search&seid=17195856858988781128
* https://www.bilibili.com/video/av36884622/?spm_id_from=333.788.videocard.5
* https://www.bilibili.com/video/av36885495/?spm_id_from=333.788.videocard.2
* https://www.bilibili.com/video/av36884375?from=search&seid=718402740995726549
* https://www.bilibili.com/video/av26403085?from=search&seid=718402740995726549
* https://baike.baidu.com/item/最短路径/6334920?fr=aladdin
* https://blog.csdn.net/yalishadaa/article/details/55827681
* https://baike.baidu.com/item/最小生成树/5223845?fr=aladdin
* https://www.jianshu.com/p/4377fa388ab9
