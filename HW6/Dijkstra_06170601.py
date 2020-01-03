from collections import defaultdict 

class node:
    def __init__(self,begin,target,weight):
        self.b=begin
        self.t=target
        self.w=weight
        
class Graph(): 
    

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        new=node(u,v,w)
        self.graph.append(new)
    
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

"""
https://www.cnblogs.com/skywang12345/p/3711496.html
https://blog.csdn.net/sm20170867238/article/details/89988982
https://github.com/yanjiyue/sac/blob/master/HW1/quicksort.ipynb
https://blog.csdn.net/aivenzhong/article/details/93648557
https://www.bilibili.com/video/av79186816?from=search&seid=17195856858988781128
https://www.bilibili.com/video/av36884622/?spm_id_from=333.788.videocard.5
https://www.bilibili.com/video/av36885495/?spm_id_from=333.788.videocard.2
https://www.bilibili.com/video/av36884375?from=search&seid=718402740995726549
https://www.bilibili.com/video/av26403085?from=search&seid=718402740995726549
https://baike.baidu.com/item/最短路径/6334920?fr=aladdin
https://blog.csdn.net/yalishadaa/article/details/55827681
https://baike.baidu.com/item/最小生成树/5223845?fr=aladdin
https://www.jianshu.com/p/4377fa388ab9
"""
