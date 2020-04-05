package net.tekrei;

import java.util.List;

import net.tekrei.ds.AVLTree;
import net.tekrei.ds.BinaryHeap;
import net.tekrei.ds.BinarySearchTree;
import net.tekrei.ds.DLinkedList;
import net.tekrei.ds.Graph;
import net.tekrei.ds.GraphNode;
import net.tekrei.ds.Queue;
import net.tekrei.ds.SLinkedList;
import net.tekrei.ds.Stack;

public class DSTest {

    private static int LIST_SIZE = 100;

    public static void main(String[] args) {
        List<Integer> integerList = Utilities.generateIntegerList(LIST_SIZE);
        System.out.println(integerList);
        testStack(integerList);
        testQueue(integerList);
        testLinkedList(integerList);
        testGraph(integerList);
        testBinaryHeap(integerList);
        testBinarySearchTree(integerList);
        testAVLTree(integerList);
    }

    private static void testStack(List<Integer> integerList) {
        Stack<Integer> stack = new Stack<Integer>();
        System.out.println("STACK");
        for (Integer i : integerList) {
            stack.push(i);
            System.out.println(stack);
        }
        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
        }
    }

    private static void testQueue(List<Integer> integerList) {
        Queue<Integer> queue = new Queue<Integer>();
        System.out.println("QUEUE");
        for (Integer i : integerList) {
            queue.enqueue(i);
            System.out.println(queue);
        }
        while (!queue.isEmpty()) {
            System.out.println(queue.dequeue());
        }
    }

    private static void testLinkedList(List<Integer> integerList) {
        SLinkedList<Integer> linkedList = new SLinkedList<Integer>();
        DLinkedList<Integer> dlinkedList = new DLinkedList<Integer>();
        for (Integer i : integerList) {
            linkedList.insert(i);
            dlinkedList.insert(i);
        }
        System.out.println("SINGLE LINKED LIST");
        System.out.println(linkedList);
        linkedList.remove(5);
        System.out.println(linkedList);

        System.out.println("DOUBLE LINKED LIST");
        System.out.println(dlinkedList);
        dlinkedList.remove(8);
        System.out.println(dlinkedList);
    }

    private static void testGraph(List<Integer> integerList) {
        Graph<Integer> graph = new Graph<Integer>();
        System.out.println("GRAPH");
        for (Integer i : integerList) {
            graph.add(i);
        }

        // add 20 random edges
        for (int i = 0; i < 10; i++) {
            GraphNode<Integer> firstNode = graph.getNode(Utilities.randomInt(graph.size()));
            GraphNode<Integer> secondNode = graph.getNode(Utilities.randomInt(graph.size()));
            graph.addEdge(firstNode, secondNode);
        }

        System.out.println(graph);
        System.out.println(graph.bfs(graph.getNode(0)));
        System.out.println(graph.dfs(graph.getNode(0)));
        System.out.println(graph.dijkstra(graph.getNode(0)));
    }

    private static void testBinaryHeap(List<Integer> integerList) {
        BinaryHeap<Integer> heap = new BinaryHeap<Integer>(15);
        System.out.println("BINARY HEAP");
        for (Integer i : integerList) {
            heap.insert(i);
        }

        while (!heap.isEmpty()) {
            System.out.println(heap.remove());
        }
    }

    private static void testBinarySearchTree(List<Integer> integerList) {
        BinarySearchTree<Integer> tree = new BinarySearchTree<Integer>();
        System.out.println("BINARY SEARCH TREE");
        for (Integer i : integerList) {
            tree.insert(i);
        }
        System.out.println(tree.size());
        System.out.println(tree);
        System.out.println(tree.postorderTraversal());
        System.out.println(tree.preorderTraversal());
        tree.insert(15);
        System.out.println(tree);
        tree.remove(15);
        System.out.println(tree);
        tree.insert(5);
        System.out.println(tree);
        System.out.println(tree.find(5));
        System.out.println(tree.contains(5));
        tree.remove(5);
        System.out.println(tree.contains(5));
        System.out.println(tree);
        System.out.println(tree.findMin());
        tree.print();
    }

    private static void testAVLTree(List<Integer> integerList) {
        AVLTree<Integer> tree = new AVLTree<Integer>();
        System.out.println("AVL TREE");
        for (Integer i : integerList) {
            tree.insert(i);
        }
        System.out.println(tree.size());
        System.out.println(tree);
        System.out.println(tree.postorderTraversal());
        System.out.println(tree.preorderTraversal());
        tree.insert(15);
        System.out.println(tree);
        tree.remove(15);
        System.out.println(tree);
        tree.insert(5);
        System.out.println(tree);
        System.out.println(tree.find(5));
        System.out.println(tree.contains(5));
        tree.remove(5);
        System.out.println(tree.contains(5));
        System.out.println(tree);
        System.out.println(tree.findMin());
        tree.checkBalance();
        tree.print();
    }

}