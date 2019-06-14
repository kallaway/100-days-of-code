import javax.swing.JOptionPane;

public class Line 
{
	private int x1;
	private int y1;
	private int x2;
	private int y2;
	
	public Line()
	{
		x1=10;
		x2=10;
		y1=10;
		y2=10;
	}
	public Line(int a1, int b1, int a2, int b2)
	{
		x1=a1;
		x2=a1;
		y1=b1;
		y2=b2;
	}
	public int getX1(){return x1;}
	public int getX2(){return x2;}
	public int getY1(){return y1;}
	public int getY2(){return y2;}	
	public void getAttributes()
	{
		String input;
		
	    input = JOptionPane.showInputDialog(null,"Please enter an integer:",
				" X-Coordiante of the start Point ",JOptionPane.QUESTION_MESSAGE);
        x1=Integer.parseInt(input);

        input = JOptionPane.showInputDialog(null,"Please enter an integer:",
				" Y-Coordiante of the start Point ",JOptionPane.QUESTION_MESSAGE);
        y1=Integer.parseInt(input);
        
        input = JOptionPane.showInputDialog(null,"Please enter an integer:",
				" X-Coordiante of the End Point ",JOptionPane.QUESTION_MESSAGE);
        x2=Integer.parseInt(input);

        input = JOptionPane.showInputDialog(null,"Please enter an integer:",
				" Y-Coordiante of the End Point ",JOptionPane.QUESTION_MESSAGE);
        y2=Integer.parseInt(input);
	}
	public double getLength()
	{
		return Math.sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) );
	}
}
