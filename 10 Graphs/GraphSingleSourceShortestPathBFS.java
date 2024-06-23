
import java.util.ArrayList;
import java.util.LinkedList;

class ILGraphNode {
    String name;
    int index;
    public ArrayList<ILGraphNode> neighbours = new ArrayList<ILGraphNode>();
    public boolean isVisited;
    public ILGraphNode parent;

    ILGraphNode(String name, int index) {
        this.name = name;
        this.index = index;
    }
}

class ILGraph {
    ArrayList<ILGraphNode> nodeList = new ArrayList<ILGraphNode>();

    ILGraph(ArrayList<ILGraphNode> nodeList) {
        this.nodeList = nodeList;
    }

    public void addEdge(int i, int j) {
        ILGraphNode first = this.nodeList.get(i);
        ILGraphNode second = this.nodeList.get(j);
        first.neighbours.add(second);
        second.neighbours.add(first);
    }

    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("\n");

        for (int i = 0; i < nodeList.size(); i++) {
            s.append(nodeList.get(i).name + " : ");
            for (ILGraphNode j : nodeList.get(i).neighbours) {
                s.append(" -> " + j.name);
            }
            s.append("\n");
        }

        return s.toString();
    }

    void pritPath(ILGraphNode node) {
        if (node.parent != null) {
            pritPath(node.parent);
        }
        System.out.print(node.name + " ");
    }

    public void bfsSingleShort() {
        ILGraphNode node = nodeList.get(0);
        LinkedList<ILGraphNode> queue = new LinkedList<>();
        queue.add(node);

        while (!queue.isEmpty()) {
            ILGraphNode currentNode = queue.remove(0);
            System.out.print("Printing for " + currentNode.name + " : ");
            currentNode.isVisited = true;
            pritPath(currentNode);
            System.out.println();
            for (ILGraphNode nei : currentNode.neighbours) {
                if (!nei.isVisited) {
                    queue.add(nei);
                    nei.isVisited = true;
                    nei.parent = currentNode;
                }
            }
        }
    }
}

public class GraphSingleSourceShortestPathBFS {
    public static void main(String[] args) {

        ArrayList<ILGraphNode> nodeList = new ArrayList<ILGraphNode>();
        nodeList.add(new ILGraphNode("A", 0));
        nodeList.add(new ILGraphNode("B", 1));
        nodeList.add(new ILGraphNode("C", 2));
        nodeList.add(new ILGraphNode("D", 3));
        nodeList.add(new ILGraphNode("E", 4));
        nodeList.add(new ILGraphNode("F", 5));
        nodeList.add(new ILGraphNode("G", 6));

        ILGraph graph = new ILGraph(nodeList);
        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 6);
        graph.addEdge(2, 3);
        graph.addEdge(2, 4);
        graph.addEdge(3, 5);
        graph.addEdge(4, 5);
        graph.addEdge(5, 6);
        graph.bfsSingleShort();
    }
}
