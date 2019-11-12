class Solution(object):
    def merge_sort(self,mylist):
        if len(mylist)<=1:
            return mylist
        n=len(mylist)//2#分為左右臨近的兩塊
        left=mylist[:n]
        right=mylist[n:]
        return self.merge(self.merge_sort(left),self.merge_sort(right))#分別再對左右兩塊進行各自的左右分塊


    def merge(self,left,right):
        r,l=0,0
        result=[]
        while l<len(left) and r<len(right):#left中的數分別與right中的數進行比較、插入
            if left[l]<=right[r]:#由於list內部已是比過大小的，所以若left第一個值小於right第一個值，則必定小於right中其他值，則無需再比較
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
        result.extend(left[l:])
        result.extend(right[r:])#將剩餘的數加回結果list後，防止值的丟失

        return result
