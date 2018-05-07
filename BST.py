class TreeNode:
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None

        

class SearchTree:
    
    def __init__(self):
        self.root = None
    def return_root(self):
        return self.root
        
    def insert(self,x):
        if not self.root:
            self.root = TreeNode(x)
        else:
            self.add(x,self.root)
    def add(self,x,current_node):
        if  x < current_node.val:
            if not current_node.left:
                current_node.left = TreeNode(x)
            else:
                self.add(x,current_node.left)
        else:
            if not current_node.right:
                current_node.right = TreeNode(x)
            else:
                self.add(x,current_node.right)
    def show(self):
        
        tre = []
        q = Queue()
        q.add([self.root,0])
        
        while q.nonempty():
            current = q.peek()
            if current[0]:
                tre.append([current[0].val,current[1]])
                q.add([current[0].left,current[1] + 1])
                q.add([current[0].right,current[1]+1])
            q.remove()
        
        return tre
    def search(self,x):
        if self.root:
            if self.root.val == x:
                print ("It's the root")
            else:
                return self.searchNode(x,self.root)
    def searchNode(self,x,current_node):
        if x == current_node.val:
            print("Found")
        if x < current_node.val:
            print("left")
            self.searchNode(x,current_node.left)
        if x > current_node.val:
            print("right")
            self.searchNode(x,current_node.right)
            
    def query(self,x):
        if self.root:
            if self.root.val == x:
                return True
            else:
                return self.queryNode(x,self.root)
        
    def queryNode(self,x,current_node):
        if current_node is None:
            return False
        if x == current_node.val:
            return True
        if x < current_node.val:
            return self.queryNode(x,current_node.left)
        if x > current_node.val:
            return self.queryNode(x,current_node.right)