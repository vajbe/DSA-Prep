package LeetCode.Greedy;

import java.util.Arrays;
import java.util.Comparator;

class Balloons {
    int[][] points;

    Balloons(int[][] points) {
        this.points = points;
    }

    public int findMinArrowShots() {
        Arrays.sort(points, Comparator.comparingInt(o -> o[1]));
        int count = 0;
        long last = Long.MIN_VALUE;
        for (int i = 0; i < points.length; i++) {
            // System.out.println("Comparing " + points[i][0] + " > " + points[i - 1][1]);
            if (last < points[i][0]) {
                count++;
                last = points[i][1];
            }
        }
        return count;
    }

    @Override
    public String toString() {
        for (int[] x : points) {
            for (int y : x) {
                System.out.print(y + " ");
            }
            System.out.println();
        }
        return "";
    }
}

class BalloonsSolution {
    public static void main(String[] args) {
        int[][] balloons = { { 10, 16 }, { 2, 8 }, { 1, 6 }, { 7, 12 } };
        Balloons b = new Balloons(balloons);
        System.out.println(b.findMinArrowShots());
        System.out.println(b);
    }
}