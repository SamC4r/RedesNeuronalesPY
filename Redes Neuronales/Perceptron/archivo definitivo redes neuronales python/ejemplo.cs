using System;
namespace Perceptron {
class Program {
 static void Main(string[] args){
 int[,] datos = { { 1, 1, 1 }, { 1, 0, 0 }, { 0, 1, 0 }, { 0, 0, 0 } }; //Tabla de verdad AND
 Random azar = new Random();
 double[] pesos = { azar.NextDouble(), azar.NextDouble(), azar.NextDouble() }; //Inicia los pesos al azar
 bool aprendiendo = true;
 int salidaEntera;
 while (aprendiendo){ //Hasta que aprenda la tabla AND
 aprendiendo = false;
 for (int cont = 0; cont <= 3 ; cont++){
 double salidaReal = datos[cont, 0] * pesos[0] + datos[cont,1] * pesos[1] + pesos[2]; //Calcula la salida real
 if (salidaReal>0) salidaEntera = 1; else salidaEntera = 0; //Transforma a valores 0 o 1
 if (salidaEntera != datos[cont, 2]) { //Si la salida no coincide con lo esperado, cambia los pesos al azar
 pesos[0] = azar.NextDouble() - azar.NextDouble();
 pesos[1] = azar.NextDouble() - azar.NextDouble();
 pesos[2] = azar.NextDouble() - azar.NextDouble();
 aprendiendo = true; //Y sigue buscando
 }
 }
 }
 for (int cont = 0; cont <= 3; cont++){ //Muestra el perceptron con la tabla AND aprendida
 double salidaReal = datos[cont, 0] * pesos[0] + datos[cont, 1] * pesos[1] + pesos[2];
 if (salidaReal > 0) salidaEntera = 1; else salidaEntera = 0;
 Console.WriteLine("Entradas: " + datos[cont,0].ToString() + " y " + datos[cont,1].ToString() + " = " +
 datos[cont,2].ToString() + " perceptron: " + salidaEntera.ToString());
 }
 Console.ReadLine();
 }
}
}