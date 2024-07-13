package LeetCode.Greedy.FractionalKnapsack;

public class KnapSackItem {
    private int index;
    private int weight;
    private double ratio;
    private int value;

    public int getIndex() {
        return index;
    }

    public KnapSackItem(int index, int weight, int value) {
        this.index = index;
        this.weight = weight;
        this.value = value;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public double getRatio() {
        return ratio;
    }

    public void setRatio(double ratio) {
        this.ratio = ratio;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return "Index: " + index + " Weight: " + weight + " Ratio: " + ratio + "Value: " + value;
    }

}
