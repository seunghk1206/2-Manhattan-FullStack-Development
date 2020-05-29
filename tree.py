"""
Binary Tree => Binary Search Tree
    1. Each node has at most 2 children nodes
    2. Left node is always less than the right node

Insertion 할때
    1. balanced Tree => insert: O(log n), search: O(log n)
    2. Unbalanced Tree => insert: O(n), search: O(log n)

preorder & inorder & postorder

Insert
[8, 3, 10, 1, 6]
    1. 8 이 root node 가 됨
    2. 3은 8보다 작으므로 Left node
    3. 10은 8보다 큼으로 right node

Search:
    1. Root Node 에서 시작을 한다
    2. Inorder 형식 또는 Binary Search 의 having 형식으로 값을 찾는다
"""
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        #TO DO
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    def _insert(self, data, cur_node):
        #TO Do
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
    def find(self, data):
        #To Do
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return False
    def _find(self, data, cur_node):
        #To do
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

bst = BST()
for n in range(1, 500):
    bst.insert(n)
print(bst.find(0))