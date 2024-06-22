import java.util.ArrayList;

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
}