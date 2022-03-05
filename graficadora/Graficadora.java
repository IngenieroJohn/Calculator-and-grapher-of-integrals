package graficadora;
import javax.swing.*;
import java.awt.*;
public class Graficadora {
	public static plano plano;
	public static void main(String[] args) {
		
		Ventana frame = new Ventana();
		frame.setDefaultCloseOperation(Ventana.EXIT_ON_CLOSE);
		frame.setBounds(500, 300, 510, 400);
		frame.setLayout(new BorderLayout());
		plano = new plano();
		
		JButton start = new JButton("Iniciar");
		start.addActionListener(frame);
		start.setText("Iniciar");
		
		frame.add( plano, BorderLayout.CENTER);
		frame.add(start, BorderLayout.SOUTH);
		frame.setVisible( true );
	}

}
