public class Customer {
    int integral;
    String card;
    void show(){
        System.out.println(String.format("积分：%d,卡类型：%s",integral,card));
        if ((card.equals("金卡")&&integral>1000)||(card.equals("普卡")&&integral>5000)){
            System.out.println("回馈积分500分！");
        }else{
            System.out.println("积分不足暂无回馈！");
        }
    }
}
