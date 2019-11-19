class Solution(object):
    def insert(self,root,item):#新增
        if root==[]:
            node=[item,[],[]]
            root.extend(node)
            return root
        else:     
            if item<=root[0]:
                newr=root[1]
                if len(newr)<1:
                    node=[item,[],[]]
                    root[1].extend(node)
                else:
                    self.insert(newr,item)
            else:
                newr=root[2]
                if len(newr)<1:
                    node=[item,[],[]]
                    root[2].extend(node)
                else:
                    self.insert(newr,item)
        return root
       
        
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
    
    def delete(self,root,item):#刪除
        c=0
        check=[]
        a=self.preorder(root,check)
        for i in range(len(a)-1):
                if a[i]==item:
                    c+=1
        if len(a)<1:
            return False
        elif len(a)==1:
            if root[0]!=item:
                return root
            else:
                root.clear()
        else:
            if c==0:
                return False
            else:
                self.delhelp(root,item)
                while c>=0:
                    self.delhelp(root,item)
                    c-=1
          
    def delhelp(self,root,item):
        if root==[] or (item<root[0] and root[1]==[]) or (item>root[0] and root[2]==[]):            
                return False     
        elif item==root[0]:
            if root[1]==[] and root[2]==[]:
                root.clear()
            elif root[1]==[]:
                root[:]=root[2]
            elif root[2]==[]:
                root[:]=root[1]
            else:
                max=self.getmax(root[1])
                root[0]=max
        elif item<root[0]:
            return self.delhelp(root[1],item)
        else:
            return self.delhelp(root[2],item)
       
        
    def getmax(self,root):
        if root[2]==[]:
            m=root[0]
            if root[1]==[]:
                root.clear()
            else:
                root[:]=root[1]
            return m
        else:return getmax(root[2])
        
    def preorder(self, root,check):  #先序遍歷    
        if root==[]:            
            return []        
        check.append(root[0])
        checkl=[]
        checkr=[]
        check.extend(self.preorder(root[1],checkl))
        check.extend(self.preorder(root[2],checkr))
        return check
    
    def modify(self,root,item,change):#修改
        if root==[]:
            return False
        c=0
        check=[]
        a=self.preorder(root,check)
        for i in range(len(a)):
                if a[i]==item:
                    c+=1
                    a[i]=change 
                else:
                    a[i]=a[i]
        if c<=0:
            return False
        else:
            result=[]
            for n in range(len(a)):
                m=a[n]
                self.insert(result,m)
            return result
