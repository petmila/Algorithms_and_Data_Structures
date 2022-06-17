class Node():
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.balance = None
        self.right_height = None
        self.left_height = None
 
    def height(self):
        if self.balance is not None:
            return max(self.left_height, self.right_height) + 1
        if self.left is not None:
            left = self.left.height()
        else:
            left = 0
        if self.right is not None:
            right = self.right.height()
        else:
            right = 0
        self.balance = right - left
        self.right_height = right
        self.left_height = left
        return max(right, left) + 1
 
 
class Tree:
    def __init__(self):
        self.tree = [Node()]
 
    def add(self, value, left, right, index):
        my_node = Node()
        my_node.value = value
        if left != 0:
            my_node.left = left
        if right != 0:
            my_node.right = right
        self.tree.append(my_node)
        for node in self.tree:
            if index == node.left:
                node.left = my_node
                break
            if index == node.right:
                node.right = my_node
                break
 
    def print_balance(self, n):
        global result
        self.height(n)
        for node in range(1, len(self.tree)):
            result.append(str(self.tree[node].balance))
 
    def height(self, n):
        if n == 0:
            return 0
        sum = 0
        for node in range(len(self.tree) - 1, 0, -1):
            sum = self.tree[node].height()
 
 
fin = open('balance.in', 'r')
fout = open('balance.out', 'w')
n = int(fin.readline())
my_tree = Tree()
result = []
for i in range(n):
    get = fin.readline().split()
    my_tree.add(int(get[0]), int(get[1]), int(get[2]), i+1)
my_tree.print_balance(n)
fout.write('\n'.join(result))
fin.close()
fout.close()
