/*
 * BSTree.cpp
 *
 *  Created on: May 25, 2015
 *      Author: tekrei
 */

#include "BSTree.h"

#include <iostream>
using namespace std;

template<class T>
BSTree<T>::~BSTree() {
	//traverse the tree and remove all elements
	while (root != NULL) {
		cout << "Removing " << root->data << endl;
		root = remove(root->data, root);
	}
	delete root;
	cout << "Destruction Complete!" << endl;
}

template<class T>
void BSTree<T>::insert(T data) {
	root = insert(data, root);
}

template<class T>
typename BSTree<T>::Node* BSTree<T>::insert(T data, Node *node) {
	if (node == NULL) {
		Node *temp = new Node(data);
		//increase size
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

template<class T>
void BSTree<T>::remove(T data) {
	//calling remove with root
	root = remove(data, root);
}

template<class T>
typename BSTree<T>::Node* BSTree<T>::findMin(Node* node) {
	Node* current = node;
	while (current->left != NULL) {
		current = current->left;
	}
	return current;
}

template<class T>
typename BSTree<T>::Node* BSTree<T>::remove(T data, Node *node) {
	//modified from: http://geeksquiz.com/binary-search-tree-set-2-delete/
	if (node == NULL)
		return node;
	//element is on the left subtree
	if (data < node->data) {
		node->left = remove(data, node->left);
	} else if (data > node->data) {
		//element is on the right subtree
		node->right = remove(data, node->right);
	} else {
		//decrease size
		size--;
		//we've found the element
		//first case: node with only one child or no child
		if (node->left == NULL) {
			Node* temp = node->right;
			//free pointers first
			delete node;
			return temp;
		} else if (node->right == NULL) {
			Node* temp = node->left;
			delete node;
			return temp;
		}
		//second case: node with two children
		//get smallest from subtree
		Node* temp = findMin(node->right);
		node->data = temp->data;
		node->right = remove(temp->data, node->right);
	}
	return node;
}

template<class T>
typename BSTree<T>::Node* BSTree<T>::search(T data) {
	return search(data, root);
}

template<class T>
typename BSTree<T>::Node* BSTree<T>::search(T data, Node *node) {
	if (node->data == data) {
		return node;
	} else if (data < node->data) {
		return search(data, node->left);
	} else {
		return search(data, node->right);
	}
}

template<class T>
void BSTree<T>::inorder() {
	inorder(root);
}

template<class T>
void BSTree<T>::inorder(Node *node) {
	if (node == 0) {
		return;
	}
	inorder(node->left);
	cout << node->data << endl;
	inorder(node->right);
}

int main() {
	BSTree<float> tree;
	for (int i = 0; i < 10; i++) {
		tree.insert((float)i/10.0);
	}
	tree.inorder();
	cout << "Current size:" << tree.getSize() << endl;
	tree.remove(5);
	tree.remove(9);
	tree.remove(0);
	cout << "Current size:" << tree.getSize() << endl;
	tree.inorder();
	tree.remove(8);
	cout << "Current size:" << tree.getSize() << endl;
	delete &tree;
	return 0;
}
