public class ArrayStack {
    int[] arr;
    int size;
    int capacity;

    public ArrayStack(int n) {
        this.capacity = n;
        this.arr = new int[capacity];
        this.size = 0;
    }

    public void push(int value) {
        System.out.println("Operation: push(" + value + ")");

               if (size == capacity) {
            System.out.println("Time Complexity: O(N)");
            
            capacity = capacity * 2;
            int[] newArr = new int[capacity];
            
                        for (int i = 0; i < size; i++) {
                newArr[i] = arr[i];
            }
            arr = newArr;
        } else {
          
            System.out.println("Time Complexity: O(1)");
        }

        arr[size] = value;
        size++;

        printStack();
    }

    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return -1;
        }
        int topValue = arr[size - 1];
        size--; // Just decreasing the size is enough
        
        System.out.println("Operation: pop()");
        printStack();
        return topValue;
    }

    public int peek() {
        if (isEmpty()) {
            return -1;
        }
        return arr[size - 1];
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

   
    public void printStack() {
        System.out.print("Current Stack: [");
        for (int i = 0; i < size; i++) {
            if (i == size - 1) {
                System.out.print(arr[i] + " (TOP)");
            } else {
                System.out.print(arr[i] + ", ");
            }
        }
        System.out.println("]");
        System.out.println("-------------------------");
    }

    public static void main(String[] args) {
      
        ArrayStack stack = new ArrayStack(2);

        stack.push(10);
        stack.push(20);
        stack.push(30); 
        stack.pop();
        stack.pop();
        stack.push(40);
    }
}