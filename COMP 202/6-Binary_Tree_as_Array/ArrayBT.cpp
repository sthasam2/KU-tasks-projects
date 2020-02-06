#include <iostream>
#include "ArrayBT.h"

using namespace std;

/*---------------------------------Public----------------------------------------*/
ArrayBT::ArrayBT()
{
	std::cout << "Binary Tree (Integers)" << endl;
}

bool ArrayBT::isEmpty()
{
	return (this->tree[1] == NULL);
}

void ArrayBT::add(int data)
{
	int addIndexId = 1;
	node *newNode = new node();
	newNode->data = data;
	newNode->key = addIndexId;

	if (isEmpty())
	{
		//Add data to first element of array
		addToIndex(addIndexId, newNode);
	}
	else
	{
		node *root = tree[1];
		insert(root, newNode, root->key);
	}
}

int ArrayBT::size()
{
	if (isEmpty())
	{
		return 0;
	}

	node *root = tree[1];
	return psize(root);
}

void ArrayBT::traverse(traversalTypes type)
{
	std::cout << "-----------" << endl
			  << " TRAVERSAL " << endl
			  << "-----------" << endl;

	if (isEmpty())
	{
		std::cout << "Tree is empty" << endl;
	}
	node *root = tree[1];
	if (type == LVR)
	{
		traverseLVR(root);
	}
	else if (type == VLR)
	{
		traverseVLR(root);
	}
	else if (type == LRV)
	{
		traverseLRV(root);
	}
	std::cout << endl
			  << "---------------------------------------" << endl;
}

//input data, output key
int ArrayBT::search(int data)
{
	if (isEmpty())
		return 0;
	node *root = tree[1];
	return searchRootInNode(root, data);
}

void ArrayBT::remove(int data)
{
	if (isEmpty())
	{
		std::cout << "Tree is empty" << endl;
	}

	int keyToBeRemoved = search(data);

	if (keyToBeRemoved == 0)
	{
		std::cout << "Data not found";
	}

	else
	{
		//recursively shift the data and remove the node :D
		node *root = tree[keyToBeRemoved];
		shiftChildToRoot(root);
	}
}

bool ArrayBT::dataExists(int query)
{
	if (isEmpty())
	{
		return false;
	}

	node *root = tree[1];
	return searchInNode(root, query);
}

/*-----------------------------Private--------------------------------------------*/
void ArrayBT::addToIndex(int index, node *newNode)
{
	tree[index] = newNode;
}

void ArrayBT::insert(node *root, node *newNode, int key)
{
	if (root == NULL)
	{
		newNode->key = key;
		tree[key] = newNode;
	}
	else if (root->data > newNode->data)
	{
		//add to left
		int leftKey = getLeftChildIndex(root->key);
		node *left = tree[leftKey];
		insert(left, newNode, leftKey);
	}
	else
	{
		//add to right
		int rightKey = getRightChildIndex(root->key);
		node *right = tree[rightKey];
		insert(right, newNode, rightKey);
	}
}

/* Traversal */
//LVR
void ArrayBT::traverseLVR(node *root)
{
	if (root != NULL)
	{

		node *left = tree[getLeftChildIndex(root->key)];
		traverseLVR(left);

		std::cout << root->data << " ";

		node *right = tree[getRightChildIndex(root->key)];
		traverseLVR(right);
	}
}

//VLR
void ArrayBT::traverseVLR(node *root)
{
	if (root != NULL)
	{
		std::cout << root->data << " ";

		node *left = tree[getLeftChildIndex(root->key)];
		traverseVLR(left);

		node *right = tree[getRightChildIndex(root->key)];
		traverseVLR(right);
	}
}

//LRV
void ArrayBT::traverseLRV(node *root)
{
	if (root != NULL)
	{
		node *left = tree[getLeftChildIndex(root->key)];
		traverseLRV(left);

		node *right = tree[getRightChildIndex(root->key)];
		traverseLRV(right);

		std::cout << root->data << " ";
	}
}
/* / Traversal */

int ArrayBT::psize(node *root)
{
	if (root == NULL)
	{
		return 0;
	}

	node *left = tree[getLeftChildIndex(root->key)];
	node *right = tree[getRightChildIndex(root->key)];

	return psize(left) + psize(right) + 1;
}

int ArrayBT::getRightChildIndex(int key)
{
	return 2 * key + 1;
}

int ArrayBT::getLeftChildIndex(int key)
{
	return 2 * key;
}

//Search
//input root & data, output bool
bool ArrayBT::searchInNode(node *root, int data)
{
	if (root == NULL)
	{
		return false;
	}
	if (root->data == data)
	{
		return true;
	}
	if (root->data > data)
	{
		node *left = tree[getLeftChildIndex(root->key)];
		return searchInNode(left, data);
	}
	else
	{
		node *right = tree[getRightChildIndex(root->key)];
		return searchInNode(right, data);
	}
}

//input root & data from search, output key
int ArrayBT::searchRootInNode(node *root, int data)
{
	if (root == NULL)
	{
		return 0;
	}
	if (root->data == data)
	{
		return root->key;
	}
	if (root->data > data)
	{
		node *left = tree[getLeftChildIndex(root->key)];
		return searchRootInNode(left, data);
	}
	else
	{
		node *right = tree[getRightChildIndex(root->key)];
		return searchRootInNode(right, data);
	}
}

//Removal
void ArrayBT::shiftChildToRoot(node *root)
{
	node *left = tree[getLeftChildIndex(root->key)];
	node *right = tree[getRightChildIndex(root->key)];

	if (left == NULL && right == NULL)
	{
		//It's a leaf so just delete, deletion takes place here
		root = NULL;
	}

	else if (left != NULL && right != NULL)
	{
		//both left and right nodes present

		// 1: get the largest of the two nodes
		node *largest = (left->data > right->data) ? left : right; //(condition)? true: false;
		root->data = largest->data;

		// 2: the largest child node to the top and do recursion
		shiftChildToRoot(largest);
	}

	else
	{
		//either of the node is present
		if (left == NULL)
		{
			//right
			root->data = right->data;
			shiftChildToRoot(right);
		}
		else
		{
			//left
			root->data = left->data;
			shiftChildToRoot(left);
		}
	}
}