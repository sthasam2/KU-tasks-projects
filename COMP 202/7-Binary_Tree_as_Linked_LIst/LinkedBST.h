#include "BST.h"

class Node
{
public:
	//node data
	int data;

	//subtree/child pointers
	Node *left;
	Node *right;

	//constructor
	Node()
	{
		data = 0;
		left = NULL;
		right = NULL;
	}
};

//custom datatype for traversal
enum Traversal
{
	PreTV,
	PostTV,
	InTV
};

class LinkedBST : public BST
{
//private functions
private:
	//insert node to specific subtree
	void insert(Node *&subtree, Node *newNode);
	//searches for targetKey in the tree
	bool find(Node *&subtree, int targetKey);
	//lists data in specific order
	void traverse(Node *root, Traversal Type);

//public function
public:
	//creates root node for each linked List BST implementation
	Node *root;
	//constructor
	LinkedBST();

	//adds data from the user into the tree
	void add(int dataUser);
	void add(Node *&root, int dataUser);
	
	//traverses the data in givern order
	void preorderTraversal();
	void postorderTraversal();
	void inorderTraversal();

	//searches for userinput data
	bool search(int dataUser);

	//returns min/max data in the tree
	int min();
	int max();
};
