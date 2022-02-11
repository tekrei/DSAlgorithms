package net.ds;

/**
 * Node for binary tree implementation
 * 
 *
 * @param <AnyType>
 *                  type of the data stored in it
 */
public class BTreeNode<AnyType> extends Node<AnyType> {

	private BTreeNode<AnyType> left;
	private BTreeNode<AnyType> right;

	private int height;

	public int getHeight() {
		return height;
	}

	public void setHeight(int height) {
		this.height = height;
	}

	public BTreeNode(AnyType _info, BTreeNode<AnyType> _left,
			BTreeNode<AnyType> _right, int _height) {
		this.information = _info;
		this.left = _left;
		this.right = _right;
		this.height = _height;
	}

	public BTreeNode(AnyType _info, BTreeNode<AnyType> _left,
			BTreeNode<AnyType> _right) {
		this(_info, _left, _right, 0);
	}

	public BTreeNode(AnyType info) {
		this(info, null, null);
	}

	public BTreeNode() {
		this(null, null, null);
	}

	public BTreeNode<AnyType> getLeft() {
		return left;
	}

	public void setLeft(BTreeNode<AnyType> left) {
		this.left = left;
	}

	public BTreeNode<AnyType> getRight() {
		return right;
	}

	public void setRight(BTreeNode<AnyType> right) {
		this.right = right;
	}

}
