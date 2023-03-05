#include <iostream>
#include <stddef.h>
#include "QueueLL.h"

using namespace std;

//Linked List Functions
LL::LL()
{
	HEAD = NULL;
	TAIL = NULL;
}

LL::~LL()
{
}

bool LL::isEmpty()
{
	return HEAD == NULL;
}

void LL::addToHead(int data)
{
	node *newNode = new node();
	newNode->info = data;
	newNode->next = HEAD;
	HEAD = newNode;
	if (TAIL == NULL)
	{
		TAIL = HEAD;
	}
}

void LL::addToTail(int data)
{
	if (isEmpty())
	{
		addToHead(data);
	}
	else
	{
		node *newNode = new node();
		newNode->info = data;
		newNode->next = NULL;
		TAIL->next = newNode;
		TAIL = newNode;
	}
}

int LL::removeFromHead()
{
	node *deleteNode = new node();
	deleteNode = HEAD;
	int value = HEAD->info;
	HEAD = deleteNode->next;
	delete deleteNode;
	return value;
}

void LL::traverse()
{
	node *temp = HEAD;

	while (temp != NULL)
	{
		std::cout << temp->info << " ";
		temp = temp->next;
	}
}

//Queue Functions
void Queue::isEmpty()
{
	bool result = LS.isEmpty();
	if (result)
	{
		std::cout << "\nQueue is EMPTY!";
	}
	else
	{
		std::cout << "\nQueue is NOT EMPTY!";
	}
}

void Queue::enQueue(int data)
{
	LS.addToTail(data);
}

void Queue::showItems()
{
	return LS.traverse();
}

int Queue::deQueue()
{
	return LS.removeFromHead();
}

//Driver Module
int main()
{
	Queue object;
	int option, data;
	char proceed;
	std::cout << "\t\t\tQueue AS LINKED LIST\n";
	std::cout << "..............................................................." << endl
			  << "|  1. isEmpty     2. showItems     3. enQueue     4. deQueue  |" << endl
			  << "..............................................................." << endl;
	do
	{
		std::cout << endl
				  << "_________________________________________________________" << endl
				  << "Please choose the option from the top menu :: ";
		std::cin >> option;
		switch (option)
		{

		//Curly brackets {} used in cases to avoid compilation error in visual studio
		case 1:
		{
			object.Queue::isEmpty();
			break;
		}

		case 2:
		{
			std::cout << endl
					  << "The data in queue : ";
			object.showItems();
			break;
		}

		case 3:
		{
			std::cout << endl
					  << "Please enter the data to enqueue : ";
			std::cin >> data;
			object.enQueue(data);
			std::cout << "***" << data << " successfuLLy enqueued to Queue***";
			break;
		}

		case 4:
		{
			data = object.deQueue();
			std::cout << "***SuccessfuLLy dequeued " << data << " from Queue***";
			break;
		}

		default:
		{
			std::cout << endl
					  << "ERROR: Wrong Option!";
			break;
		}
		}

		std::cout << endl
				  << endl
				  << "DO YOU WANT TO CONTINUE (Y/N)?";
		std::cin >> proceed;
	} while (proceed == 'y' || proceed == 'Y');
	return 0;
}
