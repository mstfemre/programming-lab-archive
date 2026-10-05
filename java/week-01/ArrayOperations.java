public class ArrayOperations {
    private int[] array;
    private int size;


    ArrayOperations(int[] inputArray) {
        array = inputArray;
        size = inputArray.length;
    }

    void display() {
        for (int i = 0; i < size; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    void oddEvenSort() {
        boolean sorted = false;

        while (!sorted) {
            sorted = true;


            for (int i = 1; i < size - 1; i += 2) {
                if (array[i] > array[i + 1]) {
                    int temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp;
                    sorted = false;
                }
            }

                for (int i = 0; i < size - 1; i += 2) {
                    if (array[i] > array[i + 1]) {
                        int temp = array[i];
                        array[i] = array[i + 1];
                        array[i + 1] = temp;
                        sorted = false;
                    }
                }
            }
        }
    void noDups() {

        for (int i = 0; i < size; i++) {

            for (int j = i + 1; j < size; j++) {

                if (array[i] == array[j]) {

                    for (int k = j; k < size - 1; k++) {
                        array[k] = array[k + 1];
                    }

                    size--;
                    j--;
                }
            }
        }
    }
    }