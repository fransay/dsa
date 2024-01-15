# Name: Francis Osei Annin
# Date: 10/11/23
# Description: AVL (self-balancing tree)

class Node(object):
    """Node in AVL tree"""

    def __init__(self, value):
        self.value = value 
        self.right = None
        self.left = None
        self.parent = None

    def is_leaf(self):
        """check if node is a leaf or not"""
        return True if self.right == None and self.left == None else False



class AVL(object):
    """Adelson Velsky Landis Tree"""

    def __init__(self):
        """init root node"""
        self.root = None
        self.root_position = 0
    
    def find(self, key):
        """find a key or item in the tree"""
        not_found = true
        current_node = self.root 
        while not current_node:
            if current_node.key == key: # root node
                self.root_position += 1
                return not not_found
            
            elif current_node.left < key: # go left
                curent_node = current_node.left

            else: 
                current_node = current_node.right
        return not_found 


    
    def insert(self, key):
        """insert node into tree"""
        # always check if the AVL tree property is maintained
        # if not perform some rotation

        # if a balance factor of a node is positive, then it is left heavy
        # if a balance factor of a node is negative, then it is right heavy

        new_node = Node(key)

        # treat root node as special case 
        if self.root is None:
            self.root = new_node

        current_node = self.root

        while current_node is not None:

            if key < current_node.key: # new node should be inserted into left subtree
                previous_node = current_node
                current_node = current_node.left

                if current_node is None:
                    current_node = new_node
                    previous_node = current_node.parent
                    # check to see if AVL property is maintained
                    # BF factor of each node in tree should be <=1 
                    # if not perform DS augmentation:: rotation
                    break
            elif key > current.key: # new node should be inserted into right subtree
                previous_node = current_node 
                current_node = current_node.right 

                if current_node is None:
                    current_node = new_node
                    previous_node = current_node.parent
                    # check to see if AVL property is maintained
                    # BF factor of each node in tree should be <=1 
                    # if not perform DS augmentation:: rotation
                    break
        return



    def remove(self, key):
        """remove node in tree"""
        # always check if AVL tree property is maintained
        # if not perform some rotation


        # test cases: node with no subtree (leaf)



        pass

    def depth_of_node(self, node):
        """return the depth of a node"""
        depth_counter = 0
        current_node = node
        while current_node is not self.root:
            current_node = current_node.parent
            depth_counter += 1
        return depth

    def height_of_node(self, node):
        """returns the height of a node"""
        height_counter = 0
        while node.left is not None and node.right is not None:
            height_counter += 1
        return height_counter
            
    
    def balance_factor(self, node):
        """return balance factor of a node"""
        # balance factor is the difference in the height of the right subtree and the left subtree
        diff =  self.height_of_node(node.right) - self.height_of_node(self.left)
        return diff


    def traverse_to_node(self, key):
        """traverse to the node in the tree with node.key == key"""
        pointer = None # start at the root node
        on_node = False

        if not self.root and self.root == key:
            pointer = self.root
            return

        current_node = self.root
        while not current_node:
            if not current_node.left:
                # check the if the left node is equal to the key
                current_node = current_node.left
                if self.match(current_node.key, key): on_node = true
                break 
            elif not current_node.right:
                # check the if the left right is equal to the key
                current_node = current_node.right
                if self.match(current_node.key, key): on_node = true
                break
        return on_node

    @staticmethod
    def match(item_one, item_two):
        """check if two items of the same value"""
        return true if item_one == item_two else false
