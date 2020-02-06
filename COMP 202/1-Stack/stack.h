#ifndef stack_H
#define stack_H

#define MAX_STACK_SIZE 5

class stack {
public:
//constructors
stack();
~stack();

//functions
void push(int element);
int pop();
int top();
bool isEmpty();
bool isFull();
void displayStack();
void sizeStack();
int getCurrentPosition();

private:
int elements[MAX_STACK_SIZE];
int element;

protected:
int topp;
};

#endif
