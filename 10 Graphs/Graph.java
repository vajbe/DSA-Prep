import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Stack;
import java.util.concurrent.LinkedBlockingDeque;

public class Graph {
    ArrayList<GraphNode> nodeList = new ArrayList<GraphNode>();
    int[][] adjancencyMatrix;

    public Graph(ArrayList<GraphNode> nodeList) {
        this.nodeList = nodeList;
        adjancencyMatrix = new int[nodeList.size()][nodeList.size()];
    }

    public void addUndirectedEdge(int i, int j) {
        this.adjancencyMatrix[i][j] = 1;
        this.adjancencyMatrix[j][i] = 1;
    }

    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("\t");
        for (int i = 0; i < nodeList.size(); i++) {
            s.append(nodeList.get(i).name + "\t");
        }
        s.append("\n");

        for (int i = 0; i < nodeList.size(); i++) {
            s.append(nodeList.get(i).name + " : ");
            for (int j : adjancencyMatrix[i]) {
                s.append("\t" + j);
            }
            s.append("\n");
        }

        return s.toString();
    }

    ArrayList<GraphNode> getNeighbours(GraphNode node) {
        ArrayList<GraphNode> neighbours = new ArrayList<GraphNode>();
        int nodeIndex = node.index;

        for (int i = 0; i < adjancencyMatrix.length; i++) {
            if (adjancencyMatrix[nodeIndex][i] == 1) {
                neighbours.add(nodeList.get(i));
            }
        }
        return neighbours;
    }

    void bfsVisit(GraphNode node) {
        LinkedList<GraphNode> list = new LinkedList<GraphNode>();
        list.add(node);

        while (!list.isEmpty()) {
            GraphNode graphNode = list.remove(0);
            graphNode.isVisited = true;
            System.err.print(" " + graphNode.name);
            ArrayList<GraphNode> neighbours = getNeighbours(graphNode);
            for (GraphNode neighbour : neighbours) {
                if (!neighbour.isVisited) {
                    list.add(neighbour);
                    neighbour.isVisited = true;
                }
            }
        }
    }

    public void bfs() {
        System.out.print("BFS =>");
        for (GraphNode node : nodeList) {
            if (!node.isVisited) {
                bfsVisit(node);
            }
        }
        System.out.println("");
    }

    void dfsVisit(GraphNode node) {
        Stack<GraphNode> stack = new Stack<GraphNode>();
        stack.push(node);

        while (!stack.isEmpty()) {
            GraphNode currentNode = stack.pop();
            currentNode.isVisited = true;
            System.err.print(" " + currentNode.name);
            ArrayList<GraphNode> neighbours = getNeighbours(currentNode);
            for (GraphNode neighbour : neighbours) {
                if (!neighbour.isVisited) {
                    stack.push(neighbour);
                    neighbour.isVisited = true;
                }
            }
        }
    }

    public void dfs() {
        System.out.print("DFS => ");
        for (GraphNode node : nodeList) {
            if (!node.isVisited)
                dfsVisit(node);
        }
        System.out.println("");
    }
}