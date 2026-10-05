
void main() {
Stack<Character> stack = new Stack<>();
    System.out.println( isBalanced("(a+b)*(c-d)"));
    System.out.println( isBalanced("{[()()]}"));
    System.out.println( isBalanced("{[(])}"));
    System.out.println(isBalanced("((("));
    System.out.println(isBalanced(""));
}

public static boolean isBalanced(String s) {
    if (s.length() == 0) return true;
    else {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(s.charAt(i));
            } else if (s.charAt(i) == ')') {
                if (stack.peek() == '(') {
                    stack.pop();
                }
            } else if (s.charAt(i) == '{') {
                stack.push(s.charAt(i));
            } else if (s.charAt(i) == '}') {
                if (stack.peek() == '{') {
                    stack.pop();
                }
            } else if (s.charAt(i) == '[') {
                stack.push(s.charAt(i));
            } else if (s.charAt(i) == ']') {
                if (stack.peek() == '[') {
                    stack.pop();
                }
            }

        }
        return stack.isEmpty();
    }
}