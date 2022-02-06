import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.Dimension;
import javax.swing.ImageIcon;
import java.awt.Color;
import javax.swing.SwingConstants;
import java.awt.Font;
import java.awt.Image;

public class Ventana extends JFrame String{
	
	public Ventana(){
		this.setSize(600, 350);
		setDefaultCloseOperation(EXIT_ON_CLOSE); //comando para activar la "x" y que se cierre nuestro programa cuando cerramos la pestaña
		setTitle("Primera Ventana");
		//setLocation(200,200);
		/* El metodo set Bounds te permite hacer en un metodo lo que haces con setLocation(posicion inicial)
		 * y setSice(tamaño de la ventana)
		 */
		//setBounds(200,200,600,300);
		// Metodo para centrar nuestra ventana
		setLocationRelativeTo(null);
		//	setMinimunSize(new Dimension(200,200));
		//this.getContentPane().setBackground(Color.BLACK);
		iniciarComponentes();
	}

	private void iniciarComponentes(){
		JPanel panel = new JPanel(); //Creación de un panel.
		this.getContentPane().add(panel); //Agregamos nuestro panel a la ventana.
		panel.setLayout(null); // Desactivarlo para poder acomodar nuestra etiqueta en donde queramos.
		//panel.setBackground(Color.GREEN); //Cambiamos el color del panel.
		//JLabel etiqueta = new JLabel("Primera Etiqueta"); 
		// o
		//JLabel etiqueta = new JLabel();
		//etiqueta.setText("Mi primera vez");
		JLabel etiqueta = new JLabel("Mi segunda vez", SwingConstants.LEADING); // LEFT, CENTER, RIGHT, LEADING or TRAILING. 
		/*
		 * Si no quieres ocupar este constructor, podemos utilizar el metodo 
		 * setHorizontalAlignment(SwingCOnstants.CENTER)
		 */
		etiqueta.setBounds(130,10,250,50); // El tercer parametro es para el ancho de nuestra etiqueta y el cuarto para el largoORANGE
		etiqueta.setForeground(Color.YELLOW); //Comando para cambiar el color de la letra de nuestra etiqueta.
		//Comando para cambiar el color del fondo de nuestra etiqueta, el fondo por default es transparente.
		/* Las etiquetas no te dejan cambiar el color de fondo, por lo que debemos desactivar el diseño por defecto
		 * y la desactivamos con el método .setOpaque()
		 */
		etiqueta.setOpaque(true);
		etiqueta.setBackground(Color.BLACK); //CYAN
		etiqueta.setFont(new Font("DejaVu Math TeX Gyre", 0, 30)); //Establecemos la fuente del texto.
		// Font(name(depende de tu sistema operativo), estilo(2 es cursiva, 3 es cursiva y NEGRITA, PLAIN, BOLD, ITALIC), tamaño)
		panel.add(etiqueta);
		// Agregamos nuestra etiqueta en nuestra ventana.
		ImageIcon imagen = new ImageIcon("pepo.jpeg");
		JLabel etiqueta2 = new JLabel();
		etiqueta2.setBounds(10, 60, 500, 500);
		etiqueta2.setIcon(new ImageIcon(imagen.getImage().getScaledInstance(etiqueta2.getWidth(), etiqueta2.getHeight(), Image.SCALE_SMOOTH))); 
		// Metodo para cambiar el tamaño de nuestra imagen, el primer antributo va el ancho, el segundo el largo
		// Y el tercero es el escalado
		panel.add(etiqueta2);
	}

	public static void main(String[] args) {
		Ventana primera = new Ventana();
		primera.setVisible(true);
	}
}