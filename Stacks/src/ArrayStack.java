import java.util.EmptyStackException;

public class ArrayStack {
	private Student[] stack;
	private int top;
	
	public ArrayStack(int capacity) {
		stack = new Student[capacity];
	}
	
	public void push(Student std) {
		if(top == stack.length) {
			// need to resize the backing array
			Student[] newArray = new Student[2*stack.length];
			System.arraycopy(stack, 0, newArray, 0, stack.length);
			stack = newArray;
		}
		
		stack[top++] = std;
	}
	
	public Student pop() {
		if(isEmpty()) {
			throw new EmptyStackException();
		}
		Student std = stack[--top];
		stack[top] = null;
		return std;	   
	}
	
	public Student peek() {
		if(isEmpty()) {
			throw new EmptyStackException();
		}
		
		return stack[top - 1];
	}
	
	public int size() {
		return top;
	}
	
	public boolean isEmpty() {
		return top==0;
	}
	
	public void printStack() {
		for(int i= top-1; i>=0; i--) {
			System.out.println(stack[i]);
		}
	}
	
	
}
