'''
基本数据类型转换规则:
str(x)将x的内容数据类型容转换为字符串
int(x)将x的内容数据类型容转换为整数
float(x)将x的内容数据类型容转换成浮点数
三种之间不可以随意转换：字符串转数值，必须是字符串内容是数值。
input():接收用户用户终端(键盘)的输入，输入的数据类型是字符串
print(打印多个内容用逗号分开。一个逗号表示一个空格)
格式化字符串%d 格式化输出整数,%f 格式化输出小鼠,%e 科学技术法
format()
布尔型：bool
预习：
Python逻辑运算（算术运算、高级赋值、比较运算、逻辑运算、运算符优先级）
Python逻辑结构(if for while contine break)
'''
# age=18
# name="zhaojixiang"
# print(age,name)
# schoolMotto="修德、长技、求真、尚美"
# print(schoolMotto)
# print("I\'am a good student.")
# print(('she said:"youa are good student'))
# print("修德、长技、\n求真、尚美.")
r=input("请输入半径：")
r=int(r)
circumference=2*3.14*r
area=3.14*r**2
print("圆的面积：%.2f,圆的周长是:%.2f"%(area,circumference))
print("圆的面积：{},圆的周长是:{}".format(area,circumference))