public class Visitor {
    String name;
    int age;
/*
void 表示方法的返回值类型为空，就是方法内部不需要有返回的东西，这个方法本质上是一个操作。方法内部没有return
charge() charge方法名
 */
    void charge() {
        if (age == 0) {
            System.out.println("退出程序");
        } else if (age <= 18 || age >= 60) {
            System.out.println(String.format("%s的年龄为:%d,门票免费", name, age));
            System.out.println();
        } else {
            System.out.println(String.format("%s的年龄为:%d,门票20元", name, age));
            System.out.println();
        }
    }
}
