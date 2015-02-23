package net.tekrei.ds;

/**
 * Node for binary tree implementation
 * 
 * @author tekrei
 *
 * @param <AnyType>
 */
public class BTreeNode<AnyType> extends Node<AnyType> {

	private BTreeNode<AnyType> left;
	private BTreeNode<AnyType> right;
	private BTreeNode<AnyType> parent;

	public BTreeNode(AnyType info, BTreeNode<AnyType> _left,
			BTreeNode<AnyType> _right, BTreeNode<AnyType> _parent) {
		this.information = info;
		this.left = _left;
		this.right = _right;
		this.parent = _parent;
	}

	public BTreeNode(AnyType info, BTreeNode<AnyType> _left,
			BTreeNode<AnyType> _right) {
		this(info, _left, _right, null);
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

	public BTreeNode<AnyType> getParent() {
		return parent;
	}

	public void setParent(BTreeNode<AnyType> parent) {
		this.parent = parent;
	}

}
