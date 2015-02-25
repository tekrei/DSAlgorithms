package net.tekrei.ds;

/**
 * Node for binary tree implementation
 * 
 * @author tekrei
 *
 * @param <AnyType>
 *            type of the data stored in it
 */
public class BTreeNode<AnyType> extends Node<AnyType> {

	private BTreeNode<AnyType> left;
	private BTreeNode<AnyType> right;

	public BTreeNode(AnyType info, BTreeNode<AnyType> _left,
			BTreeNode<AnyType> _right) {
		this.information = info;
		this.left = _left;
		this.right = _right;
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
