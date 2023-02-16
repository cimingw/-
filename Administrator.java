public class Administrator {
    String name;
    int password;
    void read(){
        if(name.equals("admin1") && password==111111){
            System.out.println();
            System.out.print("请输入新密码:");
        }else{
            System.out.println("用户名和密码不正确！");
            System.exit(0);
        }
    }
}
