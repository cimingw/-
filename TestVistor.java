import java.util.Scanner;

public class TestVistor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Visitor visitor = new Visitor();
        while (true) {
            System.out.print("请输入姓名：");
            visitor.name = scanner.next();
            if (visitor.name.equals("n")) {
                visitor.age = 0;
                visitor.charge();
                break;
            }
            System.out.print("请输入年龄：");
            visitor.age = scanner.nextInt();
            visitor.charge();
        }
    }
}
