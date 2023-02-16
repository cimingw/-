import java.util.Scanner;

public class TestAdministrator {
    public static void main(String[] args) {
        Administrator administrator=new Administrator();
        Scanner scanner=new Scanner(System.in);
        System.out.print("请输入用户名:");
        administrator.name=scanner.next();
        System.out.print("请输入密码:");
        administrator.password=scanner.nextInt();
        administrator.read();
        administrator.password= scanner.nextInt();
        System.out.print("修改密码成功");
    }
}

