#coding=utf-8   #utf-8处理全球语言    gbk国标处理中文
# print "hello word"
# print 2**3
#####################################输出输入################################################
# 注释  注解 解释
#raw_input("请输入用户名")
#变量  保存任意长度   任意的数据
# x=50    #赋值
# y=2
# print x*y
# ###############定义变量规则
# #1.不能够以数字开头，可以是_或者字母开头，后面可以跟任意字符
# _q=1
# a_1=2
# #2.不能用系统关键字，print if for while。。。。。
# #3.定义变量的时候尽量清晰一些，一般用英文单词
#
# # name=raw_input("请输入你的名字：")
# # print name
# #############################################算术运算###############################################
# print 3+4
# print 3-4
# print 3*4
# print 3.0/4.0  #在python里面，如果是整数除以整数 结果就是整数，
# print 4//3   #取整  商
# print 3%4    #取余数
# print 3**4   #次方
# #优先级 右括号先算括号 乘方最高 ， 乘 除 取整 取余次之，最后是加减（从左至右）
# print 21//3**2-5%4
# ############################################比较运算#################################################
# #  <  >  >=  <=   ==  !=
# print 1<2
# print 1!=1
# print 3.12<=3.12
# ##############################################逻辑运算################################################
# #and逻辑与  or逻辑或   not取反
# print 1<2  and 2>3
# print 1<2  or  2>3
# print not 2<3
# #布尔值  true false
#
# ##############################################数据类型###############################################
# #int整型    float浮点型   str字符串   list列表  tuple元组  dict字典
# age="23.3"
# print type(age)     #查看变量是什么数据类型
# print "哈哈"+str(100)
# #强制转换 int()  float()  str()
# print int("123")
# #字符串 '  "   """
# s="a"
# ss='1.增加 2.修改  3.删除 '
# sss='''aaaa'''
# #单双引号不能换行  字符只能在一行；三引号可以换行打印
# print """
# 1.增加
# 2.修改
# 3.删除
# """
# print "aaaa"+"""dddd"""  #拼接  连接的意思
# ##################计算100-999任意数字的百位 十位 个位数##########################################
# x=456
# print "个位数是",x%10      #逗号是不换行打印，吧所有的数据显示在一行
# print "十位数是",x//10%10
# print "百位数是",x//100

#####################################条件判断##############################################################
#如果  条件成立的时候   去做什么   否则 去干什么
#单分支
# name=raw_input("请输入你的名字：：")
# if name=="王思聪":
#     print "国民老公"
#双分支
# name=raw_input("请输入你的名字：：")
# if name=="王思聪":
#     print "国民老公"
# else:
#     print "你就是一个屌丝"
#多分支
# score=raw_input("请输入你的分数:")
# score=int(score)
# if   score<60:
#     print "不及格"
# elif score==60:
#     print  "刚好及格"
# elif  60<score<=80:
#     print  "良好"
# elif  80<score and  score<=99:
#     print "优秀"
# else:
#     print "满分"
#if嵌套
# score=raw_input("请输入你的分数:")
# score=int(score)
# if 0<=score<101:
#     if   score<60:
#         print "不及格"
#     elif score==60:
#         print  "刚好及格"
#     elif  60<score<=80:
#         print  "良好"
#     elif  80<score and  score<=99:
#         print "优秀"
#     else:
#         print "满分"
# else:
#     print "不要瞎输入"
##############################################练习##################################################33
#计算输入的某一年 是否为闰年，是则打印闰年；不是则打印平年
#能被4整数但是不能被100整除  或者能够被400整除
# while 1==1:
#     year=raw_input("请输入一个年份：")
#     year=int(year)
#     if year%4==0 and year%100!=0 or year%400==0:
#         print year,"闰年"
#     else:
#         print year,"平年"
#第二题目  输入三个数字   判断能不能组成三角形 ，并且告诉我是什么样的三角形（直角，等腰 等边 不规则）
# while 1:
#     a=raw_input("请输入a:")
#     b=raw_input("请输入b:")
#     c=raw_input("请输入c:")
#     a=int(a)
#     b=int(b)
#     c=int(c)
#     if a>0 and b>0 and c>0:
#         if a+b>c and a+c>b and b+c>a:
#             if a==b==c:
#                 print "等边三角形"
#             elif a==b!=c or a==c!=b or b==c!=a:
#                 print "等腰三角形"
#             elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#                 print "直角三角形"
#             else:
#                 print "不规则三角形"
#         else:
#             print "不能构成三角形"
#     else:
#         print "请输入整数"

#############################################循环###########################################################
# i=5
# while i>0:
#     print i
#     i-=1 #i=i-1

# i=5
# while i>0:
#     print i
#     i=i-1
#     if i==2:
#         break   #终止循环

#for循环
# for i  in range(10):
#     print i
# #for 区间
# for i in range(10,15):
#     print i
# #for 步长
# for i in range(1,10,3):
#     print i
# #for嵌套
# for i in range(3):
#     for j in range(4):
#         for k in range(2):
#             print i,j,k
# #嵌套if
# for i in range(10):
#     print i
#     if i==5:
#         break
################################打印九九乘法表###################################
# for i in range(1,10):
#     for j in range(i,10):
#         print i,"*",j,"=",i*j,'\t',
#     print ""

#水仙花数  153=1**3+5**3+3**3
#100-999之间还有多少个数符合这种条件
# for i in range(100,1000):
#     if (i//100)**3 + (i//10%10)**3 + (i%10)**3==i:
#         print i

#计算1 2 3 4  能组成多少个不重复的三位数，并且把三位数打印出来？
# for i in range(1,5):
#     for j in range(1, 5):
#         for g in range(1, 5):
#             if i!=j!=g!=i:
#                 print i*100+j*10+g
#
#print len("￥")   #在utf-8编码下，一个中文3位长度；其他编码就2位
#####################################################作业####################################################
#设计一个系统；注册登录的功能；
#注册的字段（用户名、密码、确认密码） 用户名6-10位；密码6-10位；密码跟确认密码一致，提示用户注册成功
#友好的设计 某个字段输错了 提示用户 让他输对了为止
#登录功能 先注册才能登陆，
#登录用刚刚注册的用户名和密码去登录就行了，如果用户名密码都正确，提示用户登录成功
#登录三次机会，超过三次程序终止运行
while 1:
    print""" 1.注册   2.登录"""
    choose=raw_input("请选择：")
    if choose=='1':
        print "注册功能"

    elif choose=='2':
        print "登录功能"

    else:
        print "没有这个选项，请重试"


