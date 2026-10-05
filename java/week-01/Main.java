void main() {


        int[] data = {42, 15, 8, 99, 23, 4, 16,9,9,9,9,9,243,3,5,98,86,2,123,53,62,626,7,5,0};


        ArrayOperations list = new ArrayOperations(data);

        System.out.print("before sorting: ");
        list.display();


        list.oddEvenSort();

        System.out.print("after sorting: ");
        list.display();

        list.noDups();
        System.out.print("after removing duplicates: ");
        list.display();
    }