package graficadora;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.BorderFactory;
import javax.swing.JPanel;
public class plano extends JPanel{
	public plano() {
		init();
		
	}
	public void init() {
		this.setBorder(BorderFactory.createLineBorder(Color.black));
	}
	public void paintComponent( Graphics g ) {
		super.paintComponent(g);
		g.setColor(Color.red);
		g.drawLine(0, this.getHeight()/2, this.getWidth(), this.getHeight()/2);
		g.drawLine(this.getWidth()/2, 0,this.getWidth()/2 , this.getHeight());
		
	}
	public void paintSQRFunc(Graphics g, double x2mult,
			double x1mult,double cons, double x1,double x2)
	{
		for(double i=x1;i<x2;i++)
		{
			double y = ((double)Math.pow(i,2)*x2mult)+i*x1mult+cons;
			double xp = i+1;
			double yp = ((double)Math.pow(xp,2)*x2mult)+xp*x1mult+cons;
			g.drawLine((int)coord_x(i), (int)coord_y(y), (int)coord_x(xp), (int)coord_y(yp));
		}
	}
	private double coord_x(double x)
	{
		double real_x = x+this.getWidth()/2;
		return real_x;
	}
	private double coord_y(double y)
	{
		double real_y = -y+this.getHeight()/2;
		return (real_y);
	}
	
		
	
	

}
