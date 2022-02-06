import java.awt.Frame;
import java.awt.Button;
import java.awt.event.WindowListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Label;
import java.awt.List;

/**
 * 
 * Clase que crea una interfaz gráfica.
 * @author José Manuel Pedro Méndez. 
 * @version Agosto 2020.
 */

public class InterfazGrafica{
	private Frame ventana = new Frame("Mi primera inferfaz grafica");
	private final Button b1 = new Button("Boton 1");
	private final Button b2 = new Button("Boton 2");
	private final Label l1 = new Label("Texto de Ejemplo");
	private final Label l2 = new Label("Hola k tal ");
	private final List lista1 = new List();
	private final Button b3 = new Button("Boton 3");
	private final Button[] botones;	

	public InterfazGrafica(){
    	botones = new Button[3];
    	botones[0] = b1;
    	botones[1] = b2;
    	botones[2] = b3;
    	/* 
    	 * Metodo que nos permite cambiar las coordenadas x,y de nuestro boton(Los primeros dos parametros)
    	 * Los otros parametros son para definir el tamaño de nuestro boton.
    	 * El segundo es de ariiba hacia abajo
    	 * El primero es de Izquierda a la Derecha
    	 */
    	b1.setBounds(100,100,300,50);
    	ventana.add(b1);

    	b2.setBounds(100,200,300,50);
    	ventana.add(b2);

    	b3.setBounds(100, 800, 300, 50);
    	ventana.add(b3);

    	/*l1.setBounds(100,400,200,50);
    	ventana.add(l1);*/

    	/*lista1.setBounds(400, 300, 200, 300);
    	lista1.add("Elemento 1");
    	lista1.add("Elemento 2");
    	lista1.add("Elemento 3");
    	lista1.add("Elemento 4");
    	lista1.add("Elemento 5");
    	lista1.add("Elemento 6");
    	lista1.add("Elemento 7");
    	lista1.add("Elemento 8");
    	lista1.add("Elemento 9");
    	lista1.add("Elemento 10");
    	lista1.add("Elemento 11");
    	ventana.add(lista1);*/

    	l2.setBounds(700, 10, 200, 50);
    	ventana.add(l2);

    	ventana.setSize(1024,700);
    	ventana.setLayout(null);
    	ventana.setVisible(true);

    	b1.addActionListener(new ActionListener(){
    		public void actionPerformed(ActionEvent e){
    			b2.setVisible(true);
    			b1.setVisible(false);
    		}
    	});

    	b2.addActionListener(new ActionListener(){
    		public void actionPerformed(ActionEvent e){
    			b2.setVisible(false);
    			b1.setVisible(true);
    		}
    	});

    	b3.addActionListener(new ActionListener(){
    		public void actionPerformed(ActionEvent e){
    			b2.setVisible(false);
    			b1.setVisible(true);
    		}
    	});

    	/*
    	b3.addActionListener(new ActionListener(){
    		public void actionPerformed(ActionEvent e){
    			int pos = lista1.getSelectedIndex();
    			String elemento = lista1.getItem(pos);
    			l2.setText(elemento);
    		}
    	});*/

    	ventana.addWindowListener(new WindowAdapter() {
    		public void windowClosing(WindowEvent we) {
    			ventana.dispose();
    		}
    	});

    }
    public static void main(String[] args) {
    	InterfazGrafica in = new InterfazGrafica();
    }
}