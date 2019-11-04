 class Solution(object):       
    def heap_sort(self,arr):
      end=len(arr)-1
      while end>=0:#運行直到所有節點都被抽出
        for start in range(len(arr)):
            self.good(arr,start,len(arr)-1)#開始一輪排序
        arr[0],arr[end]=arr[end],arr[0]#將末尾值與根互換，使最末值成為新根
        end-=1
      return arr
   
    def good(self,arr,start,end):
      root=start
      child=start+1
      while child<=end:
   #僅在子節點的位置在arr範圍之內時進行
        if child+1<=end and arr[child+1]<arr[child]:
        #若子節點的下一位小於子節點則互換；使root始終與較小值比較
           child+=1
        if arr[root]>arr[child]:
        #若root大於子節點，則互換位置與坐標，以保證root始終為最小值
           arr[root],arr[child]=arr[child],arr[root]
           root=child
           child=root+1
        else:break
