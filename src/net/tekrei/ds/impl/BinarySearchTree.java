package net.tekrei.ds.impl;

import net.tekrei.ds.BTreeNode;

/**
 * Binary search tree implementation
 * 
 * @author tekrei
 *
 * @param <AnyType>
 *            type of the data stored in it
 * 
 *            For more information @see {@linktourl
 *            https://en.wikipedia.org/wiki/Binary_search_tree}
 */
public class BinarySearchTree<AnyType extends Comparable<AnyType>> {

	BTreeNode<AnyType> root;
	private int size = 0;

	public BTreeNode<AnyType> find(AnyType info) {
		// TODO not implemented yet
		return null;
	}

	public void remove(AnyType info) {
		root = remove(info, root);
	}

	private BTreeNode<AnyType> remove(AnyType info, BTreeNode<AnyType> node) {
		if (node == null)
			return node;
		int comparison = info.compareTo(node.getInfo());
		if (comparison < 0) {
			node.setLeft(remove(info, node.getLeft()));
		} else if (comparison > 0) {
			node.setRight(remove(info, node.getRight()));
		} else if (node.getLeft() != null && node.getRight() != null) {
			node.setInfo(findMin(node.getRight()).getInfo());
			node.setRight(remove(node.getInfo(), node.getRight()));
		} else {
			node = (node.getLeft() != null) ? node.getLeft() : node.getRight();
		}
		return node;
	}

	public void insert(AnyType info) {
		root = insert(info, root);
	}

	/**
	 * Currently works as a set, doesn't insert duplicates
	 * 
	 * @param info
	 * @param node
	 * @return
	 */
	private BTreeNode<AnyType> insert(AnyType info, BTreeNode<AnyType> node) {
		if (node == null) {
			size++;
			return new BTreeNode<AnyType>(info, null, null);
		}
		int comparison = info.compareTo(node.getInfo());
		if (comparison == -1) {
			// add to the left tree
			node.setLeft(insert(info, node.getLeft()));
		} else if (comparison == 1) {
			// add to the right tree
			node.setRight(insert(info, node.getRight()));
		}
		return node;
	}

	private BTreeNode<AnyType> findMin(BTreeNode<AnyType> node) {
		// TODO not implemented yet
		return null;
	}

	public boolean contains(AnyType info) {
		// TODO not implemented yet
		return false;
	}

	public boolean isEmpty() {
		return (size == 0);
	}

	public int size() {
		return size;
	}

	public String inorderTraversal() {
		String str = "INORDER:[";
		str += inorder(root);
		return str + "]";
	}

	public String postorderTraversal() {
		String str = "POSTORDER:[";
		str += postorder(root);
		return str + "]";
	}

	public String preorderTraversal() {
		String str = "PREORDER:[";
		str += preorder(root);
		return str + "]";
	}

	private String inorder(BTreeNode<AnyType> node) {
		String str = "";
		if (node == null)
			return str;
		str += inorder(node.getLeft());
		str += node.getInfo() + " ";
		str += inorder(node.getRight());
		return str;
	}

	private String postorder(BTreeNode<AnyType> node) {
		String str = "";
		if (node == null)
			return str;
		str += postorder(node.getLeft());
		str += postorder(node.getRight());
		str += node.getInfo() + " ";
		return str;
	}

	private String preorder(BTreeNode<AnyType> node) {
		String str = "";
		if (node == null)
			return str;
		str += node.getInfo() + " ";
		str += preorder(node.getLeft());
		str += preorder(node.getRight());
		return str;
	}

	public String toString() {
		return inorderTraversal();
	}

}
