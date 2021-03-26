import java.util.Random;

public class Red {

	public int capas = 4;
	public int neuronas_por_capa[] = { 2, 4, 4, 1 };
	public double[][] entradas;
	public double[][][] umbrales;
	public double[][][][] pesos;
	public Random rand = new Random(10);
	private int u,c;
	
	public void Build() {

		this.c = 0;
		this.u = 0;
		for (int k = 0; k < capas -1 ; k++) {
			pesos = new double[capas][capas][neuronas_por_capa[k]][neuronas_por_capa[k + 1]];
			umbrales = new double[capas][capas][neuronas_por_capa[k]];
			entradas = new double[capas][neuronas_por_capa[k]];

		}

		// Random values

		// Pesos
		for (int k = 0; k < capas - 1; k++) {
			for (int i = 0; i < neuronas_por_capa[k]; i++) {
				for (int j = 0; j < neuronas_por_capa[k + 1]; j++) {
					pesos[k][i][j][0] = rand.nextDouble();
					// System.out.println("W[" + k + "," + i + "," + j + "] = " +
					// pesos[k][i][j][0]);
					++this.c;
				}
			}
		}
		// System.out.println("total pesos: " + c+"\n\n");

		for (int k = 1; k < capas; k++) {
			for (int i = 0; i < neuronas_por_capa[k]; i++) {
				umbrales[k][i][0] = rand.nextDouble();
				// System.out.println("U[" + k + "," + i + "] = " + umbrales[k][i][0]);
				++this.c;

			}
		}
		// System.out.println("total pesos: " + u);

	}

	public void calculaSalida() {
		// forward propagation

		for (int k = 1; k < capas; k++) {

			for (int i = 0; i < neuronas_por_capa[k]; i++) {

				entradas[k][i] = 0;

				// sumatorio
				for (int j = 0; j < neuronas_por_capa[k-1]; j++) {

					entradas[k][i] += entradas[k - 1][j] * pesos[k - 1][j][i][0];

				}
				entradas[k][i] = entradas[k][i]+umbrales[k][i][0];
				entradas[k][i] = (1) / (1 + (Math.exp(-entradas[k][i])));
				// System.out.println(entradas[k][i][0]);
			}

		}
	}

	public void backpropagation(double[] se, double[] e, double tasaAprende) {

		// PARA PESOS
		// capa 4
		for (int j = 0; j < neuronas_por_capa[2]; j++) {
			for (int i = 0; i < neuronas_por_capa[3]; ++i) {

				double yi = entradas[3][i];
				double derror = entradas[2][j] * yi * (1 - yi) * (-se[i] + yi);
				pesos[2][j][i][0] = pesos[2][j][i][0] - (tasaAprende * derror);//modifica pesos jejerejeje

			}
		}

		// capa 3

		for (int j = 0; j < neuronas_por_capa[1]; j++) {

			for (int k = 0; k < neuronas_por_capa[2]; k++) {

				double acum = 0;

				for (int i = 0; i < neuronas_por_capa[3]; i++) {
					double yi = entradas[3][i];
					acum += pesos[2][k][i][0] * yi * (1 - yi) * (-se[i] + yi);

				}
				double derror = entradas[1][j] * entradas[2][k] * (1 - entradas[2][k]) * acum;
				pesos[1][j][k][0] = pesos[1][j][k][0] - (tasaAprende * derror);

			}
		}

		// capa 2
		for (int j = 0; j < neuronas_por_capa[0]; j++) {

			for (int k = 0; k < neuronas_por_capa[1]; k++) {

				double acumular = 0;

				for (int p = 0; p < neuronas_por_capa[2]; ++p) {

					double acum = 0;

					for (int i = 0; i < neuronas_por_capa[3]; i++) {
						double yi = entradas[3][i];

						acum += pesos[2][p][i][0] * yi * (1 - yi) * (-se[i] + yi);

					}
					acumular += pesos[1][k][p][0] * entradas[2][p] * (1 - entradas[2][p]) * acum;

				}
				double derror = e[j] * entradas[1][k] * (1 - entradas[1][k]) * acumular;
				pesos[0][j][k][0] = pesos[0][j][k][0] - (tasaAprende * derror);
			}
		}

		// UMBRALES

		// capa 4

		for (int i = 0; i < neuronas_por_capa[3]; i++) {

			double yi = entradas[3][i];
			double derror = yi * (1 - yi) * (-se[i] + yi);
			umbrales[2][i][0] = umbrales[2][i][0] - (tasaAprende * derror);

		}

		// capa 3
		for (int k = 0; k < neuronas_por_capa[2]; k++) {

			double acum = 0;
			for (int i = 0; i < neuronas_por_capa[3]; i++) {
				double yi = entradas[3][i];
				acum += pesos[2][k][i][0] * yi * (1 - yi) * (-se[i] + yi);

			}
			double derror = entradas[2][k] * (1 - entradas[2][k]) * acum;
			umbrales[1][k][0] = umbrales[1][k][0] - (tasaAprende * derror);

		}

		// capa 2

		for (int k = 0; k < neuronas_por_capa[1]; k++) {
			double acumular = 0;
			for (int p = 0; p < neuronas_por_capa[2]; p++) {

				double acum = 0;

				for (int i = 0; i < neuronas_por_capa[3]; i++) {
					double yi = entradas[3][i];
					acum += pesos[2][p][i][0] * yi * (1 - yi) * (-se[i] + yi);
				}
				acumular += pesos[1][k][p][0] * entradas[2][p] * (1 - entradas[2][p]) * acum;

			}
			double derror = entradas[1][k] * (1 - entradas[1][k]) * acumular;
			umbrales[0][k][0] = umbrales[0][k][0] - (tasaAprende * derror);

		}
	}

}
