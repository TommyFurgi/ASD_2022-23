# Binary search tree

class Node():
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None
        self.data=None


    def search(root,value):
        while root!=None:
            if root.key==value:
                return root
            elif root.key>value:
                root=root.left
            else:
                root=root.right

        return None
    
    def insert(root,value):
        if root==None:
            new=Node(value)
            return new

        while root!=None:
            if root.key==value:
                return 
            elif root.key>value:
                prev=root
                root=root.left
            else:
                prev=root
                root=root.right

        new=Node(value)
        new.parent=prev
        if prev.key>value:
            prev.left=new
        else:
            prev.right=new

        return 
    
    def min(root):
        while root!=None:
            if root.left!=None:
                root=root.left
            else:
                return root

        return None
    
    def max(root):
        while root!=None:
            if root.right!=None:
                root=root.right
            else:
                return root

        return None
    
    def pred(root,value): # predecessor
        node=Node.search(root,value)
        if node==None:
            return None

        if node.left!=None:
            return Node.max(node.left)

        else:
            curr=node.parent
            if curr==None:
                return None
            
            if curr.right==node:
                return curr


            while curr!=None and curr.left==node:
                node=curr
                curr=curr.parent

            return curr

    def succ(root,value): # successor
        node=Node.search(root,value)
        if node==None:
            return None

        if node.right!=None:
            return Node.min(node.right)

        else:
            curr=node.parent
            if curr==None:
                return None
            
            if curr.left==node:
                return curr


            while curr!=None and curr.right==node:
                node=curr
                curr=curr.parent

            return curr

    def remove(root,value):
        node=Node.search(root,value)
        if node.parent==None:
            if root.left==None and root.right==None:
                return None
            elif root.left==None:
                node=root.right
                root.right=None
                node.parent=None
                del(root)
                return node
            elif root.right==None:
                node=root.left
                root.left=None
                node.parent=None
                del(root)
                return node
            else:
                successor = Node.succ(root, node.key)
                node.key = successor.key
                Node.remove(successor, successor.key)
                return root



        p=node.parent
        node.parent=None
        if node.right==None and node.left==None:
            if p.right==node:
                p.right=None
            else:
                p.left=None

        elif node.right==None:
            if p.right==node:
                p.right=node.left
            else:
                p.left=node.left
        
        elif node.left==None:
            if p.right==node:
                p.right=node.right
            else:
                p.left=node.right

        else:
            successor = Node.succ(root, node.key)
            node.key = successor.key
            Node.remove(successor, successor.key)

        
        del(node)
        return root

    def create(T):
        root=Node(T[0])
        for i in range(1,len(T)):
            Node.insert(root,T[i])
        
        return root
    
T=[50,25,75,12,37,60,100]
root=Node.create(T)
#          50
#       /     \
#      25      75
#     /  \    /  \
#   12   37  60   100
# s=Node.pred(root,50)
root=Node.remove(root,50)
print()