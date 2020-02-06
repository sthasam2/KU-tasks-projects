#ifndef QueueLL_h
#define QueueLL_h

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

private:
node* HEAD;
node* TAIL;
};

class Queue {
private:
LL LS;

public:
void isEmpty();
void enQueue(int data);
void showItems();
int deQueue();
};

#endif
