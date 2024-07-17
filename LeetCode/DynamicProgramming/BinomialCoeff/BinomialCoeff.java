package LeetCode.DynamicProgramming.BinomialCoeff;

// User function Template for Java

import java.util.Arrays;

class BinoamialCoeff {

    public static void main(String[] args) {
        nCr(69, 43);
    }

    static int nCr(int n, int k) {
        // code here
        int[][] dp = new int[n + 1][k + 1];
        System.out.println(Arrays.deepToString(dp));

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= Math.min(i, k); j++) {
                if (j == 0 || i == j) {
                    dp[i][j] = 1;
                } else
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            }
        }
        System.out.println(Arrays.deepToString(dp));
        System.out.println(dp[n][k]);

        /*
        Brute Force Approach
         * if (r > n) {
         * return 0;
         * }
         * if (r == 0 || n == r) {
         * return 1;
         * }
         * return nCr(n - 1, r - 1) + nCr(n - 1, r);
         */
        return dp[n][k];
    }
}