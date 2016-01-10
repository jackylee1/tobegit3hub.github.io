+++
date = "2013-02-27T08:35:28+08:00"
draft = true
title = "cpp foreach syntax"

+++



<pre>
#include<iostream>
using namespace std;
    
int main(){
  int array[] = {1,22, 1992};
    
  for(auto i : array){
            cout<<i<<endl;
  }          
}
</pre>


奇葩语法配奇葩编译选项：  

`g++ foreach.cpp -std=c++0x`