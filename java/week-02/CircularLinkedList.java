public class CircularLinkedList {
    int size;
    Node tail;

    void add(int x) {
        Node n = new Node(x);
        if(size==0){
            tail = n;
            tail.next = tail;
            size++;
        }
        else{
            n.next = tail.next;
            tail.next = n;
            tail=n;
            size++;
        }


    }


    void rotate(){
        Node temp =tail;
        tail = tail.next;


    }
    void removeFirst() {

        if (size == 0) {
            return;
        }


        if (size == 1) {
            tail = null;
        }

        else {
            tail.next = tail.next.next;
        }
size--;
    }
    void print(){
        Node curr=tail.next;
        System.out.println("-----------------------------------------");
        for(int i=0;i<size;i++){
            System.out.println(curr.value+" ");
            curr=curr.next;
        }
    }

}

