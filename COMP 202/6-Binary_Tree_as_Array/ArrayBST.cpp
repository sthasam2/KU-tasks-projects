#include <iostream>
#include "ArrayBST.h"
using namespace std;

ArrayBST::ArrayBST()
{
	for (int i = 0; i < 20; i++)
	{
		this->array[i] = 0;
	}
}
ArrayBST::~ArrayBST()
{
}

void ArrayBST::addData(int data)
{

	if (this->array[0] == 0)
	{
		this->array[1] = data;
	}
	else
	{
		for (int i = 1; i <= 20;)
		{
			if (data < this->array[i])
			{
				i = 2 * i;
			}
			else
			{
				i = 2 * i + 1;
			}
			if (this->array[i] == 0)
			{
				this->array[i] = data;
				break;
			}
		}
	}
	this->array[0] = this->array[0] + 1;
}

void ArrayBST::preorderTraversal()
{
	int i = 1;
	cout << "The pre-order traversal of the tree is ";
	cout << array[i];
	preordertraversal(get_left_child(i));
	preordertraversal(get_right_child(i));
	cout << endl;
}

void ArrayBST ::preordertraversal(int index)
{
	if (index != -1)
	{
		cout << ", " << array[index];
		preordertraversal(get_left_child(index));
		preordertraversal(get_right_child(index));
	}
}

void ArrayBST::inorderTraversal()
{
	int i = 1;
	cout << "The in-order tranversal of the tree is ";
	inorder_traversal(get_left_child(i));
	cout << array[i] << ", ";
	inorder_traversal(get_right_child(i));
	cout << endl;
}

void ArrayBST ::inorder_traversal(int index)
{
	if (index != -1)
	{
		inorder_traversal(get_left_child(index));
		cout << array[index] << ", ";
		inorder_traversal(get_right_child(index));
	}
}

int ArrayBST ::get_left_child(int index)
{
	if (array[2 * index] != 0 && 2 * index < 20)
	{
		return 2 * index;
	}
	else
		return -1;
}

int ArrayBST ::get_right_child(int index)
{
	if (array[2 * index + 1] != 0 && 2 * index + 1 < 20)
	{
		return 2 * index + 1;
	}
	else
		return -1;
}

void ArrayBST::deleteData(int data)
{
	int left_subtree, right_subtree;
	bool value_found = false;
	for (int i = 1; i < 20; i++)
	{
		if (data == this->array[i])
		{
			left_subtree = get_left_child(i);
			right_subtree = get_right_child(i);
			if (left_subtree != -1)
			{
				right_subtree = get_right_child(left_subtree);
				while (right_subtree != -1)
				{
					right_subtree = get_right_child(right_subtree);
				}
				cout << this->array[i] << " is to be deleted now." << endl;
				this->array[i] = this->array[right_subtree];
				this->array[right_subtree] = 0;
			}
			else if (right_subtree != -1)
			{
				left_subtree = get_left_child(right_subtree);
				while (left_subtree != -1)
				{
					left_subtree = get_left_child(left_subtree);
				}
				cout << this->array[i] << " is to be deleted now." << endl;
				this->array[i] = this->array[left_subtree];
				this->array[left_subtree] = 0;
			}
			else
			{
				cout << this->array[i] << " is to be deleted now." << endl;
				this->array[i] = 0;
			}
			value_found = true;
		}
	}
	if (!value_found)
	{
		cout << "The value " << data << " you entered for deletion is not in the tree." << endl;
	}
	this->array[0]--;
}

bool ArrayBST::search(int data)
{
	int current_index = 1;
	while (current_index <= 20)
	{
		if (array[current_index] == data)
		{
			return true;
			break;
		}
		else if (array[current_index] > data)
		{
			current_index = 2 * current_index;
		}
		else if (array[current_index] < data)
		{
			current_index = 2 * current_index + 1;
		}
	}
	return false;
}

int ArrayBST::max()
{
	int temp;
	for (int i = 0; i < 20;)
	{
		if (this->array[2 * i + 1] && (2 * i + 1 < 20))
		{
			temp = this->array[2 * i + 1];
			i = i * 2 + 1;
		}
		else
			break;
	}
	return temp;
}

int ArrayBST::min()
{
	int temp;
	for (int i = 1; i < 20;)
	{
		if (this->array[2 * i] != 0)
		{
			temp = this->array[2 * i];
			i = i * 2;
		}
		else
			break;
	}
	return temp;
}

int main()
{

	ArrayBST a;
	a.addData(10);
	a.addData(13);
	a.addData(5);
	a.addData(3);
	a.addData(6);
	a.addData(11);
	a.addData(23);
	a.addData(2);
	a.addData(4);
	if (a.search(3))
	{
		cout << "searched data 3 is in the BST." << endl;
	}
	a.preorderTraversal();
	a.inorderTraversal();

	cout << "The maximum value in the tree is " << a.max() << endl;
	cout << "The minimum value in the tree is " << a.min() << endl;
	a.deleteData(11);
	a.preorderTraversal();
	a.deleteData(23);
	a.inorderTraversal();
	cout << endl;
	return 0;
}
