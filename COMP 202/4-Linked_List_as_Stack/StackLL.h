#ifndef StackLL_h
#define StackLL_h

#include <iostream>

class node {
public:
node() {
};
int info;
node* next;
};

class LL {
public:
//constructors
LL();
~LL();

//functons
bool isEmpty();

void addToHead(int data);
void addToTail(int data);

int removeFromHead();

void traverse();
int itemHead();

private:
node* HEAD;
node* TAIL;
};

class Stack {
private:
LL LS;

public:
void isEmpty();
void push(int data);
int top();
int pop();
};

#endif
