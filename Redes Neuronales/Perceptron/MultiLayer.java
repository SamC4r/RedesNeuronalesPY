package Perceptron;
import java.util.Random;

public class MultiLayer {

    private double[][][] W; //Los pesos serán arreglos multidimensionales. Así: W[capa, neurona inicial, neurona final]
    private double[][] U; //Los umbrales de cada neurona serán arreglos bidimensionales. Así: U[capa, neurona que produce la salida]
    double[][] A; //Las salidas de cada neurona serán arreglos bidimensionales. Así: A[capa, neurona que produce la salida]
    private double[][][] WN; //LosPerceptron nuevos pesos serán arreglos multidimensionales. Así: W[capa, neurona inicial, neurona final]
    private double[][] UN; //Los nuevos umbrales de cada neurona serán arreglos bidimensionales. Así: U[capa, neurona que produce la salida]

    int TotalCapas; //El total de capas que tendrá el perceptrón incluyendo la capa de entrada
    int[] neuronasporcapa; //Cuantas neuronas habrá en cada capa
    int TotalEntradas; //Total de entradas externas del perceptrón
    int TotalSalidas; //Total salidas externas del perceptrón
    public MultiLayer(int TotalEntradas, int TotalSalidas, int TotalCapas, int[] neuronasporcapa) {
        this.TotalEntradas = TotalEntradas;
        this.TotalSalidas = TotalSalidas;
        this.TotalCapas = TotalCapas;
        int maxNeuronas = 0; //Detecta el máximo número de neuronas por capa para dimensionar los arreglos
        this.neuronasporcapa = new int[TotalCapas + 1];
        for (int capa = 1; capa <= TotalCapas; capa++) {
            this.neuronasporcapa[capa] = neuronasporcapa[capa];
            if (neuronasporcapa[capa] > maxNeuronas) maxNeuronas = neuronasporcapa[capa];
        }
//Dimensiona con el máximo valor
        W = new double[TotalCapas + 1][ maxNeuronas + 1][ maxNeuronas + 1];
        U = new double[TotalCapas + 1][ maxNeuronas + 1];
        WN = new double[TotalCapas + 1][ maxNeuronas + 1][ maxNeuronas + 1];
        UN = new double[TotalCapas + 1][ maxNeuronas + 1];
        A = new double[TotalCapas + 1][ maxNeuronas + 1];
//Da valores aleatorios a pesos y umbrales
        Random azar = new Random();
        for (int capa = 2; capa <= TotalCapas; capa++)
            for (int i = 1; i <= neuronasporcapa[capa]; i++)
                U[capa][ i] = azar.nextDouble();
        for (int capa = 1; capa < TotalCapas; capa++)
            for (int i = 1; i <= neuronasporcapa[capa]; i++)
                for (int j = 1; j <= neuronasporcapa[capa+1]; j++)
                    W[capa][ i][ j] = azar.nextDouble();
    }
    public void Procesa(double[] E) {
//Entradas externas del perceptrón pasan a la salida de la primera capa
        for (int copia = 1; copia <= TotalEntradas; copia++) A[1][ copia] = E[copia];
//Proceso del perceptrón
        for (int capa = 2; capa <= TotalCapas; capa++)
            for (int neurona = 1; neurona <= neuronasporcapa[capa]; neurona++) {
                A[capa][ neurona] = 0;
                for (int entra = 1; entra <= neuronasporcapa[capa - 1]; entra++)
                    A[capa][ neurona] += A[capa - 1][ entra] * W[capa - 1][ entra][ neurona];
                A[capa][ neurona] += U[capa][ neurona];
                A[capa][neurona] = 1 / (1 + Math.exp(-A[capa][ neurona]));
            }
    }
    // Muestra las entradas externas del perceptrón, las salidas esperadas y las salidas reales
    public void Muestra(double[] E, double[] S) {
        for (int cont = 1; cont <= TotalEntradas; cont++) System.out.println(E[cont] + ","); System.out.println(" = ");
        for (int cont = 1; cont <= TotalSalidas; cont++) System.out.println(S[cont] + ","); System.out.println(" <vs> ");
        for (int cont = 1; cont <= TotalSalidas; cont++) //Salidas reales del perceptrón
            if (A[TotalCapas][cont] > 0.5){ //El umbral: Mayor de 0.5 es 1, de lo contrario es cero
            System.out.println("1, " + A[TotalCapas][ cont]); //Salida binaria y salida real

        }else{
                System.out.println("0, " + A[TotalCapas][ cont]);
                System.out.println(" ");
    }}
    //El entrenamiento es ajustar los pesos y umbrales
    public void Entrena(double alpha, double[] E, double[] S) {
//Ajusta pesos capa3 ==> capa4
        for (int j = 1; j <= neuronasporcapa[3]; j++)
            for (int i = 1; i <= neuronasporcapa[4]; i++) {
                double Yi = A[4][ i];
                double dE3 = A[3][ j] * (Yi - S[i]) * Yi * (1 - Yi);
                WN[3][ j][ i] = W[3][ j][i] - alpha * dE3; //Nuevo peso se guarda temporalmente
            }
//Ajusta pesos capa2 ==> capa3

        for (int j = 1; j <= neuronasporcapa[2]; j++)
        for (int k = 1; k <= neuronasporcapa[3]; k++) {
            double acum = 0;
            for (int i = 1; i <= neuronasporcapa[4]; i++) {
                double Yi = A[4][ i];
                acum += W[3] [k] [i] * (Yi - S[i]) * Yi * (1 - Yi);
            }
            double dE2 = A[2][j] * A[3][ k] * (1 - A[3][k]) * acum;
            WN[2][j] [k] = W[2][j][ k] - alpha * dE2; //Nuevo peso se guarda temporalmente
        }
//Ajusta pesos capa1 ==> capa2
        for (int j = 1; j <= neuronasporcapa[1]; j++)
            for (int k = 1; k <= neuronasporcapa[2]; k++) {
                double acumular = 0;
                for (int p = 1; p <= neuronasporcapa[3]; p++) {
                    double acum = 0;
                    for (int i = 1; i <= neuronasporcapa[4]; i++) {
                        double Yi = A[4][ i];
                        acum += W[3][ p][ i] * (Yi - S[i]) * Yi * (1 - Yi);
                    }
                    acumular += W[2][ k][ p] * A[3][ p] * (1 - A[3][p]) * acum;
                }
                double dE1 = E[j] * A[2][ k] * (1 - A[2][ k]) * acumular;
                WN[1][ j][ k] = W[1][ j][ k] - alpha * dE1; //Nuevo peso se guarda temporalmente
            }
//Ajusta umbrales de neuronas de la capa 4
        for (int i = 1; i <= neuronasporcapa[4]; i++) {
            double Yi = A[4][ i];
            double dE4 = (Yi - S[i]) * Yi * (1 - Yi);
            UN[4][ i] = U[4][ i] - alpha * dE4; //Nuevo umbral se guarda temporalmente
        }
//Ajusta umbrales de neuronas de la capa 3
        for (int k = 1; k <= neuronasporcapa[3]; k++) {
            double acum = 0;
            for (int i = 1; i <= neuronasporcapa[4]; i++) {
                double Yi = A[4][ i];
                acum += W[3][ k][i] * (Yi - S[i]) * Yi * (1 - Yi);
            }
            double dE3 = A[3][k] * (1 - A[3][k]) * acum;
            UN[3][ k] = U[3][k] - alpha * dE3; //Nuevo umbral se guarda temporalmente
        }
//Ajusta umbrales de neuronas de la capa 2
        for (int k = 1; k <= neuronasporcapa[2]; k++) {
            double acumular = 0;
            for (int p = 1; p <= neuronasporcapa[3]; p++) {
                double acum = 0;
                for (int i = 1; i <= neuronasporcapa[4]; i++) {
                    double Yi = A[4][ i];
                    acum += W[3][ p][i] * (Yi - S[i]) * Yi * (1 - Yi);
                }
                acumular += W[2][ k][p] * A[3][p] * (1 - A[3][p]) * acum;
            }
            double dE2 = A[2][k] * (1 - A[2][k]) * acumular;
            UN[2][k] = U[2][ k] - alpha * dE2; //Nuevo umbral se guarda temporalmente
        }
//Copia los nuevos pesos y umbrales a los pesos y umbrales respectivos del perceptrón
        for (int capa = 2; capa <= TotalCapas; capa++)
            for (int i = 1; i <= neuronasporcapa[capa]; i++)
                U[capa][ i] = UN[capa][i];
        for (int capa = 1; capa < TotalCapas; capa++)
            for (int i = 1; i <= neuronasporcapa[capa]; i++)
                for (int j = 1; j <= neuronasporcapa[capa + 1]; j++)
                    W[capa] [i][ j] = WN[capa][i][j];
    }
}


