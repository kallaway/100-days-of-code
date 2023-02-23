public class IsUnique {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(isUnique("kapil"));

	}
//	private static boolean isUnique(String str) {
//		for(int i=0; i<str.length()-1; i++) {
//			if(str.charAt(i) == str.charAt(i+1))
//				return false;
//		}
//	   return true;
//	}   O(n^2)
	
//	private static boolean isUnique(String str) {
//		if(str.length()>128)
//			return false;
//		boolean[] ch = new boolean[128];
//		for(int i=0; i<str.length(); i++) {
//			int val = str.charAt(i);
//			if(ch[val])
//				return false;
//			ch[val]=true;
//		}
//		return true;
//	}
	// O(1) for n>128
	// O(n) for n<=128..
	
	private static boolean isUnique(String str) {
		int checker = 0;
		for(int i=0; i< str.length();i++) {
			int val = str.charAt(i) - 'a';
			System.out.println("val: " + val);
			System.out.println("if stmt: "+ (checker & (1<<val)));
			if((checker & (1 << val)) > 0) {
//				System.out.println("if stmt: "+ (checker & (1<<val)));
				return false;
			}
			System.out.println("val after operation: "+ (1 << val));
			checker = checker | (1 << val );
			
			System.out.println("checker: "+checker);
		}
		return true;
	}
}
