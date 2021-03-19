package Perceptron;

public class Main {
    


    public static void main(String[] args) {
          
      
            int TotalEntradas = 2; //Número de entradas externas del perceptrón
            int TotalSalidas = 1; //Número de salidas externas del perceptrón
            int TotalCapas = 4; //Total capas que tendrá el perceptrón
            int[] neuronasporcapa = new int[TotalCapas + 1]; //Los índices iniciarán en 1 en esta implementación
            neuronasporcapa[1] = TotalEntradas; //Entradas externas del perceptrón
            neuronasporcapa[2] = 4; //Capa oculta con 4 neuronas
            neuronasporcapa[3] = 4; //Capa oculta con 4 neuronas
            neuronasporcapa[4] = TotalSalidas; //Capa de salida con 2 neuronas
            MultiLayer objP = new MultiLayer(TotalEntradas, TotalSalidas, TotalCapas, neuronasporcapa);
            
/* Tabla del XOR. Son 4 conjuntos de entradas y salidas
1 ..... 1 ===> 0
1 ..... 0 ===> 1
0 ..... 1 ===> 1
0 ..... 0 ===> 0
*/
            int ConjuntoEntradas = 4;
            double[][] entraXOR = new double[ConjuntoEntradas+1][];
            entraXOR[1] = new double[3];
            entraXOR[2] = new double[3];
            entraXOR[3] = new double[3];
            entraXOR[4] = new double[3];
            entraXOR[1][1] = 1; entraXOR[2][1] = 1; entraXOR[3][1] = 0; entraXOR[4][1] = 0;
            entraXOR[1][2] = 1; entraXOR[2][2] = 0; entraXOR[3][2] = 1; entraXOR[4][2] = 0;
            double[][] salirXOR = new double[ConjuntoEntradas+1][];
            salirXOR[1] = new double[3];
            salirXOR[2] = new double[3];
            salirXOR[3] = new double[3];
            salirXOR[4] = new double[3];
            salirXOR[1][1] = 0; salirXOR[2][1] = 1; salirXOR[3][1] = 1; salirXOR[4][1] = 0;
            double alpha = 0.4; //Factor de aprendizaje
//Ciclo que entrena la red neuronal
            for (int ciclo = 1; ciclo <= 8000; ciclo++) {
                if (ciclo % 500 == 0) System.out.println("Iteracion: " + ciclo);
//Importante: Se envía el primer conjunto de entradas-salidas, luego el segundo, tercero y cuarto
//por cada ciclo de entrenamiento.
                for (int entra = 1; entra <= ConjuntoEntradas; entra++) {
                    objP.Procesa(entraXOR[entra]);
                    if (ciclo % 500 == 0) {
                        objP.Muestra(entraXOR[entra], salirXOR[entra]);
                        objP.Entrena(alpha, entraXOR[entra], salirXOR[entra]);
                    }
                }
            }
            //Console.ReadKey();
        }


}


/*
*
0.0,
1.0,
 =
1.0,
 <vs>
1, 0.5224026656551004
0.0,
0.0,
 =
0.0,
 <vs>
1, 0.5658563228148856
Iteracion: 5000
1.0,
1.0,
 =
0.0,
 <vs>
1, 0.5159712861265078
1.0,
0.0,
 =
1.0,
 <vs>
0, 0.4636503879620711

0.0,
1.0,
 =
1.0,
 <vs>
1, 0.5166176382352089
0.0,
0.0,
 =
0.0,
 <vs>
1, 0.5608201451472433
Iteracion: 5500
1.0,
1.0,
 =
0.0,
 <vs>
1, 0.511086146206718
1.0,
0.0,
 =
1.0,
 <vs>
0, 0.4593347783204399

0.0,
1.0,
 =
1.0,
 <vs>
1, 0.512582719585149
0.0,
0.0,
 =
0.0,
 <vs>
1, 0.5572883189257729
Iteracion: 6000
1.0,
1.0,
 =
0.0,
 <vs>
1, 0.5076832147798358
1.0,
0.0,
 =
1.0,
 <vs>
0, 0.45634489411646784

0.0,
1.0,
 =
1.0,
 <vs>
1, 0.5097704215018004
0.0,
0.0,
 =
0.0,
 <vs>
1, 0.5548131660452388
Iteracion: 6500
1.0,
1.0,
 =
0.0,
 <vs>
1, 0.5053140150961328
1.0,
0.0,
 =
1.0,
 <vs>
0, 0.4542740262945868

0.0,
1.0,
 =
1.0,
 <vs>
1, 0.507810720007006
0.0,
0.0,
 =
0.0,
 <vs>
1, 0.5530778119195654
Iteracion: 7000
1.0,
1.0,
 =
0.0,
 <vs>
1, 0.5036650248569571
1.0,
0.0,
 =
1.0,
 <vs>
0, 0.452840836881726

0.0,
1.0,
 =
1.0,
 <vs>
1, 0.5064450937309127
0.0,
0.0,
 =
0.0,
 <vs>
1, 0.5518594038208798
Iteracion: 7500
1.0,
1.0,
 =
0.0,
 <vs>
1, 0.5025176078450869
1.0,
0.0,
 =
1.0,
 <vs>
0, 0.4518505197463749

0.0,
1.0,
 =
1.0,
 <vs>
1, 0.5054932693120314
0.0,
0.0,
 =
0.0,
 <vs>
1, 0.5510017992504718
Iteracion: 8000
1.0,
1.0,
 =
0.0,
 <vs>
1, 0.5017194626660763
1.0,
0.0,
 =
1.0,
 <vs>
0, 0.4511680241455487

0.0,
1.0,
 =
1.0,
 <vs>
1, 0.5048296483572157
0.0,
0.0,= 0.0,<vs> 1, 0.5503958408741655
*
*
* */
