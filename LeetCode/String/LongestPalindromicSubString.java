package LeetCode.String;

public class LongestPalindromicSubString {
    public static void main(String[] args) {
        // System.out.println(lonngPalidroimmString("cbbd"));
        // System.out.println(lonngPalidroimmString("babad"));
        System.out.println(lonngPalidroimmString("bb"));
    }

    static String lonngPalidroimmString(String s) {
        String longPalindrome = s.charAt(0) + "";
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j < s.length(); j++) {
                String subString = s.substring(i, j + 1);
                System.out.println("Substring " + subString);
                if (isPalindrome(subString)) {
                    if (subString.length() > longPalindrome.length()) {
                        longPalindrome = subString;
                    }
                }
            }
        }
        return longPalindrome;
    }

    static boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        for (; j >= i; j--, i++) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
        }
        return true;
    }

}
