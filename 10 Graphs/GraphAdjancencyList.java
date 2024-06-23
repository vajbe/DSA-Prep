import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Stack;

class IGraphNode {
    String name;
    int index;
    public ArrayList<IGraphNode> neighbours = new ArrayList<IGraphNode>();
    public boolean isVisited;

    IGraphNode(String name, int index) {
        this.name = name;
        this.index = index;
    }
}

class IGraph {
    ArrayList<IGraphNode> nodeList = new ArrayList<IGraphNode>();

    IGraph(ArrayList<IGraphNode> nodeList) {
        this.nodeList = nodeList;
    }

    public void addEdge(int i, int j) {
        IGraphNode first = this.nodeList.get(i);
        IGraphNode second = this.nodeList.get(j);
        first.neighbours.add(second);
        second.neighbours.add(first);
    }

    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("\n");

        for (int i = 0; i < nodeList.size(); i++) {
            s.append(nodeList.get(i).name + " : ");
            for (IGraphNode j : nodeList.get(i).neighbours) {
                s.append(" -> " + j.name);
            }
            s.append("\n");
        }

        return s.toString();
    }

    private void bfsVisit(IGraphNode node) {
        LinkedList<IGraphNode> queue = new LinkedList<IGraphNode>();
        queue.add(node);

        while (!queue.isEmpty()) {
            IGraphNode currentNode = queue.remove(0);
            System.out.print(" => " + currentNode.name);
            currentNode.isVisited = true;
            for (IGraphNode neighbour : currentNode.neighbours) {
                if (!neighbour.isVisited) {
                    queue.add(neighbour);
                    neighbour.isVisited = true;
                }
            }
        }
    }

    void bfs() {
        System.out.print("BFS => ");
        for (IGraphNode node : this.nodeList) {
            if (!node.isVisited) {
                this.bfsVisit(node);
            }
        }
    }

    private void dfsVisit(IGraphNode node) {
        Stack<IGraphNode> stack = new Stack<IGraphNode>();
        stack.push(node);

        while (!stack.isEmpty()) {
            IGraphNode currentNode = stack.pop();
            System.out.print(" => " + currentNode.name);
            currentNode.isVisited = true;
            for (IGraphNode neightbour : currentNode.neighbours) {
                if (!neightbour.isVisited) {
                    stack.push(neightbour);
                    neightbour.isVisited = true;
                }
            }
        }
    }

    void dfs() {
        System.out.print("DFS => ");
        for (IGraphNode node : this.nodeList) {
            if (!node.isVisited) {
                dfsVisit(node);
            }
        }
    }

}

public class GraphAdjancencyList {
    public static void main(String[] args) {

        ArrayList<IGraphNode> nodeList = new ArrayList<IGraphNode>();
        nodeList.add(new IGraphNode("A", 0));
        nodeList.add(new IGraphNode("B", 1));
        nodeList.add(new IGraphNode("C", 2));
        nodeList.add(new IGraphNode("D", 3));
        nodeList.add(new IGraphNode("E", 4));
        IGraph g = new IGraph(nodeList);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(0, 3);
        g.addEdge(1, 4);
        g.addEdge(2, 3);
        g.addEdge(3, 4);
        System.out.println(g.toString());
        /* g.bfs(); */
        g.dfs();
    }
}
