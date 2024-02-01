import java.io.IOException;
import java.text.DecimalFormat;
import java.util.Scanner;

public class ex3474 {
 
    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        
        Double valor = Double.parseDouble(leitor.next());
        int amigos = Integer.parseInt(leitor.next());
        
        DecimalFormat df = new DecimalFormat();
        df.applyPattern("#,##0.00");
        System.out.println(df.format(valor/amigos));

        leitor.close();
 
    }
 
}