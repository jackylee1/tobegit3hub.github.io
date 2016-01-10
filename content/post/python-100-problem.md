+++
date = "2012-12-28T08:35:27+08:00"
draft = true
title = "python 100 problem"

+++



第1题：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

<pre>
# -*- coding: utf-8 -*-
#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
count = 0

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                count += 1
                print "The number =", i*100+j*10+k
        
print "Count =", count
</pre>

第2题：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润>高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的>部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

<pre>
# -*- coding: utf-8 -*-
#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润>高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的>部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
        
salaryLevel = [1000000, 600000, 400000, 200000, 100000, 0]
rateLevel = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
                
def calculateSalary(originalSalary):
    newSalary = originalSalary
    for i in range(6):
        if originalSalary > salaryLevel[i]:
            newSalary += originalSalary * rateLevel[i]
            return newSalary

print "When 100000, newSalary =", calculateSalary(100000)
print "When 100001, newSalary =", calculateSalary(100001)
</pre>

第3题：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问>该数是多少？

<pre>
# -*- coding: utf-8 -*-
#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问>该数是多少？

import math

for i in range(1024):
    if (int(math.sqrt(i+100))**2 == i+100) and (int(math.sqrt(i+168))**2 == i+168):
        print "The number =", i
        print "The number+100 =", i+100
        print "The number+168 =", i+168
</pre>

第4题：输入某月某日，判断这一天是这一年的第几天？(非润年）

<pre>
# -*- coding: utf-8 -*-
#题目：输入某月某日，判断这一天是这一年的第几天？(非润年）

daysOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

def calculateDays(month, day):
    days = 0
    for i in range(12):
        if month-1 > i:
            days += daysOfMonth[i]
    days += day
    return days

print "1/10 =", calculateDays(1, 10)
print "2/10 =", calculateDays(2, 10)
</pre>

第5题：输入三个整数x,y,z，请把这三个数由小到大输出。

<pre>
# -*- coding: utf-8 -*-
#题目：输入三个整数x,y,z，请把这三个数由小到大输出。

def sort(array):
    return sorted(array)

print "1, 3, 2 =", sort((1,3,2))
print "6, 5, 4 =", sort((6,5,4))
</pre>

第8题：输出9*9口诀。

<pre>
# -*- coding: utf-8 -*-
#题目：输出9*9口诀。

for i in range(1,10):
    for j in range(1,10):
        print i,"*",j,"=",i*j
    print " "
</pre>

第11题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

<pre>
# -*- coding: utf-8 -*-
#题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三
个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

def fibonacci(number):
    if (number==1) or (number==2):
        return 1
    else:
        return fibonacci(number-2) + fibonacci(number-1)

print "Fibonacci(3) =", fibonacci(3)
print "Fibonacci(5) =", fibonacci(5)
</pre>

第12题：判断101-200之间有多少个素数，并输出所有素数。

<pre>
# -*- coding: utf-8 -*-
#题目：判断101-200之间有多少个素数，并输出所有素数。

import math

for i in range(2,1024):
    isPrime = True
    medium = int(math.sqrt(i))
        
    for j in range(2, medium+1):
        if i%j==0:
            isPrime = False
            break
    if isPrime:
        print "Prime number =", i
</pre>

第13题：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等>于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。

<pre>
# -*- coding: utf-8 -*-
#题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等>于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。

for i in range(100,1000):
    first = int(i/100)
    second = int((i-100*first)/10)
    third = i-100*first-10*second
        
    if i == first**3 + second**3 + third**3:
        print "Daffodil number =", i
</pre>

第14题：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

<pre>
# -*- coding: utf-8 -*-
#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

def decompose(number):
    while number!=1:
        for i in range(2,number+1):
            if number%i == 0:
                number /= i
                print i
                break
print "6 =", decompose(6)
print "24 =", decompose(24)
</pre>

第15题：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间>的用B表示，60分以下的用C表示。

<pre>
# -*- coding: utf-8 -*-
#题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间>的用B表示，60分以下的用C表示。

def calculateLevel(score):
    grade = "C"
    if score >= 90:
        grade = "A"
    elif score >= 60: 
        grade = "B"
    else:
        grade = "C"
    return grade

print "95 =", calculateLevel(95)
print "55 =", calculateLevel(55)
</pre>

第17题：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

<pre>
# -*- coding: utf-8 -*-
#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

def calculateCharacters(string):
    letter = 0
    digit = 0
    space = 0
    other = 0 
    
    for char in string:
        if char.isalpha():
            letter += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        else:
            other += 1
    
    print "Letter =", letter
    print "Digit =", digit
    print "Space =", space
    print "Other =", other

if __name__ == "__main__":
    calculateCharacters("Hello Gal, I'm 43")
</pre>