import java.io.IOException;
import java.util.Scanner;
import java.text.DecimalFormat;

public class ex1036 {
 
    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        
        double a=Double.parseDouble(leitor.next()), b=Double.parseDouble(leitor.next()), c=Double.parseDouble(leitor.next()); //declaração e atribuição das variaveis que representam os coeficientes da equação

        if(a==0 || b*b-4*a*c<0){ //verificando se é possivel realizar os calculos. se o a for igual a zero ou o delta for negativo, não é possivel
            System.out.println("Impossivel calcular");
        }
        else{ //condição caso seja possivel realizar o calculo
            DecimalFormat df = new DecimalFormat("0.00000"); //iremos utilizar o double com 5 casas decimais
            System.out.println("R1 = "+df.format((-b + Math.sqrt(b*b - 4*a*c))/(2*a))); //faz o cálculo do x1 e arredonda para 5 casas decimais após a virgula, além de imprimir o resultado na tela
            System.out.println("R2 = "+df.format((-b - Math.sqrt(b*b - 4*a*c))/(2*a))); //faz o cálculo do x2 e arredonda para 5 casas decimais após a virgula, além de imprimir o resultado na tela
        }

        leitor.close();
    }
 
}