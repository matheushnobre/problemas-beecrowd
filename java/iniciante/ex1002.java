import java.io.IOException;
import java.util.Scanner; 
import java.text.DecimalFormat;

public class ex1002 {
 
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        
        double raio = Double.parseDouble(input.next());
        DecimalFormat df = new DecimalFormat("0.0000");
        //df.setMaximumFractionDigits(4);
        
        System.out.println("A="+df.format(3.14159 * (raio*raio)));

        input.close();
    }
 
}