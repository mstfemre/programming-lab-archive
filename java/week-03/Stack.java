class Node<T>{
    Node next;
    T value;
    Node(T value){
        this.value = value;
    }
}


public class Stack<T> {
    private int lenght;
    private Node top;
    void push(T value){
        Node nn = new Node(value);
        if(lenght==0){
            top = nn;
        }else{
            nn.next = top;
            top = nn;
        }
        lenght++;
    }
    T pop(){
if(lenght==0){
    throw new IllegalArgumentException("Stack is empty");
}else{
    Object val=top.value;
    Node temp =top.next;
    top=temp;
    lenght--;
    return (T)val;
}
    }
    T peek(){
        if(lenght==0){
            throw new IllegalArgumentException("Stack is empty");
        }else{
    Object val=top.value;
return (T)val;
        }

     }
     boolean isEmpty(){
        return lenght==0;
     }


}
