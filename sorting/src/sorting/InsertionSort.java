package sorting;

public class InsertionSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] intArray = {15, 25, 21, 22, 56, 48, 2, -1, -22, 6};
		
		for(int firstUnsortedIndex = 1; firstUnsortedIndex<intArray.length; 
				firstUnsortedIndex++) {
			int newElement = intArray[firstUnsortedIndex];
			int i;
			for(i=firstUnsortedIndex; i>0 && intArray[i-1]> newElement ; i--) {
				intArray[i] = intArray[i-1];
			}
			intArray[i] = newElement;
		}
		
		for(int i=0; i<intArray.length; i++) {
			System.out.print(intArray[i]+" ");
		}

	}

}
