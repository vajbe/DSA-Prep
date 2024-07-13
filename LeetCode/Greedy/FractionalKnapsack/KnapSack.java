package LeetCode.Greedy.FractionalKnapsack;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class KnapSack {
    static void knapSack(ArrayList<KnapSackItem> list, int capacity) {
        Comparator<KnapSackItem> comparator = new Comparator<KnapSackItem>() {
            @Override
            public int compare(KnapSackItem o1, KnapSackItem o2) {
                if (o2.getRatio() > o1.getRatio()) {
                    return 1;
                }
                return -1;
            }
        };
        Collections.sort(list, comparator);

        int usedCapacity = 0;
        double totalValue = 0;

        for (KnapSackItem item : list) {
            if (usedCapacity + item.getWeight() <= capacity) {
                usedCapacity += item.getWeight();
                totalValue += item.getValue();
            } else {
                int usedWeight = capacity - usedCapacity;
                double value = item.getRatio() * usedWeight;
                usedCapacity += usedWeight;
                totalValue += value;
            }
            System.out.println(
                    "Index: " + item.getIndex() + " Value: " + item.getValue() + " Weight: " + item.getWeight()
                            + " Total Value: " + totalValue);
            if (capacity == usedCapacity)
                break;
        }
        System.out.println("Total value obtained " + totalValue);
    }

}
