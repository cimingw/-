public class TestTelephone {
    public static void main(String[] args) {
        /**
         * 创建对象的方法
         * 语法形式；类名 对象名=new 类名();
         */
        Telephone telephone=new Telephone();
        telephone.name="华为";
        telephone.price=5000;
        telephone.cupSize=8;
        telephone.screenSize=6;
        telephone.call();
    }
}
