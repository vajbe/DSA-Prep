package LeetCode.DynamicProgramming.Knapsack;

import java.util.Arrays;

public class KnasackExample {
    public static void main(String[] args) {
        int w = 10;
        int[] val = { 10, 40, 30, 50 };
        int[] wt = { 5, 4, 6, 3 };
        int n = wt.length;
        int[][] dp = new int[n + 1][w + 1];
        for (int i = 0; i < n + 1; i++) {
            dp[i][0] = 0;
        }

        for (int j = 0; j < w + 1; j++) {
            dp[0][j] = 0;
        }

        for (int item = 1; item <= n; item++) {
            for (int capacity = 1; capacity <= w; capacity++) {
                int withoutCurrent = dp[item - 1][capacity];
                int withCurrent = 0;
                int weightOfCurrent = wt[item - 1];

                if (capacity >= weightOfCurrent) {
                    withCurrent = val[item - 1];
                    int remaining = capacity - weightOfCurrent;
                    withCurrent += dp[item - 1][remaining];
                }
                dp[item][capacity] = Math.max(withoutCurrent, withCurrent);
            }
        }

        System.out.println(dp[n][w]);
        System.out.println(Arrays.deepToString(dp));
    }
}
