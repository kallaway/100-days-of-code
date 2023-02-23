import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		List<Employee> emp = new ArrayList<>();
		emp.add(new Employee("Kapil", "Bavisiya", 123));
		emp.add(new Employee("John", "Doe", 222));
		emp.add(new Employee("Jane", "Doe", 111));
		
		System.out.println(emp.get(2));
		
		System.out.println(emp.isEmpty());
		
		emp.set(1, new Employee("bharat", "bavisiya", 444));
		
		System.out.println(emp.size());
		
		emp.add(3, new Employee("John", "Doe", 000));
//		emp.forEach(e -> System.out.println(e));
		
//		Employee[] empArray = emp.toArray(new Employee[emp.size()]);
//		for(Employee e : empArray) {
//			System.out.println(e);
//		}
		
		System.out.println(emp.contains(new Employee("Kapil","Bavisiya",123)));
		
		System.out.println(emp.indexOf(new Employee("John", "Doe", 0)));
		
		emp.remove(3);
		emp.forEach(e -> System.out.println(e));
		
		
	}	

}
