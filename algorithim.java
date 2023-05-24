import java.util.*;

public class algorithim{
    public static void main(String[] args){
       Scanner sc = new Scanner(System.in);

        System.out.println("input the number here: ");
        int int1 = sc.nextInt();
        int factorial = 1;
        int i;
        
        for(i=1; i<int1; i++){
            factorial *= i+1;
        }
        
        System.out.println("the factorial is: " + factorial);
    }
}