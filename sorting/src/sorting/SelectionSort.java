package sorting;

public class SelectionSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] intArray = {20,35,-15,22,18,2,32};
		
		for(int lastUnsortedindex = intArray.length-1; lastUnsortedindex>0;
					lastUnsortedindex--) {
			int largest=0;
			for(int i=1; i<=lastUnsortedindex; i++) {
				if(intArray[i] > intArray[largest]) {
					largest = i;
				}
			}
			swap(intArray, largest, lastUnsortedindex);
			
		}
		
		for(int i=0; i<intArray.length; i++) {
			System.out.println(intArray[i]);
		}
		

	}
	
	public static void swap(int[] array, int i, int j) {
		if(i==j) {
			return;
		}
		else {
			int temp = array[i];
			array[i] = array[j];
			array[j] = temp;
		}
		
	}

}
