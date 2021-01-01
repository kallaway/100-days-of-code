
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Employee jd = new Employee("Jane", "Doe", 777);
		Employee kb = new Employee("Kapil", "Bavisiya", 458);
		Employee hk = new Employee("Hasmukh", "Vekariya", 125);
		Employee rk = new Employee("Ravi", "Kahar", 444);
		
		EmployeeDoublyLinkedList list = new EmployeeDoublyLinkedList();
		
		System.out.println(list.isEmpty());
		list.addToFront(jd);
		list.addToFront(kb);
		list.addToFront(hk);
		list.addToFront(rk);
		
		list.printList();
		System.out.println(list.getSize());
//		System.out.println(list.isEmpty());
//		list.removeFromFront();
//		list.printList();
//		System.out.println(list.getSize());
		
		Employee kkEnd = new Employee("K", "k", 0);
		
		list.addToEnd(kkEnd);
		list.printList();
		System.out.println(list.getSize());
		
		list.removeFromFront();
		list.printList();
		System.out.println(list.getSize());
		
		list.removeFromEnd();
		list.printList();
		System.out.println(list.getSize());
		
		
	}

}
