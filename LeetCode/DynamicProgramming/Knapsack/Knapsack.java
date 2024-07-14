package LeetCode.DynamicProgramming.Knapsack;

import java.util.Arrays;

public class Knapsack {
    public static void main(String[] args) {
        int w = 10;
        int[] val = { 10, 40, 30, 50 };
        int[] wt = { 5, 4, 6, 3 };
        int n = wt.length;

        int[][] mat = new int[n + 1][w + 1];

        for (int i = 0; i < w + 1; i++) {
            mat[0][i] = 0;
        }

        for (int j = 0; j < n + 1; j++) {
            mat[j][0] = 0;
        }

        for (int item = 1; item <= n; item++) {
            for (int capacity = 1; capacity <= w; capacity++) {
                int withoutCurrent = mat[item - 1][capacity];
                int withCurrent = 0;
                int weightOfCurrent = wt[item - 1];
                if (capacity >= weightOfCurrent) {
                    withCurrent = val[item - 1];
                    int remaining = capacity - weightOfCurrent;
                    withCurrent += mat[item - 1][remaining];
                }
                mat[item][capacity] = Math.max(withoutCurrent, withCurrent);
            }
        }

        System.out.println(mat[n][w]);
        System.out.println(Arrays.deepToString(mat));
    }
}
