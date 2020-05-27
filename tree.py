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
        pass
    def _insert(self, data, cur_node):
        #TO Do
        pass
    def find(self, data):
        #To Do
        pass
    def _find(self, data, cur_node):
        #To do
        pass

bst = BST()
bst.insert()
print(bst.find())