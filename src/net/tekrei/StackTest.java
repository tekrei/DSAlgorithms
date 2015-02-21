package net.tekrei;

import java.util.List;

import net.tekrei.ds.impl.Stack;

public class StackTest {

	public static void main(String[] args) {
		Stack<Integer> stack = new Stack<Integer>();
		List<Integer> integerList = SortingTest.generateIntegerList(10);
		for (Integer i : integerList) {
			stack.push(i);
			System.out.println(stack);
		}
		while (!stack.isEmpty()) {
			System.out.println(stack.pop());
		}
	}

}
