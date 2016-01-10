+++
date = "2012-12-29T08:35:27+08:00"
draft = true
title = "solve einstain problem"

+++



## 积分设计模式

积分设计模式是我在解决爱因斯坦大难题时用到的方法，觉得确实是一种编程的思路，就分享一下。

## “爱因斯坦大难题”

究竟什么是爱因斯坦大难题呢？听起来好像很高级，其实与相对论无关，也叫Zebra Puzzle，就是我们都玩过的数学智力游戏，题目即有五个不同国籍的人居住在五幢不同颜色的房子，他们各有自己不同的心爱的动物（如马，斑马，狗等）喝不同的饮料，和抽不同的香烟。现在已知：

1. 英国人住在红房子里。
2. 西班牙人喜欢养狗。
3. 绿房子的主人喜欢喝咖啡。
4. 乌克兰人喜欢喝茶。
5. 绿房子在白房子的右边。（从读者的方向看，以下相同）
6. 抽“万宝路”牌香烟的人养蜗牛。
7. 黄房子的主人抽“可乐”牌香烟。
8. 当中那幢房子的主人喝牛奶。
9. 挪威人住在左边第一幢房子。
10. 抽“本生”牌香烟的人和养狐狸的人是隔壁邻居。
11. 抽“可乐”牌香烟的人和养马的人是隔壁邻居。
12. 抽“肯特”牌香烟的人喝橘子水。
13. 日本人抽“摩尔”牌香烟。
14. 挪威人和蓝房子的主人是隔壁邻居

从以上的14重情况判断：谁是喝水的人？谁是养斑马的人？

## 解决办法

手工做：我用的是国外网上介绍的Shrinking Table（应该译作收缩表吧），两个小时可以"缩"出来。

编程解决：我也是用了两个小时来编程，就是用到了积分模式（这里插一句，我用排列算法穷举了所有情况，大概遍历了三千亿次循环，结果在Linux下最优编译跑了20分钟，Windows下跑了半个小时后死机）。

## 编程解决

唉，废话太多了（这里又一句），讲讲编程思路吧。

因为每次对以上14种情况都要判断，而且每次都至少有几种条件符合，然后穷举出来的两种情况前后又不能互相干扰。所以我在每次判断是否为解前（即是否同时满足14种条件），设置了个score变量，进入判断时若条件满足score++，最后判断如果score为14则为正解，否则重置为0继续遍历（很简单吧，我也不知道这算不算一种designpattern，但是当时能想到用这个觉得还是挺不错的，就一思路而已）。</p>

### 排列算法

这里所说的积分模式是用暴力算法解决的（一千二百亿次的循环，本机Windows运行了一个多小时），也就是穷举了所有情况从而找出所要的结果。首先第一步，就是排列，C++实现代码如下。

<pre>
#include <stdio.h>
#include <algorithm>

int a[4];

void perm(int l, int r)
{
    if (l == r) {
        for (int i = 0; i <= r; i++)
		{
			printf("%d ", a[i]);
		}
        puts("");
        return;
    }
    for (int i = l; i <= r; i++) {
        std::swap(a[l], a[i]);
        perm(l + 1, r);
        std::swap(a[l], a[i]);
    }
}

int main()
{
    for (int i = 0; i < 4; i++)
        a[i] = i + 1;
    perm(0, 3);
}
</pre>

### 算法思路

首先，对所给的自然语言的数据进行编号，如下图。

![](/images/einstein-problem-solutiont.jpg)

同时，要对所给条件进行编号的转化。

然后在多次A55的循环中判断是否符合条件，里面还有遍历5次的循环来找到相应的国籍或者宠物。

最后利用积分找到真正的答案。

### 输出结果

最终答案:挪威人喝水，日本人养斑马。

![](/images/einstein-problem-output.jpg)

### 源代码

<pre>
/*
 * author : tobe
 * date : 2012.6.12
 * problem : Zebra Puzzle
 *
 */


#include<iostream>
#include <algorithm>
using namespace std;


int a[5];		//用原有的排列函数所需要的数组

int indexOfPossibility = 0;		//表示第几种可能组合
int nation[120][5];		//表示nation的A55全排列（共120种），二维数组下表才表示每种情况下的国家组合
int color[120][5];
int animal[120][5];
int drink[120][5];
int cigarette[120][5];


void perm(int l, int r)
{
    if (l == r) {
        for (int i = 0; i <= r; i++)
		{
			//printf("%d ", a[i]);		//输出排列结果

			nation[indexOfPossibility][i] = a[i];		//为每种可能情况赋值
			color[indexOfPossibility][i] = a[i];
			animal[indexOfPossibility][i] = a[i];
			drink[indexOfPossibility][i] = a[i];
			cigarette[indexOfPossibility][i] = a[i];

		}

        //puts("");		//换行

		indexOfPossibility++;		//转移到下一种可能的情况(从0到119共120种可能情况)

        return;
    }

    for (int i = l; i <= r; i++) {
        swap(a[l], a[i]);		//递归调用，并且缩小了范围
        perm(l + 1, r);
        swap(a[l], a[i]);
    }
}


int main()
{
    for (int i = 0; i < 5; i++)
        a[i] = i;
    perm(0, 4);		//使用排列算法为各种可能情况初始化

	/*
	for(int i=0;i<120;++i){
		for(int j=0;j<5;++j){
			cout<<cigarette[i][j]<<" ";
		}
		cout<<endl;
	}
	*/


	int score = 0;

	cout<<"