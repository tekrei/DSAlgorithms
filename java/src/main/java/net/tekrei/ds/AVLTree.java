package net.tekrei.ds;

/**
 * Implementation of AVL Tree - A balanced BST
 * 
 * @author tekrei
 *
 * @param <AnyType>
 * 
 * @see <a
 *      href="https://en.wikipedia.org/wiki/AVL_tree">https://en.wikipedia.org/wiki/AVL_tree</a>
 */

public class AVLTree<AnyType extends Comparable<AnyType>> extends
		BinarySearchTree<AnyType> {

	private static final int ALLOWED_IMBALANCE = 1;

	@Override
	public void insert(AnyType info) {
		root = insert(info, root);
	}

	@Override
	public void remove(AnyType info) {
		root = remove(info, root);
	}

	private BTreeNode<AnyType> remove(AnyType info, BTreeNode<AnyType> node) {
		if (node == null)
			return node; // Item not found; do nothing

		int compareResult = info.compareTo(node.getInfo());

		if (compareResult < 0)
			node.setLeft(remove(info, node.getLeft()));
		else if (compareResult > 0)
			node.setRight(remove(info, node.getRight()));
		else if (node.getLeft() != null && node.getRight() != null) // Two children
		{
			node.setInfo(findMin(node.getRight()).getInfo());
			node.setRight(remove(node.getInfo(), node.getRight()));
		} else
			node = (node.getLeft() != null) ? node.getLeft() : node.getRight();
		return balance(node);
	}

	private BTreeNode<AnyType> insert(AnyType info, BTreeNode<AnyType> node) {
		if (node == null)
			return new BTreeNode<AnyType>(info, null, null);

		int compareResult = info.compareTo(node.getInfo());

		if (compareResult < 0) {
			node.setLeft(insert(info, node.getLeft()));
		} else if (compareResult > 0) {
			node.setRight(insert(info, node.getRight()));
		} else {
			// duplicate
		}
		return balance(node);
	}

	private BTreeNode<AnyType> balance(BTreeNode<AnyType> node) {
		if (node == null)
			return node;

		if (height(node.getLeft()) - height(node.getRight()) > ALLOWED_IMBALANCE) {
			if (height(node.getLeft().getLeft()) >= height(node.getLeft()
					.getRight())) {
				node = rotateWithLeftChild(node);
			} else {
				node = doubleWithLeftChild(node);
			}
		} else if (height(node.getRight()) - height(node.getLeft()) > ALLOWED_IMBALANCE) {
			if (height(node.getRight().getRight()) >= height(node.getRight()
					.getLeft())) {
				node = rotateWithRightChild(node);
			} else {
				node = doubleWithRightChild(node);
			}
		}
		node.setHeight(Math.max(height(node.getLeft()), height(node.getRight())) + 1);
		return node;
	}

	private BTreeNode<AnyType> rotateWithLeftChild(BTreeNode<AnyType> node) {
		BTreeNode<AnyType> left = node.getLeft();
		node.setLeft(left.getRight());
		left.setRight(node);
		node.setHeight(Math.max(height(node.getLeft()), height(node.getRight())) + 1);
		left.setHeight(Math.max(height(left.getLeft()), node.getHeight()) + 1);
		return left;
	}

	private BTreeNode<AnyType> doubleWithLeftChild(BTreeNode<AnyType> node) {
		node.setLeft(rotateWithRightChild(node.getLeft()));
		return rotateWithLeftChild(node);
	}

	private BTreeNode<AnyType> rotateWithRightChild(BTreeNode<AnyType> node) {
		BTreeNode<AnyType> right = node.getRight();
		node.setRight(right.getLeft());
		right.setLeft(node);
		node.setHeight(Math.max(height(node.getLeft()), height(node.getRight())) + 1);
		right.setHeight(Math.max(height(right.getRight()), node.getHeight()) + 1);
		return right;
	}

	private BTreeNode<AnyType> doubleWithRightChild(BTreeNode<AnyType> node) {
		node.setRight(rotateWithLeftChild(node.getRight()));
		return rotateWithRightChild(node);
	}

	public void checkBalance() {
		checkBalance(root);
	}

	private int checkBalance(BTreeNode<AnyType> node) {
		if (node == null)
			return -1;

		if (node != null) {
			int hl = checkBalance(node.getLeft());
			int hr = checkBalance(node.getRight());
			if (Math.abs(height(node.getLeft()) - height(node.getRight())) > 1
					|| height(node.getLeft()) != hl || height(node.getRight()) != hr)
				System.out.println("Unbalanced!");
		}

		return height(node);
	}
}
