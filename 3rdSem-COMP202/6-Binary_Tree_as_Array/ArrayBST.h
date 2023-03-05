
#include "BST.h"
#include <iostream>

class ArrayBST : public BST
{
public:
	ArrayBST();
	~ArrayBST();
	void addData(int data);
	void deleteData(int data);

	void preordertraversal(int index);
	void preorderTraversal();

	bool search(int data);

	void inorderTraversal();
	void inorder_traversal(int index);

	int get_left_child(int index);
	int get_right_child(int index);

	int min();
	int max();

private:
	int array[20];
};
