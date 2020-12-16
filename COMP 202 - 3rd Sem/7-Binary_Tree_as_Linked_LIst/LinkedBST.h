#include "BST.h"

//creates a class called Node consisting of data and two child pointers
class Node
{
public:
	//node data
	int data;
	//subtree/child pointer: left
	Node *left;
	//subtree/child pointer: right
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
	//traverses data in specific order
	void traverse(Node *root, Traversal Type);

	//public function
public:
	//creates root node for each linked List BST object
	Node *root;
	//constructor
	LinkedBST();
	//takes data from the user to input into into the tree
	void addData(int userData);
	//adds node with user data into the tree
	void addNode(Node *&root, int userData);
	//takes data by user to delete from the tree
	void deleteData(int userData);
	//deletes the node from the tree and replaces with successor
	Node *deleteNode(Node *&tempRoot, int userData);
	//traverses the data in pre order
	void preorderTraversal();
	//traverses the data in post order
	void postorderTraversal();
	//traverses the data in in order
	void inorderTraversal();
	//searches for userinput data
	bool search(int userData);
	//returns min data in the tree
	int min();
	//returns max data in the tree
	int max();
};
