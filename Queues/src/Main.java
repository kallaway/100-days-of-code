
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Employee e1 = new Employee("Kapil", "bavisiya", 47);
		Employee e2 = new Employee("Dwayne", "bravo", 147);
		Employee e3 = new Employee("keiron", "pollard", 11);
		Employee e4 = new Employee("Chris", "gayle", 333);
		Employee e5 = new Employee("marnus", "labuschange", 33);
		

		ArrayQueue queue = new ArrayQueue(5);
		
		queue.add(e1);
		queue.add(e2);
		queue.remove();
		queue.add(e3);
		queue.remove();
		queue.add(e4);
		queue.remove();
		queue.add(e5);
		queue.remove();

		queue.add(e1);
		
		queue.printQueue();
		
//		ArrayQueue queue = new ArrayQueue(10);
//		queue.add(e1);
//		queue.add(e2);
//		queue.add(e3);
//		queue.add(e4);
//		queue.add(e5);
		
//		queue.printQueue();
		
//		queue.remove();
//		queue.remove();
//		queue.remove();
//		queue.remove();
//		queue.remove();
//		queue.remove();
		
//		queue.add(e3);
//		queue.printQueue();
		
//		System.out.println(queue.peek());
	}

}
