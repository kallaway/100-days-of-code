package com.hunderd.days.ds1;

import java.util.LinkedList;
import java.util.List;


public class LinkedListStackImpl<E> implements Stack<E> {
	
	List<E> list =null;
	
	int top=-1;
	int MAX_SIZE=0;
	
	
	public  LinkedListStackImpl(int size) {
		list = new LinkedList<>();
		this.MAX_SIZE=size;
		
	}

	@Override
	public void push(E e) throws Exception {
		if(top>MAX_SIZE) {
			throw new Exception("stack is full");
		}
		list.add(++top, e);
		
	}

	@Override
	public E pop() throws Exception {
		if(top==-1) {
			throw new Exception("stack is empty");
		}
		
		return list.remove(top--);
	}

	@Override
	public int size() {
		// TODO Auto-generated method stub
		return top;
	}
	
	public static void main(String[] args) {
		Stack<Integer> stack = new LinkedListStackImpl<Integer>(3);

		System.out.println("==1====" + stack.size());

		try {
			stack.push(100);
			System.out.println("==2====" + stack.size());
			stack.push(101);
			System.out.println("==3====" + stack.size());

			System.out.println(stack.pop());
		  System.out.println("==4===="+ stack.size());
			System.out.println(stack.pop());
			// System.out.println("==5===="+ stack.size());
			 System.out.println(stack.pop());
			//stack.push(100);
			//stack.push(100);
			//stack.push(100);

		} catch (Exception e) {
			System.out.println("exception will be==>" + e);
		}

	}

}
