import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class ex1259 {

    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        int entradas = leitor.nextInt(); 
        ArrayList<Integer> numerosPares = new ArrayList<Integer>(); 
        ArrayList<Integer> numerosImpares = new ArrayList<Integer>();
        for (int i = 0; i < entradas; i++) {
            int numero = leitor.nextInt();
            if (numero % 2 == 0) {
                numerosPares.add(numero);
            } else {
                numerosImpares.add(numero);
            }
        }
        leitor.close();
        Collections.sort(numerosPares);
        Collections.sort(numerosImpares, Collections.reverseOrder());
        for(int i : numerosPares){
            System.out.println(i);
        }
        for(int i : numerosImpares){
            System.out.println(i);
        }

    }

}