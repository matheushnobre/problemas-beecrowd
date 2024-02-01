import java.util.Scanner;
import java.util.Stack;

public class ex1024 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        //pegando número de entradas
        int entradas = Integer.parseInt(input.nextLine());
        String palavras[] = new String[entradas];
        
        //pegando palavras
        for(int i=0; i<entradas; i++){
            palavras[i] = input.nextLine();
        }
        
        //imprimindo palavras
        for(int i=0; i<entradas; i++){
            System.out.println(criptografarPalavra(palavras[i]));
        }

        input.close();
    }
    
    static String criptografarPalavra(String palavra){
        Stack<String> palavraCriptografadaPilha; //cria uma pilha que irá nos auxiliar na 2º passagem pelo texto
        palavraCriptografadaPilha = new Stack<String>();
        String palavraAuxiliar = ""; //palavra auxiliar que irá ajudar na 3º passagem pelo texto
        String palavraCriptografadaString = "";
        
        //1º passagem pelo texto
        for(int i=0; i<palavra.length(); i++){
            int caractere = palavra.charAt(i);
            if(caractere >= 65 && caractere <= 90 || caractere >= 97 && caractere <= 122){
                caractere += 3;
            }
            String caractereAdicionado = ""+(char)caractere;
            palavraCriptografadaPilha.add(caractereAdicionado);
        }
        
        //2º passagem pelo texto
        while(!palavraCriptografadaPilha.isEmpty()){
            palavraAuxiliar += palavraCriptografadaPilha.pop();
        }
        
        //3º passagem pelo texto
        palavraCriptografadaString = palavraAuxiliar.substring(0, palavraAuxiliar.length()/2);
        for(int i = palavraAuxiliar.length()/2; i<palavraAuxiliar.length(); i++){
            int caractere = palavraAuxiliar.charAt(i) - 1;
            palavraCriptografadaString += (char) caractere;
        }
        
        return palavraCriptografadaString;
    }
    
}
