
/*
Question 1 : Implement a stack using Array
Write push and pop methods to demonstrate Stack behavior (Last In First Out).
*/


package com.hunderd.days.ds0;

public class ArrayStackImpl {

	int[] arr;
	int top = -1;

	ArrayStackImpl(int size) {
		arr = new int[size];
	}

	public void push(int element) throws Exception {

		if (top >= arr.length - 1) {
			throw new Exception("stack is full");
		}

		arr[++top] = element;

	}

	public int pop() throws Exception {

		if (top == -1) {
			throw new Exception("stack is empty");
		}
		return arr[top--];
	}

	public int size() {
		return top;
	}

	public static void main(String[] args) {

		ArrayStackImpl stack = new ArrayStackImpl(3);

		System.out.println("==1====" + stack.size());

		try {
			stack.push(100);
			System.out.println("==2====" + stack.size());
			stack.push(101);
			System.out.println("==3====" + stack.size());

			System.out.println(stack.pop());
			// System.out.println("==4===="+ stack.size());
			// System.out.println(stack.pop());
			// System.out.println("==5===="+ stack.size());
			// System.out.println(stack.pop());
			//stack.push(100);
			//stack.push(100);
			//stack.push(100);

		} catch (Exception e) {
			System.out.println("exception will be==>" + e);
		}

	}

}


