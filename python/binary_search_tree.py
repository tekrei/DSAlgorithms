"""
Created on May 16, 2015
"""
import random
from typing import Type


class Node(object):
    def __init__(self, data: any, left: object, right: object):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree(object):
    """
    Binary Search Tree implementation
    """

    def __init__(self):
        """
        Constructor
        """
        self.root = None

    def _find(self, node: Type[Node], data: any):
        """
        find helper
        """
        if node == None or node.data == data:
            return node
        elif data < node.data:
            return self._find(node.left, data)
        else:
            return self._find(node.right, data)

    def find(self, data: any):
        """
        find data in BST
        """
        return self._find(self.root, data)

    def insert(self, data: any):
        """
        insert new element to the BST
        """
        self.root = self._insert(self.root, data)

    def _insert(self, node: Type[Node], data: any):
        """
        recursive insert helper
        """
        if node is None:
            return Node(data, None, None)
        if data == node.data:
            return Node(data, node.left, node.right)
        if data < node.data:
            return Node(node.data, self._insert(node.left, data), node.right)
        else:
            return Node(node.data, node.left, self._insert(node.right, data))

    def lookup(self, node: Type[Node], data: any, parent=None):
        """
        Lookup node containing data

        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < node.data:
            if node.left is None:
                return None, None
            return self.lookup(node.left, data, node)
        elif data > node.data:
            if node.right is None:
                return None, None
            return self.lookup(node.right, data, node)
        else:
            return node, parent

    def children_count(self, node: Type[Node]):
        """
        Returns the number of children for a given node
        @returns number of children: 0, 1, 2
        """
        count = 0
        if node.left:
            count += 1
        if node.right:
            count += 1
        return count

    def delete(self, data: any):
        """
        Delete node containing data
        @param data node's content to delete
        Source: https://gist.github.com/NahimNasser/4705371
        """
        node, parent = self.lookup(self.root, data)
        if node:
            children_count = self.children_count(node)
            if children_count == 0:
                # If node has no children then remove it
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                if node.left:
                    child = node.left
                else:
                    child = node.right
                if parent:
                    if parent.left is node:
                        parent.left = child
                    else:
                        parent.right = child
                del node
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def _inorder(self, node: Type[Node], datalist: list):
        """
        inorder traversal helper function
        """
        if node == None:
            return
        self._inorder(node.left, datalist)
        datalist.append(str(node.data))
        self._inorder(node.right, datalist)

    def inorder(self):
        """
        inorder traversal
        """
        datalist = []
        self._inorder(self.root, datalist)
        return datalist

    def __str__(self):
        datalist = self.inorder()
        strrep = "["
        for current in datalist:
            strrep += current + ", "
        return strrep[:-2] + "]"


if __name__ == "__main__":
    bst = BinarySearchTree()
    numbers = [random.randint(0, 25) for x in range(10)]
    print(numbers)
    for n in numbers:
        bst.insert(n)
    bst.insert(12)
    bst.insert(6)
    print(bst)
    bst.delete(6)
    bst.delete(12)
    print(bst)
