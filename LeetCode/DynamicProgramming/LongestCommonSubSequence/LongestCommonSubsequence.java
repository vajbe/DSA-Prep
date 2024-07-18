package LeetCode.DynamicProgramming.LongestCommonSubSequence;
// TOP DOWN APPROACH
public class LongestCommonSubsequence {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                dp[i][j] = -1;
            }
        }
        return longestCommon(text1, text2, m, n, dp);
    }

    int longestCommon(String text1, String text2, int m, int n, int[][] dp) {
        if (m == 0 || n == 0) {
            return 0;
        }
        if (dp[m][n] != -1) {
            return dp[m][n];
        }
        if (text1.charAt(m - 1) == text2.charAt(n - 1)) {
            return dp[m][n] = 1 + longestCommon(text1, text2, m - 1, n - 1, dp);
        } else {
            return dp[m][n] = Math.max(longestCommon(text1, text2, m - 1, n, dp),
                    longestCommon(text1, text2, m, n - 1, dp));
        }
    }
}