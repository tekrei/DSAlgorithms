#ifndef INCLUDES_BSTREE_H_
#define INCLUDES_BSTREE_H_

#include <cstddef>
#include <iostream>

template <class T>
class BSTree {
 private:
  class Node {
   public:
    T data;
    Node *left, *right;
    explicit Node(T val) : data(val), left(NULL), right(NULL) {}
  };

  Node *root;
  size_t size;
  Node *insert(T data, Node *node);
  Node *remove(T data, Node *node);
  Node *search(T data, Node *node);
  Node *findMin(Node *node);
  void inorder(Node *node);

 public:
  BSTree() : root(NULL), size(0) {}
  virtual ~BSTree<T>();
  bool isEmpty() const { return root == NULL; }
  void insert(T data);
  void remove(T data);
  Node *search(T data);
  void inorder();
  int getSize() { return size; }
};

template <class T>
BSTree<T>::~BSTree() {
  // traverse the tree and remove all elements
  while (root != NULL) {
    std::cout << "Removing " << root->data << std::endl;
    root = remove(root->data, root);
  }
  delete root;
  std::cout << "Destruction Complete!" << std::endl;
}

template <class T>
void BSTree<T>::insert(T data) {
  root = insert(data, root);
}

template <class T>
typename BSTree<T>::Node *BSTree<T>::insert(T data, Node *node) {
  if (node == NULL) {
    Node *temp = new Node(data);
    // increase size
    size++;
    return temp;
  } else {
    if (data < node->data) {
      node->left = insert(data, node->left);
    } else {
      node->right = insert(data, node->right);
    }
  }
  return node;
}

template <class T>
void BSTree<T>::remove(T data) {
  // calling remove with root
  root = remove(data, root);
  std::cout << "Removed " << data << std::endl;
}

template <class T>
typename BSTree<T>::Node *BSTree<T>::findMin(Node *node) {
  Node *current = node;
  while (current->left != NULL) {
    current = current->left;
  }
  return current;
}

template <class T>
typename BSTree<T>::Node *BSTree<T>::remove(T data, Node *node) {
  // modified from: http://geeksquiz.com/binary-search-tree-set-2-delete/
  if (node == NULL) return node;
  // element is on the left subtree
  if (data < node->data) {
    node->left = remove(data, node->left);
  } else if (data > node->data) {
    // element is on the right subtree
    node->right = remove(data, node->right);
  } else {
    // decrease size
    size--;
    // we've found the element
    // first case: node with only one child or no child
    if (node->left == NULL) {
      Node *temp = node->right;
      // free pointers first
      delete node;
      return temp;
    } else if (node->right == NULL) {
      Node *temp = node->left;
      delete node;
      return temp;
    }
    // second case: node with two children
    // get smallest from subtree
    Node *temp = findMin(node->right);
    node->data = temp->data;
    node->right = remove(temp->data, node->right);
  }
  return node;
}

template <class T>
typename BSTree<T>::Node *BSTree<T>::search(T data) {
  return search(data, root);
}

template <class T>
typename BSTree<T>::Node *BSTree<T>::search(T data, Node *node) {
  if (node->data == data) {
    return node;
  } else if (data < node->data) {
    return search(data, node->left);
  } else {
    return search(data, node->right);
  }
}

template <class T>
void BSTree<T>::inorder() {
  inorder(root);
}

template <class T>
void BSTree<T>::inorder(Node *node) {
  if (node == 0) {
    return;
  }
  inorder(node->left);
  std::cout << node->data << std::endl;
  inorder(node->right);
}

#endif  // INCLUDES_BSTREE_H_
