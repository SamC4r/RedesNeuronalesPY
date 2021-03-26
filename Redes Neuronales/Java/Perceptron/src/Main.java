import java.awt.List;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static Red r = new Red();
	public static double[][] entra;
	private static Scanner s;
	private static Scanner ent;


	public static void main(String[] args) {
		
		
		int conjunto = 4;
		double[][] entra = { { 0, 0 }, { 0, 1 }, { 1, 0 }, { 1, 1 } };
		double[][] sale = { { 0 }, { 1 }, { 1 }, { 0 } };
		r.Build();

		for (int a = 0; a <= 8001; a++) {
			if (a % 1000 == 0)
				System.out.println("Iteracion " + a);

			for (int i = 0; i < conjunto; i++) {
				r.entradas[0] = entra[i];
				r.calculaSalida();
				r.backpropagation(sale[i], entra[i], 0.4f);

				if (a % 1000 == 0) {

					System.out.println(r.entradas[r.entradas.length - 1][0] + "  <vs>  " + sale[i][0]);
				}
			}

		}

		Demostrar();

	}

	private static void Demostrar() {
		
		
		
		for (int k = 0; k < r.capas -1 ; k++) {

			entra= new double[r.capas][r.neuronas_por_capa[k]];

		}
		int conjunto;
		int e;
		s = new Scanner(System.in);

		System.out.println("conjunto entradas: ");
		conjunto = s.nextInt();

		for (int a = 0; a < conjunto; a++) {

			double[] c = new double[r.neuronas_por_capa[0]];
			for (int b = 0; b < r.neuronas_por_capa[0]; b++) {
				ent = new Scanner(System.in);
				System.out.println("Entrada " + b + ": ");
				e = ent.nextInt();
				c[b] = e;

			}
			entra[0]= c;
			System.out.println(calculaSalidaNueva(entra));
			

		}

	}

	private static double calculaSalidaNueva(double[][] entra) {

		for (int k = 1; k < r.capas; k++) {

			for (int i = 0; i < r.neuronas_por_capa[k]; i++) {

				entra[k][i] = 0;

				// sumatorio
				for (int j = 0; j < r.neuronas_por_capa[k - 1]; j++) {

					entra[k][i] += entra[k - 1][j] * r.pesos[k - 1][j][i][0];

				}
				entra[k][i] = entra[k][i] + r.umbrales[k][i][0];
				entra[k][i] = (1) / (1 + (Math.exp(-entra[k][i])));
				// System.out.println(entradas[k][i][0]);
			}

		}

		return entra[entra.length-1][0];

	}

}
