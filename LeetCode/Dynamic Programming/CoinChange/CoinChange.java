
import java.util.Arrays;

public class CoinChange {
    public static void main(String[] args) {
        int[] coins = { 1, 2, 5 };
        int sum = 11;
        int[] dp = new int[sum + 1];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        int ans = CoinChange.calculateChange(coins, sum, dp);
        System.out.println(ans);
    }

    static int calculateChange(int[] arr, int n, int[] dp) {
        if (n == 0)
            return 0;
        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < arr.length; i++) {
            if (n - arr[i] >= 0) {
                int subAns = 0;
                if (dp[n - arr[i]] != -1) {
                    subAns = dp[n - arr[i]];
                } else {
                    subAns = calculateChange(arr, n - arr[i], dp);
                }

                if (subAns != Integer.MAX_VALUE && subAns + 1 < ans) {
                    ans = subAns + 1;
                }
            }
        }
        return dp[n] = ans;
    }
}