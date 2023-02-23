import java.util.Arrays;

//import com.sun.tools.javac.util.List;
import java.util.*;

public class DemoStringBuilder {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<String> trees = Arrays.asList("Hello","This",
				 "is","new","tree");
		System.out.println(listToString(trees));
		System.out.println(listWithSeparator(trees, ","));
		
		String word ="asddsa";
		System.out.printf("%s : %b", word, isPalindrome(word));
	}
	
	private static String listToString(List<String> list) {
		StringBuilder sb = new StringBuilder(32);
		for(String el : list) {
			sb.append(el).append(" ");
		}
		return sb.toString();
	}
	// we can do this with String as well.. 
	//but it will create new object every time when we concate a string
	// for small input it is useful but not for the large no. of string

	private static String listWithSeparator(List<String> list, String separator)
	{
		StringBuilder sb = new StringBuilder(32);
		boolean first = true;
		
		for(String el : list) {
			if(first)
				first= false;
			else {
				sb.append(separator);
			}
			sb.append(el);
		}
		return sb.toString();
	}
	
	private static boolean isPalindrome(String word) {
		StringBuilder sb = new StringBuilder(word);
		String reversed = sb.reverse().toString();
		
		return reversed.equalsIgnoreCase(word);
	}
}
