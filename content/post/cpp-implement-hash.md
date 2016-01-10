+++
date = "2016-01-10T08:35:28+08:00"
draft = true
title = "cpp implement hash"

+++



<pre>

#include<iostream>
using namespace std;

class Pair{

public:
    char key;
    int value;

    Pair(char key, int value){
        this->key = key;
        this->value = value;
    }
};


class Hash{

public:
    int size;
    int capacity;
    Pair **pairs;

    Hash(){
        size = 0;
        capacity = 26;
        pairs = new Pair*[26];
    }

    int hash(char c){
        return (c-'a')%capacity;
    }

    void add(char key, int value){
        size++;
        int index = hash(key);
        pairs[index] = new Pair(key, value);
    }

    int query(char key){
        int index = hash(key);
        return pairs[index]->value;
    }

};


int main(){

    Hash *hash = new Hash();

    hash->add('a', 999);
    hash->add('d', 219);
    hash->add('c', 6165);
    
    for(int i=0; i<hash->capacity; ++i){
        if(hash->pairs[i]){
            char key = hash->pairs[i]->key;
            cout<<key<<" "<<hash->query(key)<<endl;
        }
    }

}

</pre>