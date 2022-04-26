
import time


class Node():
    def __init__(self, value):
        self.value = value
        self.color = 'R'  # R represents red as we always insert a new node as red
        self.parent = None
        self.left = None
        self.right = None


class RBtree():
    def __init__(self):  # this constructor creates an empty RB tree
        self.nil = Node(' ')  # null node
        self.nil.color = 'B'  # an empty tree has nil which is black
        self.nil.parent = None
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil  # root is null

    def fixRBtree(self, node):
        # base case 1: if node is root, make it black then it's fixed
        if node == self.root:
            node.color = 'B'
            return
        # base case 2: if node's parent is black (or root), do nothing
        if node.parent.color == 'B':
            return

        if node.parent.color == 'R':
            # find uncle node
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
            else:
                uncle = node.parent.parent.left

            # case 1: uncle red, recolor then recursively fix the grandparent
            if uncle.color == 'R':
                uncle.color = 'B'
                node.parent.color = 'B'
                node.parent.parent.color = 'R'
                self.fixRBtree(node.parent.parent)
            else:
                # case 2.1: left left, swap colors of p and g then rotateRight g
                if node.parent == node.parent.parent.left and node == node.parent.left:
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotateRight(node.parent.parent)
                # case 2.2: right right, swap colors of p and g then rotateLeft g
                elif node.parent == node.parent.parent.right and node == node.parent.right:
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotateLeft(node.parent.parent)
                # case 3.1: left right, rotateLeft p, then move to case 2.1 with (node) as the new p
                elif node.parent == node.parent.parent.left and node == node.parent.right:
                    self.rotateLeft(node.parent)
                    node.color = 'B'
                    node.parent.color = 'R'
                    self.rotateRight(node.parent)
                # case 3.2: right left, rotateRight p, then move to case 2.2 with (node) as the new p
                else:
                    self.rotateRight(node.parent)
                    node.color = 'B'
                    node.parent.color = 'R'
                    self.rotateLeft(node.parent)

    def rotateLeft(self, node):
        p = node.right
        node.right = p.left  # right child of grandparent is left child of parent, if any
        if p.left != self.nil:
            p.left.parent = node
        p.parent = node.parent
        if node.parent == None:  # node was root
            self.root = p
            node.parent = p

        elif node == node.parent.left:  # if node was a left child then make p the new left
            node.parent.left = p
            node.parent = p

        else:
            node.parent.right = p
            node.parent = p
        p.left = node

    def rotateRight(self, node):
        p = node.left
        node.left = p.right
        if p.right != self.nil:
            p.right.parent = node
        p.parent = node.parent
        if node.parent == None:  # node was root
            self.root = p
            node.parent = p

        elif node.parent.left == node:  # if node was a left child then make p the new left
            node.parent.left = p
            node.parent = p

        else:
            node.parent.right = p
            node.parent = p
        p.right = node

    def insert(self, value):
        newNode = Node(value)  # init new node
        newNode.left = self.nil  # left child is a nil
        newNode.right = self.nil  # right child is a nil
        x = self.root
        parent = None  # keeps track of inserted node's parent

        # loop until parent is found
        while x != self.nil:
            parent = x
            if newNode.value < x.value:
                x = x.left
            elif newNode.value > x.value:
                x = x.right
        newNode.parent = parent
        if parent == None:  # root
            self.root = newNode
        elif newNode.value < parent.value:
            parent.left = newNode  # modify parent's left child to point to inserted node
        else:
            parent.right = newNode  # modify parent's right child to point to inserted node
        # if newNode.parent.parent == None: #newNode's parent is root, no fixing required
            # return
        self.fixRBtree(newNode)

    def search(self, root, key):
        if root == self.nil:  # tree is empty
            return False

        if root.value == key:
            return True

        if key < root.value:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def RBheight(self, root):  # no. of edges
        if root == self.nil:  # tree is empty
            return -1
        else:
            return 1 + max(self.RBheight(root.left), self.RBheight(root.right))

    def RBsize(self, root):
        if root == self.nil:  # tree is empty, 0 elements
            return 0
        else:
            return 1 + self.RBsize(root.left) + self.RBsize(root.right)


def loadDictionary(name):
    rbt = RBtree()
    try:
        f = open(name, "r")
        words = f.read()
        word = words.splitlines()  # list of dictionary words
        for i in range(0, len(word)):
            rbt.insert(word[i])
        f.close()
        print("Dictionary loaded successfully!")
        return rbt
    except FileNotFoundError:
        print("File not found!!")
        return None


def interface():
    run = True
    a = input(
        "Choose an action:\n1. Enter a separate dictionary path\n2. Use the default dictionary\n")
    if a == '1':
        file = input("Enter path of dictionary: ")
        rbtree = loadDictionary(file)
    else:
        rbtree = loadDictionary('EN-US-Dictionary.txt')
    if rbtree != None:
        print("Size of Dictionary = " + str(rbtree.RBsize(rbtree.root)))
        print("Height of Dictionary = " + str(rbtree.RBheight(rbtree.root)))
        while(run):
            choice = input(
                "Choose an action:\n1. Insert a word in the dictionary\n2. Lookup a word\n3. Exit\n")
            if choice == '1':
                word = input("Enter the word to be inserted: ")
                if rbtree.search(rbtree.root, word) == True:
                    print("ERROR: Word is already in the dictionary! ")
                else:
                    rbtree.insert(word)
                    print("New Size of Dictionary = " +
                          str(rbtree.RBsize(rbtree.root)))
                    print("New Height of Dictionary = " +
                          str(rbtree.RBheight(rbtree.root)))

            elif choice == '2':
                word = input("Enter a word to lookup: ")
                if rbtree.search(rbtree.root, word) == True:
                    print("FOUND!")
                else:
                    print("NOT FOUND!!")

            elif choice == '3':
                run = False

            else:
                print("INVALID CHOICE, please try again!")
                time.sleep(1)


interface()
