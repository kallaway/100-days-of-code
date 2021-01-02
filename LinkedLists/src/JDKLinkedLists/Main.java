package JDKLinkedLists;

import java.util.Iterator;
import java.util.LinkedList;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Employee e1 = new Employee("Kapil", "bavisiya", 159);
		Employee e2 = new Employee("Nehal", "bavisiya", 444);
		Employee e3 = new Employee("bharat", "bavisiya", 458);
		Employee e4 = new Employee("kiran", "bavisiya", 587);
		
		Employee billEnd = new Employee("Bill", "End", 100);
		
		LinkedList<Employee> list = new LinkedList<>();
		list.addFirst(e1);
		list.addFirst(e2);
		list.addFirst(e3);
		list.addFirst(e4);
		
		Iterator iter = list.iterator();
		System.out.print("HEAD -> ");
		while(iter.hasNext()) {
			System.out.print(iter.next());
			System.out.print("<=>");
		}
		System.out.println("null");
		
//		for(Employee employee: list) {
//			System.out.println(employee);
//		}
		
				
		list.add(billEnd);  // you also can use addLast..result are same
		iter = list.iterator();
		System.out.print("HEAD -> ");
		while(iter.hasNext()) {
			System.out.print(iter.next());
			System.out.print("<=>");
		}
		System.out.println("null");
		
		list.removeFirst();  // or you can use remove();
		iter = list.iterator();
		System.out.print("HEAD -> ");
		while(iter.hasNext()) {
			System.out.print(iter.next());
			System.out.print("<=>");
		}
		System.out.println("null");
		
		list.removeLast();
		iter = list.iterator();
		System.out.print("HEAD -> ");
		while(iter.hasNext()) {
			System.out.print(iter.next());
			System.out.print("<=>");
		}
		System.out.println("null");
		
		

	}

}
