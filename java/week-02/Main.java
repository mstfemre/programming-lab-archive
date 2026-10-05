void main() {
CircularLinkedList list = new CircularLinkedList();
list.add(1);
list.add(2);
list.add(3);
list.add(4);
list.add(5);
list.print();
list.rotate();
list.print();
    System.out.println("-----------------------------------------");
    System.out.println("before remove");
list.removeFirst();
list.print();
    System.out.println("-----------------------------------------");
System.out.println("after remove");
    System.out.println("-----------------------------------------");

}
