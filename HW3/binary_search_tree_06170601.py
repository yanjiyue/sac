class TreeNode(object):
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None            
        
class Solution(object):
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
        
            
    def search(self,node,item):#查
        if (node.val is None) or (item<node.val and node.left is None) or (item>node.val and node.right is None):return False
        elif node.val==item:
            print(True)
            return node
        elif item<=node.val:
            newnode=node.left
            return self.search(newnode,item)
        else:
            newnode=node.right
            return self.search(newnode,item)
        
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
