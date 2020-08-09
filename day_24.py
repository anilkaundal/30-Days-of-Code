import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here 
        for i in range(1, T+1): 
            self.GivenLevel(root, i)
            
    def GivenLevel(self, root , level): 
        if root is None: 
            return
        if level == 1: 
            print(root.data,end=" ") 
        elif level > 1 : 
            self.GivenLevel(root.left , level-1) 
            self.GivenLevel(root.right , level-1) 

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
