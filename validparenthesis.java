import java.util.Stack;

public class validparenthesis {
    public static boolean isValid (String s){
        Stack<Character> st = new Stack<>();
        for (char c:s.toCharArray()){
            if (c=='('||c=='['||c=='{')
                st.push(c);
            else{
                if(!st.isEmpty() && getChar(c)==st.peek())
                    st.pop();
                else
                    return false;
            }
        }
        return st.isEmpty();
    }

    static char getChar(char c){
        if (c==')') return '(';
        if (c=='}') return '{';
        else return '[';
    }
    public static void main(String[] args) {
        String s = "[{()}]";
        String a = "";        
        String d = "{]";        
        System.out.println(isValid(s));
        System.out.println(isValid(a));
        System.out.println(isValid(d));

    }
}
//Runtime: 2 ms, faster than 90.88%
