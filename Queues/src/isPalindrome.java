
import java.util.LinkedList;

public class isPalindrome {

    public static void main(String[] args) {
        // should return true
        System.out.println(checkForPalindrome("abccba"));
        // should return true
        System.out.println(checkForPalindrome("Was it a car or a cat I saw?"));
        // should return true
        System.out.println(checkForPalindrome("I did, did I?"));
        // should return false
        System.out.println(checkForPalindrome("hello"));
        // should return true
        System.out.println(checkForPalindrome("Don't nod"));
    }

    public static boolean checkForPalindrome(String string) {
    	
    	LinkedList<Character> stack = new LinkedList<Character>();
    	LinkedList<Character> queue = new LinkedList<Character>();
    	String lowerCase = string.toLowerCase();
    	
    	for(int i=0; i<lowerCase.length();i++) {
    		char c = lowerCase.charAt(i);
    		if(c >= 'a' && c<='z') {
    			queue.addLast(c);
    			stack.push(c);
    		}
    	}
    	
    	while(!stack.isEmpty()) {
    		if(!stack.pop().equals(queue.removeFirst())) {
    			return false;
    		}
    	}
    	return true;
    }
}
