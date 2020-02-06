#ifndef ArrayBT_h
#define ArrayBT_h

#define MAX_SIZE 500

class node
{
public:
	node(){};

	int key;
	int data;
};

// user defined data type
enum traversalTypes
{
	LVR,
	LRV,
	VLR,
};

class ArrayBT
{
private:
	node *tree[MAX_SIZE]; //initialize a binary tree

	void addToIndex(int index, node *node); //Add the node to the given index of our array

	//travers the given node
	void traverseLVR(node *root);
	void traverseVLR(node *root);
	void traverseLRV(node *root);

	void insert(node *root, node *node, int key); //Add to appropriate child of the given root node

	int psize(node *root); //Returns node cardinality form the given root node

	int getRightChildIndex(int key); //returns the index of its right child
	int getLeftChildIndex(int key);  //returns the index of its left child

	//search in each node
	bool searchInNode(node *root, int data);
	int searchRootInNode(node *root, int data);

	void shiftChildToRoot(node *root); //for removing the node shift the data from lower node to highter

public:
	ArrayBT();

	bool isEmpty();						//check if tree is empty
	int size();							//Return the total nodes in the tree
	void add(int data);					//Add data to the binary tree
	void remove(int data);				//Remove the node with given data.
	int search(int data);				//Returns the node's key with given data. else couts exception.
	bool dataExists(int query);			//Return true if there is an node with data in the table. else return false
	void traverse(traversalTypes type); //Prints all node's data in the tree
};

#endif