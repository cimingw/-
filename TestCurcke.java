import java.util.Scanner;

public class TestCurcke {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        Curcke curcke=new Curcke();
        curcke.radius=sc.nextInt();
        curcke.area();
    }
}
