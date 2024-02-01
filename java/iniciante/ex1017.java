import java.io.IOException;
import java.util.Scanner;

public class ex1017 {
 
    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        int numA = leitor.nextInt(), numB = leitor.nextInt();
        System.out.println("PROD = "+numA*numB);

        leitor.close();
    }
 
}
