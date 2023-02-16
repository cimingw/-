import java.util.Scanner;

public class TestCustomer {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        Customer customer=new Customer();
        customer.integral= scanner.nextInt();
        customer.card= scanner.next();
        customer.show();
    }
}
