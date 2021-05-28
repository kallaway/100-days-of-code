package com.hunderd.days.ds1;

import java.util.Queue;
import java.util.concurrent.ArrayBlockingQueue;

public class QueueBasedStackImpl<E> implements Stack<E> {

	Queue<E> q1;
	Queue<E> q2;

	boolean pushInQ1 = true;
	int MAX_SIZE;

	public QueueBasedStackImpl(int size) {
		this.MAX_SIZE = size;
		q1 = new ArrayBlockingQueue<>(size);
		q2 = new ArrayBlockingQueue<>(size);

	}

	@Override
	public void push(E e) throws Exception {
		if (pushInQ1) {
			q1.add(e);
		} else {
			q2.add(e);

		}
	}

	@Override
	public E pop() throws Exception {
		if (pushInQ1) {
			int size = q1.size();

			for (int i = 1; i < size ; i++) {
				System.out.println(q1.peek());
				q2.add(q1.poll());
			}
			pushInQ1 = false;

			return q1.poll();

		} else {
			int size = q2.size();
			for (int i = 1; i < size ; i++) {
				System.out.println(q1.peek());

				q1.add(q2.poll());
			}
			pushInQ1 = true;

			return q2.poll();

		}
	}

	@Override
	public int size() {
		return (pushInQ1) ? q1.size() : q2.size();
	}
	
	
	public static void main(String[] args) {
		
		Stack<Integer> st = new QueueBasedStackImpl<>(3);
		
		try {
			st.push(1);
			//System.out.println(st.size());
			st.push(2);
			st.push(3);
			st.push(4);
			//System.out.println(st.size());

			//Integer pop = st.pop();
			//System.out.println(pop);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}

}
