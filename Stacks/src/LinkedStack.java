import java.util.LinkedList;
import java.util.ListIterator;

public class LinkedStack {
	private LinkedList<Student> stack;
	public LinkedStack() {
		stack = new LinkedList<Student>();
	}
	
	public void push(Student std) {
		stack.push(std);
	}
	
	public Student pop() {
		return stack.pop();
	}
	
	public Student peek() {
		return stack.peek();
	}
	
	public boolean isEmpty() {
		return stack.isEmpty();
	}
	
	public void printStack() {
		ListIterator<Student> iter = stack.listIterator();
		while(iter.hasNext()) {
			System.out.println(iter.next());
		}
	}
}
