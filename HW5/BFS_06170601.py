from collections import defaultdict 
  
class Graph:
   
    def __init__(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        result=[]
        result.append(s)
        arr=self.graph[s]
        while arr:  
            m=arr[0]
            arr=arr[1:]
            if m not in result:
                result.append(m)
                arr=self.take(arr,m)             
        return result
    
    def take(self,l,a):
        arr=self.graph[a]
        for i in range(len(arr)):
            if arr[i] not in l:
                l.append(arr[i])
        return l
    
    def DFS(self, s):
        result=[]
        result.append(s)
        stack=self.graph[s]
        while stack:
            x=len(stack)-1
            m=stack[x]
            stack=stack[:-1]
            if m not in result:
                result.append(m)
                stack=self.take(stack,m)
        return result
#https://baike.baidu.com/item/宽度优先搜索/5224802?fromtitle=BFS&fromid=542084&fr=aladdin

#https://www.cnblogs.com/wzl19981116/p/9397203.html

#https://blog.csdn.net/qq_41759198/article/details/81510147

#https://www.bilibili.com/video/av12019553?from=search&seid=11049328282069570805

#https://www.bilibili.com/video/av21521491?from=search&seid=11049328282069570805

#https://www.bilibili.com/video/av25761720?from=search&seid=11049328282069570805

#https://www.bilibili.com/video/av41856043?from=search&seid=11049328282069570805

#https://www.bilibili.com/video/av25763384?from=search&seid=11049328282069570805

#https://www.bilibili.com/video/av25829980?from=search&seid=11049328282069570805

#https://baike.baidu.com/item/深度优先搜索/5224976?fromtitle=DFS&fromid=5055&fr=aladdin

#https://www.cnblogs.com/wzl19981116/p/9397203.html
