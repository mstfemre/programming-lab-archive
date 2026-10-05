public class Main {
    public static int linearSearch(int[] array, int target) {
        int steps = 0;

        for (int i = 0; i < array.length; i++) {
            steps++;

            if (array[i] == target) {
                System.out.println("Linear Search steps for " + target + ": " + steps);
                return i;
            }
        }

        System.out.println("Linear Search steps for " + target + ": " + steps);
        return -1;
    }

    public static int binarySearch(int[] array, int target) {
        int steps = 0;
        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            steps++;

            int middle = left + (right - left) / 2;

            if (array[middle] == target) {
                System.out.println("Binary Search steps for " + target + ": " + steps);
                return middle;
            } else if (array[middle] < target) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }

        System.out.println("Binary Search steps for " + target + ": " + steps);
        return -1;
    }

    public static boolean isSortedO1(int[] array) {
        if (array.length <= 1) {
            return true;
        }

        return array[0] <= array[array.length - 1];
    }

    public static void showResult(String searchName, int index) {
        if (index == -1) {
            System.out.println(searchName + ": target was not found. Returned index = -1");
        } else {
            System.out.println(searchName + ": target was found at index " + index);
        }
    }

    public static void showLinearComplexity(int index, int length) {
        if (index == 0) {
            System.out.println("Linear Search case: Best Case, O(1)");
        } else if (index == -1 || index == length - 1) {
            System.out.println("Linear Search case: Worst Case, O(n)");
        } else if (index <= 1) {
            System.out.println("Linear Search case: Early Match Case, O(1)");
        } else {
            System.out.println("Linear Search case: Average Case, O(n)");
        }
    }

    public static void showBinaryComplexity(int[] array, int target, int index, boolean sorted) {
        int firstMiddle = (array.length - 1) / 2;

        if (!sorted) {
            System.out.println("Binary Search case: Unsorted Input Case, O(log n)");
        } else if (array[firstMiddle] == target) {
            System.out.println("Binary Search case: Best Case, O(1)");
        } else if (index == -1) {
            System.out.println("Binary Search case: Worst Case, O(log n)");
        } else {
            System.out.println("Binary Search case: Average Case, O(log n)");
        }
    }

    public static void testTarget(int[] dataset, int target) {
        System.out.println("\nTarget value: " + target);

        int linearIndex = linearSearch(dataset, target);
        showResult("Linear Search", linearIndex);
        showLinearComplexity(linearIndex, dataset.length);

        boolean sorted = isSortedO1(dataset);
        System.out.println("O(1) sorted check before Binary Search: " + sorted);

        int binaryIndex = binarySearch(dataset, target);
        showResult("Binary Search", binaryIndex);
        showBinaryComplexity(dataset, target, binaryIndex, sorted);
    }

    public static void main(String[] args) {
        int[] dataset = {10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100};

        System.out.println("Case 1: Searching with Linear Search and Binary Search");
        testTarget(dataset, 999);
        testTarget(dataset, 15);
        testTarget(dataset, 55);

        System.out.println("\nCase 2: General time complexities");
        System.out.println("Linear Search Best Case: O(1)");
        System.out.println("Linear Search Average/Worst Case: O(n)");
        System.out.println("Binary Search Best Case: O(1)");
        System.out.println("Binary Search Average/Worst Case: O(log n)");

        System.out.println("\nCase 3: Corrupting the sorted array");
        int temp = dataset[0];
        dataset[0] = dataset[dataset.length - 1];
        dataset[dataset.length - 1] = temp;

        boolean sorted = isSortedO1(dataset);
        System.out.println("O(1) sorted check before Binary Search: " + sorted);

        int binaryIndex = binarySearch(dataset, 10);
        showResult("Binary Search", binaryIndex);
        showBinaryComplexity(dataset, 10, binaryIndex, sorted);

        if (binaryIndex == -1) {
            System.out.println("Binary Search failed because the array is no longer sorted.");
        }
    }
}
