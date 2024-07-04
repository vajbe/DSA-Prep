import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

class WeightedNode implements Comparable<WeightedNode> {
    public String name;
    public ArrayList<WeightedNode> neighbours = new ArrayList<>();
    public HashMap<WeightedNode, Integer> weightMap = new HashMap<>();
    public int distance;
    public int index;
    public boolean isVisited;
    public WeightedNode parent;

    public WeightedNode(String name, int index) {
        this.name = name;
        this.index = index;
        distance = Integer.MAX_VALUE;
    }

    @Override
    public String toString() {
        return this.name;
    }

    @Override
    public int compareTo(WeightedNode o) {
        return this.distance - o.distance;
    }

}

class WeightedGraph {
    public ArrayList<WeightedNode> nodeList = new ArrayList<>();

    public WeightedGraph(ArrayList<WeightedNode> nodeList) {
        this.nodeList = nodeList;
    }

    void dijkstra(WeightedNode node) {
        PriorityQueue<WeightedNode> queue = new PriorityQueue<>();
        node.distance = 0;
        queue.addAll(nodeList);
        while (!queue.isEmpty()) {
            WeightedNode currentNode = queue.remove();
            for (WeightedNode neighbour : currentNode.neighbours) {
                if (queue.contains(neighbour)) {
                    if (neighbour.distance > currentNode.distance + currentNode.weightMap.get(neighbour)) {
                        neighbour.distance = currentNode.distance + currentNode.weightMap.get(neighbour);
                        neighbour.parent = currentNode;
                        queue.remove(neighbour);
                        queue.add(neighbour);
                    }
                }
            }
        }

        for (WeightedNode nodeToCheck : nodeList) {
            System.out.print("Node: " + nodeToCheck + ", Distance: " + nodeToCheck.distance + ", Path:");
            pritPath(nodeToCheck);
            System.out.println();
        }
    }

    void pritPath(WeightedNode node) {
        if (node.parent != null) {
            pritPath(node.parent);
        }
        System.out.print(node.name + " ");
    }

    public void addEdge(int firstIndex, int secondIndex, int distance) {
        WeightedNode firstNode = nodeList.get(firstIndex);
        WeightedNode secondNode = nodeList.get(secondIndex);
        firstNode.neighbours.add(secondNode);
        firstNode.weightMap.put(secondNode, distance);
    }

}

public class Dijkstras {
    public static void main(String[] args) {
        ArrayList<WeightedNode> nodeList = new ArrayList<>();
        nodeList.add(new WeightedNode("A", 0));
        nodeList.add(new WeightedNode("B", 1));
        nodeList.add(new WeightedNode("C", 2));
        nodeList.add(new WeightedNode("D", 3));
        nodeList.add(new WeightedNode("E", 4));
        nodeList.add(new WeightedNode("F", 5));
        nodeList.add(new WeightedNode("G", 6));

        WeightedGraph graph = new WeightedGraph(nodeList);

        graph.addEdge(0, 1, 2);
        graph.addEdge(0, 2, 5);
        graph.addEdge(1, 2, 6);
        graph.addEdge(1, 3, 1);
        graph.addEdge(1, 4, 3);
        graph.addEdge(2, 5, 8);
        graph.addEdge(3, 4, 4);
        graph.addEdge(4, 6, 9);
        graph.addEdge(5, 6, 7);

        System.out.println("Printing Paths --- ");
        graph.dijkstra(nodeList.get(0));

    }
}
