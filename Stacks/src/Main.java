
public class Main {

	public static void main(String[] args) {
		// Stack using array
//		ArrayStack stack = new ArrayStack(10);
		
//		stack.push(new Student("Kapil", "22c", 47));
//		stack.push(new Student("John", "snow", 111));
//		stack.push(new Student("camilia", "clark", 102));
//		stack.push(new Student("amanda", "cerny", 1235));
		
		Student s1 = new Student("Kapil", "Bavisiya", 1212);
		Student s2 = new Student("meet", "Sorathiya", 58);
		Student s3 = new Student("tushar", "gajera", 569);
		Student s4 = new Student("Naimish", "Sorathiya", 111);
		
		LinkedStack stack = new LinkedStack();
		stack.push(s1);
		stack.push(s2);
		stack.push(s3);
		stack.push(s4);
		
		
//		stack.printStack();
		
//		 
		
		System.out.println("Popped: "+ stack.pop());
		System.out.println(stack.peek());
		

	}

}
