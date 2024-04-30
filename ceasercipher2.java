// Transpositional: 
// import java.util.Arrays;
import java.util.Scanner;

public class ceasercipher2 {
   public static void main(String[] args) {
       Scanner sc=new Scanner(System.in);
       System.out.println("Enter the String to be encrypted");
       String str=sc.nextLine();
       int row= (int) Math.floor(Math.sqrt(str.length()));
       int col=str.length()/row;
       if(row*col<str.length()){
           col++;
       }
       int index=0;
       char[][] transpositionArr=new char[row][col];
       for(int i=0;i<row;i++){
           for(int j=0;j<col;j++){
               if (index < str.length()) {
                   transpositionArr[i][j] = str.charAt(index++);
               } else {
                   transpositionArr[i][j] = ' ';
               }
       }}
       for(int i=0;i<row;i++){
           for(int j=0;j<col;j++){
               System.out.print(transpositionArr[i][j]+" ");
           }
           System.out.println();}
       System.out.println("Encrypted string is:");
       for(int i=0;i<col;i++){
           for(int j=0;j<row;j++){

               System.out.print(transpositionArr[j][i]);
           }
       }System.out.println();
System.out.println("Decrypted string is:");
for (int i = 0; i < row; i++) {
   for (int j = 0; j < col; j++) {
       System.out.print(transpositionArr[i][j]);
   }
}
    sc.close();
   }
}
