package net.tekrei;

import java.util.List;

import net.tekrei.ds.GraphNode;
import net.tekrei.ds.impl.Graph;

public class GraphTest {
	public static void main(String[] args) {
		Graph<Integer> graph = new Graph<Integer>();
		List<Integer> integerList = SortingTest.generateIntegerList(5);
		System.out.println(integerList);
		for (Integer i : integerList) {
			graph.add(i);
		}

		// add 20 random edges
		for (int i = 0; i < 10; i++) {
			GraphNode<Integer> firstNode = graph.getNode(SortingTest
					.randomInt(graph.size()));
			GraphNode<Integer> secondNode = graph.getNode(SortingTest
					.randomInt(graph.size()));
			graph.addEdge(firstNode, secondNode);
		}

		System.out.println(graph);
		System.out.println(graph.bfs(graph.getNode(0)));
		System.out.println(graph.dfs(graph.getNode(0)));
		System.out.println(graph.dijkstra(graph.getNode(0)));
	}

}
