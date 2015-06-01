/*
 * BSTree.h
 *
 *  Created on: May 25, 2015
 *      Author: tekrei
 */

#ifndef BST_BSTREE_H_
#define BST_BSTREE_H_

#include <iostream>

template<class T>
class BSTree {
private:
	class Node {
		public:
			T data;
			Node *left, *right;
			Node(T val) :
				data(val), left(NULL), right(NULL) {
			}
	};
	Node *root;
	size_t size;
	Node *insert(T data, Node *node);
	Node *remove(T data, Node *node);
	Node *search(T data, Node *node);
	Node *findMin(Node *node);
	void inorder(Node *node);
public:
	BSTree() :
			root(NULL), size(0) {
	}
	virtual ~BSTree<T>();
	bool isEmpty() const {
		return root == NULL;
	}
	void insert(T data);
	void remove(T data);
	Node *search(T data);
	void inorder();
	int getSize() {
		return size;
	}
};

#endif /* BST_BSTREE_H_ */
