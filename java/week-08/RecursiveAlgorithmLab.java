public class RecursiveAlgorithmLab {
    public static void main(String[] args) {
        int[] examPapers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

        System.out.println("Task 1 - Sequential Grading");
        gradeSequentially(examPapers, 0);

        System.out.println();
        System.out.println("Task 2 - Finding a Specific Exam");
        int target = 70;
        int foundIndex = findExam(examPapers, target, 0, examPapers.length - 1);
        if (foundIndex == -1) {
            System.out.println("Exam ID " + target + " was not found.");
        } else {
            System.out.println("Exam ID " + target + " was found at index " + foundIndex + ".");
        }

        System.out.println();
        System.out.println("Task 3 - Archive Binding");
        bindExams(examPapers, 0, examPapers.length - 1);

        System.out.println();
        printComplexityReport();
    }

    public static void gradeSequentially(int[] exams, int index) {
        if (index >= exams.length) {
            return;
        }

        System.out.println("Grading Exam ID: " + exams[index]);
        gradeSequentially(exams, index + 1);
    }

    public static int findExam(int[] exams, int target, int left, int right) {
        if (left > right) {
            return -1;
        }

        int mid = left + (right - left) / 2;

        if (exams[mid] == target) {
            return mid;
        }

        if (target < exams[mid]) {
            return findExam(exams, target, left, mid - 1);
        }

        return findExam(exams, target, mid + 1, right);
    }

    public static void bindExams(int[] exams, int left, int right) {
        if (left > right) {
            return;
        }

        if (left == right) {
            System.out.println("Single Exam ID ready: " + exams[left]);
            return;
        }

        int mid = left + (right - left) / 2;

        bindExams(exams, left, mid);
        bindExams(exams, mid + 1, right);

        for (int i = left; i <= right; i++) {
            System.out.println("Binding Exam ID: " + exams[i]
                    + " in segment [" + left + ", " + right + "]");
        }
    }

    public static void printComplexityReport() {
        int paperCount = 1048576;
        int taskOneFrames = paperCount + 1;
        int taskTwoSuccessfulFrames = 21;
        int taskTwoWorstCaseFrames = 22;

        System.out.println("Task 4 - Complexity Report");
        System.out.println("Big-O complexities:");
        System.out.println("Task 1: O(n)");
        System.out.println("Task 2: O(log n)");
        System.out.println("Task 3: O(n log n)");
        System.out.println("Ranked from fastest to slowest: Task 2, Task 1, Task 3");
        System.out.println();
        System.out.println("For exactly " + paperCount + " (2^20) exam papers:");
        System.out.println("Task 1 stack frames: " + taskOneFrames
                + " including the base-case frame (" + paperCount + " grading frames).");
        System.out.println("Task 2 stack frames: " + taskTwoWorstCaseFrames
                + " in the worst case including the not-found base-case frame ("
                + taskTwoSuccessfulFrames + " frames if found at the deepest level).");
        System.out.println();
        System.out.println("If Task 2 divided the pile into 3 parts instead of 2:");
        System.out.println("New Big-O notation: O(log_3 n), which is still O(log n).");
    }
}
