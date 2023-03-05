#include <iostream>
#include "stack.h"

using namespace std;

//definitions start

stack::stack()
{
	topp = -1;
}

stack::~stack()
{
}

bool stack::isFull()
{
	return topp == (MAX_STACK_SIZE - 1);
}

bool stack::isEmpty()
{
	return topp < 0;
}

void stack::push(int element)
{
	if (isFull())
	{
		std::cout << "Cannot push" << element << ".Stack is full";
	}
	else
	{
		topp++;
		this->elements[topp] = element;
	}
}

int stack::pop()
{
	if (isEmpty())
	{
		std::cout << "Stack Empty. Cannot pop.";
	}
	else
	{
		return elements[topp--];
	}
}

int stack::top()
{
	if (!isEmpty())
		return elements[topp];
	else
	{
		return elements[topp];
	}
}

void stack::displayStack()
{
	int i = 0;
	std::cout << "STACK:\n";
	for (i; i < MAX_STACK_SIZE; i++)
	{
		std::cout << i + 1 << ". " << elements[i] << endl;
	}
}

void stack::sizeStack()
{
	std::cout << "Size of stack: " << MAX_STACK_SIZE << endl;
}

int stack::getCurrentPosition()
{
	return topp;
}

//definitions end

int main()
{
	stack a;
	a.sizeStack();
	int i = 0;
	for (i; i < MAX_STACK_SIZE; i++)
	{
		int option;
		std::cout << "\n\nELEMENT: " << i + 1 << endl;
		std::cout << "..................................." << endl
				  << "|  1. Push     2. Pop     3. Peek |" << endl
				  << "..................................."
					 "\t\n->";
		std::cin >> option;
		switch (option)
		{

		case 1:
			int data;
			std::cout << "Element no. " << i + 1 << "\tPush element: ";
			std::cin >> data;
			a.push(data);
			if (!a.isFull())
				std::cout << "/// Pushed " << data << " ///";
			break;

		case 2:
			if (a.isEmpty())
			{
				std::cout << "Stack empty, cannot pop." << endl;
			}
			else
			{
				std::cout << "\\\\\\ Popped data of element " << i << ": " << a.pop() << " \\\\\\" << endl;
			}
			i = a.getCurrentPosition(); //to correspond with loop since stack position changes but loop continues
			break;

		case 3:
			std::cout << "Top element: ";
			if (!a.isEmpty())
				std::cout << a.top() << endl;
			else
				std::cout << "Stack Underflow";
			i = a.getCurrentPosition(); //to correspond with loop since stack position changes but loop continues
			break;

		default:
			std::cout << "Wrong option!" << endl;
			i = a.getCurrentPosition(); //to correspond with loop since stack position changes but loop continues
			break;
		}
	}

	cout << endl;
	a.displayStack();
}
