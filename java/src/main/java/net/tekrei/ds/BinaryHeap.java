package net.tekrei.ds;

import java.util.Arrays;

/**
 * Binary Heap implementation - minimum is the highest priority (min-heap)
 * 
 * @author tekrei
 * 
 *         A binary heap is a heap data structure created using a binary tree.
 *         It can be seen as a binary tree with two additional constraints:
 * 
 *         Shape property: A binary heap is a complete binary tree; that is, all
 *         levels of the tree, except possibly the last one (deepest) are fully
 *         filled, and, if the last level of the tree is not complete, the nodes
 *         of that level are filled from left to right.
 * 
 *         Heap property: All nodes are either greater than or equal to or less
 *         than or equal to each of its children, according to a comparison
 *         predicate defined for the heap.
 *
 * @param <AnyType>
 *            type of the data stored in it
 * 
 * @see <a href=
 *      "https://en.wikipedia.org/wiki/Heap_(data_structure)">https://en
 *      .wikipedia.org/wiki/Heap_(data_structure)</a ><br/>
 *      <a href="http://courses.cs.washington.edu/courses/cse373/11wi/homework
 *      /5
 *      /BinaryHeap.java">http://courses.cs.washington.edu/courses/cse373/11wi/
 *      homework /5/BinaryHeap.java</a>
 */
public class BinaryHeap<AnyType extends Comparable<AnyType>> {

	// storage for the values
	private AnyType[] data;
	// size of the heap
	private Integer size;

	@SuppressWarnings("unchecked")
	public BinaryHeap(Integer initialSize) {
		data = (AnyType[]) new Comparable[initialSize];
		size = 0;
	}

	public BinaryHeap() {
		this(100);
	}

	public void insert(AnyType value) {
		if (size >= data.length - 1)
			data = this.resize();
		// put the value to the last
		size++;
		int index = size;
		data[index] = value;
		// and move it to the correct position
		percolateUp();
	}

	public AnyType peek() {
		if (isEmpty()) {
			return null;
		}
		return data[1];
	}

	public boolean isEmpty() {
		return (size == 0);
	}

	public AnyType remove() {
		AnyType result = peek();

		// get rid of the last leaf/decrement
		data[1] = data[size];
		data[size] = null;
		size--;
		// arrange the tree to fulfill the properties
		percolateDown();

		return result;
	}

	public Integer size() {
		return size;
	}

	/**
	 * correct the heap after removal
	 */
	private void percolateDown() {
		int index = 1;

		while (hasLeftChild(index)) {
			// which of my children is smaller?
			int smallerChild = leftIndex(index);

			// bubble with the smaller child, if I have a smaller child
			if (hasRightChild(index)
					&& data[leftIndex(index)]
							.compareTo(data[rightIndex(index)]) > 0) {
				smallerChild = rightIndex(index);
			}

			if (data[index].compareTo(data[smallerChild]) > 0) {
				swap(index, smallerChild);
			} else {
				break;
			}

			// make sure to update loop counter/index of where last el is put
			index = smallerChild;
		}
	}

	/**
	 * correct the heap after insertion
	 */
	private void percolateUp() {
		int index = this.size;
		// starting from the insertion point
		// compare the elements and swap with their parents
		// until heap is OK
		while (hasParent(index) && (parent(index).compareTo(data[index]) > 0)) {
			swap(index, parentIndex(index));
			index = parentIndex(index);
		}
	}

	private boolean hasParent(int i) {
		return i > 1;
	}

	private int leftIndex(int i) {
		return i * 2;
	}

	private int rightIndex(int i) {
		return i * 2 + 1;
	}

	private boolean hasLeftChild(int i) {
		return leftIndex(i) <= size;
	}

	private boolean hasRightChild(int i) {
		return rightIndex(i) <= size;
	}

	private AnyType parent(int i) {
		return data[parentIndex(i)];
	}

	private int parentIndex(int i) {
		return i / 2;
	}

	private AnyType[] resize() {
		return Arrays.copyOf(data, data.length * 2);
	}

	private void swap(int index1, int index2) {
		AnyType tmp = data[index1];
		data[index1] = data[index2];
		data[index2] = tmp;
	}

	public String toString() {
		return Arrays.toString(data);
	}

}
