package LeetCode.Greedy.FractionalKnapsack.LeetCodeSolution;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Sol {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        ArrayList<KnapsackItem> list = new ArrayList<KnapsackItem>();

        for (int i = 0; i < boxTypes.length; i++) {
            list.add(new KnapsackItem(boxTypes[i][0], boxTypes[i][1]));
        }
        return KnapsackSolution.getMax(list, truckSize);
    }
}

class KnapsackItem {
    private int weight;
    private int value;
    private double ratio;

    public KnapsackItem(int v, int w) {
        this.weight = w;
        this.value = v;
        this.ratio = Math.floor((v * 1.0) / w);
    }

    public int getWeight() {
        return this.weight;
    }

    public int getValue() {
        return this.value;
    }

    public double getRatio() {
        return this.ratio;
    }
}

class KnapsackSolution {
    static int getMax(ArrayList<KnapsackItem> list, int capacity) {
        Comparator<KnapsackItem> c = new Comparator<KnapsackItem>() {
            @Override
            public int compare(KnapsackItem o1, KnapsackItem o2) {
                if (o2.getRatio() > o1.getRatio()) {
                    return 1;
                }
                return -1;
            }
        };
        Collections.sort(list, c);
        int usedCapacity = 0;
        double totalValue = 0;
        for (KnapsackItem item : list) {
            if (usedCapacity + item.getWeight() <= capacity) {
                usedCapacity += item.getWeight();
                totalValue += item.getValue();
            } else {
                System.err.println();
                int usedWeight = capacity - usedCapacity;
                double value = item.getRatio() * usedWeight;
                usedCapacity += usedWeight;
                totalValue += value;
            }
            System.out.println(
                    " Value: " + item.getValue() + " Weight: " + item.getWeight() + " Ratio: " + item.getRatio()
                            + " Total Value: " + totalValue);
            if (usedCapacity == capacity)
                break;
        }
        return (int) Math.round(totalValue);
    }
}

class Solution {
    public static void main(String[] args) {
        Sol s = new Sol();
        int[][] numbers = { { 1, 3 }, { 2, 2 }, { 3, 1 } };
        System.out.println(s.maximumUnits(numbers, 4));
    }
}