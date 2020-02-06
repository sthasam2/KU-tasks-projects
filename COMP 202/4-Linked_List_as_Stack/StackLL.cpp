#include <iostream>
#include <stddef.h>
#include "StackLL.h"

using namespace std;

//Linked List Functions
LL::LL() {
								HEAD = NULL;
								TAIL = NULL;
}

LL::~LL() {
}

bool LL::isEmpty() {
								return HEAD == NULL;
}

void LL::addToHead(int data) {
								node* newNode = new node();
								newNode->info = data;
								newNode->next = HEAD;
								HEAD = newNode;
								if (TAIL == NULL) {
																TAIL = HEAD;
								}
}

void LL::addToTail(int data) {
								node* newNode = new node();
								newNode->info = data;
								newNode->next = NULL;
								TAIL->next = newNode;
								TAIL = newNode;
}

int LL::removeFromHead() {
								node* deleteNode = new node();
								deleteNode = HEAD;
								int value = HEAD->info;
								HEAD = deleteNode->next;
								delete deleteNode;
								return value;
}

void LL::traverse() {
								node* temp = HEAD;

								while (temp != NULL) {
																std::cout << temp->info << " ";
																temp = temp->next;
								}
}

int LL::itemHead() {
								if (isEmpty()) {
																cout << endl << "List is EMPTY";
								}
								else {
																int num = HEAD->info;
																return num;
								}
}


//Stack Functions
void Stack::isEmpty() {
								bool result = LS.isEmpty();
								if (result) {
																std::cout << "\nStack is EMPTY!";
								}
								else {
																std::cout << "\nStack is NOT EMPTY!";
								}
}

void Stack::push(int data) {
								LS.addToHead(data);
}

int Stack::top() {
								return LS.itemHead();
}

int Stack::pop() {
								return LS.removeFromHead();
}

//Driver Module
int main() {
								Stack object;
								int option, data;
								char proceed;
								std::cout << "\t\t\tSTACK AS LINKED LIST\n";
								std::cout << ".................................................." << endl <<
																"|  1. isEmpty     2. Top     3. Push     4. Pop  |" << endl <<
																".................................................." << endl;
								do {
																std::cout << endl << "_________________________________________________________" << endl <<
																								"Please choose the option from the top menu :: ";
																std::cin >> option;
																switch (option) {

																//Curly brackets {} used in cases to avoid compilation error in visual studio
																case 1: {
																								object.Stack::isEmpty();
																								break;
																}

																case 2: {
																								std::cout << endl << "The data at TOP : "<<object.top();
																								break;
																}

																case 3: {
																								std::cout << endl << "Please enter the data to push : ";
																								std::cin >> data;
																								object.push(data);
																								std::cout << "***" << data << " successfuLLy pushed to STACK***";
																								break;
																}

																case 4: {
																								data = object.pop();
																								std::cout << "***SuccessfuLLy popped " << data << " from Stack***";
																								break;
																}

																default: {
																								std::cout << endl << "ERROR: Wrong Option!";
																								break;
																}
																}

																std::cout << endl << endl << "DO YOU WANT TO CONTINUE (Y/N)?";
																std::cin >> proceed;
								} while (proceed == 'y' || proceed == 'Y');
								return 0;
}
