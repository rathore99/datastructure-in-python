''' main operations 
1. insert()
2. delete()
3. Find()
4. traverse()
   i) inorder
   ii) preorder
   iii) postorder
'''
class Tree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left

    def insert(self, data):
        #check duplicate
        if self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = Tree(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Tree(data)
    
    def preorder(self):
        if self is not None:
            print(self.data , end = " ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end =" ")
            if self.right is not None:
                self.right.inorder()

    def postorder(self):
        if self is not None:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.data, end =' ')    

tree = Tree(4)
for i in [3,4,5,1,7,6]:
    tree.insert(i)
    print('preorder:', end = " ")
    tree.preorder()
    print()
    print('inorder:', end = " ")
    tree.inorder()
    print()
    print('postorder:', end = " ")
    tree.postorder()
    print()
