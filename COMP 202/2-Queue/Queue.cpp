#include <iostream>
#include "Queue.h"

using namespace std;

//function definition start
queue::queue(int size){
								elements = new char[size];
								capacity = size;
								front = -1;
								rear = -1;
								count = 0;
}

queue::~queue(){
								delete elements;
}

int queue::sizeQueue() {
								return capacity;
}

void queue::dequeue(){
								if (isEmpty()) {
																cout << "UnderFlow: Cannot remove element";
								}

								else {
																cout << "\\\\\\ Removing \"" << elements[front + 1] << "\" from queue \\\\\\\n";
																elements[front + 1] = NULL;
																front = (front + 1) % capacity;
																count--;
								}
}

void queue::enqueue(char item){
								if (isFull()) {
																cout << "OverFlow: Cannot add elements";
								}

								else {
																cout << "/// Inserting \"" << item << "\" to queue. ///\n";
																rear = (rear + 1) % capacity;
																elements[rear] = item;
																count++;
								}
}

char queue::peek(){
								if (isEmpty()) {
																cout << "UnderFlow: no elements\n";
								}
								return elements[front+1];
}

int queue::size(){
								return count;
}

int queue::getCurrentPosition() {
								return rear;
}

bool queue::isEmpty(){
								return (size() == 0);
}

bool queue::isFull(){
								return (size() == capacity);
}

void queue::displayQueue() {
								for (int i = 0; i < capacity; i++) {
																cout << i + 1 << ". " << elements[i]<<endl;
								}
}
//functon definition end

//main module start
int main(){
								queue a(5);
								cout << "Size of the Queue: " << a.sizeQueue() << endl;
								int i = 0;

								for (i; i < a.sizeQueue(); i++) {
																int option;
																std::cout << "\n\nELEMENT: " << i + 1 << endl;
																std::cout << "...........................................\n|  1. Enqueue     2. Dequeue     3. Peek  |\n...........................................\t\n->"; std::cin >> option;
																switch (option) {

																case 1: char data; std::cout << "Element no. " << i + 1 << "\tEnqueue element: "; std::cin >> data;
																								a.enqueue(data);
																								break;

																case 2:
																								a.dequeue();
																								i = a.getCurrentPosition(); //to correspond with loop since queue position changes but loop continues
																								break;

																case 3:
																								cout<<"||| Front Element of Queue: "<<a.peek()<<" |||"<<endl;
																								i = a.getCurrentPosition(); //to correspond with loop since stack position changes but loop continues
																								break;

																default:
																								std::cout << "Wrong option!" << endl;
																								i = a.getCurrentPosition(); //to correspond with loop since stack position changes but loop continues
																								break;
																}
								}

								cout << endl; a.displayQueue();
}
//main module end
