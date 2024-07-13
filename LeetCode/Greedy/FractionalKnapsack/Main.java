package LeetCode.Greedy.FractionalKnapsack;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        int[] value = { 100, 120, 60 };
        int[] weight = { 20, 30, 10 };
        int capacity = 50;

        ArrayList<KnapSackItem> list = new ArrayList<>();

        for (int i = 0; i < value.length; i++) {
            list.add(new KnapSackItem(i + 1, weight[i], value[i]));
        }

        KnapSack.knapSack(list, capacity);
    }
}
