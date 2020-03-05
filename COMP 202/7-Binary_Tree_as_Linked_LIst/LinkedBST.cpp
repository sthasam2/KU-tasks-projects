#include <iostream>
#include "LinkedBST.h"

//PUBLIC
LinkedBST::LinkedBST()
{
    root = NULL;
}

void LinkedBST::addData(int userData)
{
    addNode(root, userData);
}

void LinkedBST::addNode(Node *&root, int userData)
{
    Node *newNode = new Node();
    newNode->data = userData;
    //condition when root is null ie no root exists
    if (root == NULL)
    {
        root = new Node();
        this->root = newNode;
    }
    //condition when root is not null ie a root exists
    else
    {
        insert(root, newNode);
    }
}

void LinkedBST::deleteData(int userData)
{
    deleteNode(root, userData);
}

Node *LinkedBST::deleteNode(Node *&tempRoot, int userData)
{
    //condition when root is null ie no root exists
    if (tempRoot == NULL)
    {
        std::cout << "Error: root empty";
        return tempRoot;
    }
    //condition when root is not null ie a root exists
    //recursive calls for getting to the node to be deleted
    //when userdata is less than root data
    if (tempRoot->data > userData)
    {
        tempRoot->left = deleteNode(tempRoot->left, userData);
        return tempRoot;
    }
    //when userdata is greater than root data
    else if (tempRoot->data < userData)
    {
        tempRoot->right = deleteNode(tempRoot->right, userData);
        return tempRoot;
    }
    //when the node to be deleted is found ie user data = root data
    // If one of the children is empty
    if (tempRoot->left == NULL)
    {
        Node *temp = tempRoot->right;
        delete tempRoot;
        return temp;
    }
    else if (tempRoot->right == NULL)
    {
        Node *temp = tempRoot->left;
        delete tempRoot;
        return temp;
    }
    // If both children exist
    else
    {
        Node *predecessor = tempRoot->right;
        // Find successor
        Node *successor = tempRoot->right;
        
        while (successor->left != NULL)
        {
            predecessor = successor;
            successor = successor->left;
        }
        // Delete successor. Since successor is always left child of its parent, we can safely make successor's right child as left of its parent.
        predecessor->left = successor->right;
        // Copy Successor Data to root
        tempRoot->data = successor->data;
        // Delete Successor and return root
        delete successor;
        return tempRoot;
    }
}

bool LinkedBST::search(int userData)
{
    return find(root, userData);
}

//Traversal

void LinkedBST::preorderTraversal()
{
    traverse(root, PreTV);
}

void LinkedBST::postorderTraversal()
{
    traverse(root, PostTV);
}

void LinkedBST::inorderTraversal()
{
    traverse(root, InTV);
}

//MAX MIN

int LinkedBST::max()
{
    int max;
    //when tree empty
    if (root == NULL)
    {
        std::cout << "ERROR: NULL TREE!\n";
    }
    //when tree not empty
    else
    {
        Node *temp = new Node();
        //initializing search node: 'temp' from root
        temp = root;
        //looping until end of BST
        while (temp != NULL)
        {
            max = temp->data;
            temp = temp->right;
        }
    }
    return max;
}

int LinkedBST::min()
{
    int min;
    //when tree empty
    if (root == NULL)
    {
        std::cout << "ERROR: NULL TREE!\n";
    }
    //when tree not empty
    else
    {
        Node *temp = new Node();
        //initializing search node: 'temp' from root
        temp = root;
        //looping until end of BST
        while (temp != NULL)
        {
            min = temp->data;
            temp = temp->left;
        }
    }
    return min;
}

// ------------------------------------------------------------------------------------------

//PRIVATE

void LinkedBST::insert(Node *&subtree, Node *newNode)
{
    //condition when parent->data is greater than newNode->data ie newNode smaller
    if (subtree->data > newNode->data)
    {
        //adding newNode to left node when left is populated recursively
        if (subtree->left != NULL)
        {
            insert(subtree->left, newNode);
            //adding directly to left since left is empty
        }
        //if space to add is null ie when adding point reached
        else
        {
            subtree->left = newNode;
        }
    }
    //condition when parent->data is smaller than newNode->data ie newNode is greater
    else
    {
        //adding newNode to right node when right is populated recursively
        if (subtree->right != NULL)
        {
            insert(subtree->right, newNode);
        }
        //adding directly to right since right is empty
        else
        {
            subtree->right = newNode;
        }
    }
}

bool LinkedBST::find(Node *&subtree, int targetKey)
{
    //when tree empty
    if (root == NULL)
    {
        std::cout << "ERROR: NULL TREE!\n";
    }
    //when tree not empty
    else
    {
        Node *temp = new Node();
        //initializing search node: 'temp' from root
        temp = root;
        //looping until end of BST
        while (temp != NULL)
        {
            //condition when targetKey > current node data
            if (targetKey > temp->data)
            {
                temp = temp->right;
            }
            //condition when targetKey < current node data
            else if (targetKey < temp->data)
            {
                temp = temp->left;
            }
            //condition when targetKey = current node data
            else if (targetKey == temp->data)
            {
                return true;
            }
        }
    }
    //when targetKey does not exist
    return false;
}

void LinkedBST::traverse(Node *root, Traversal Type)
{
    //check if tree empty the return
    if (root == NULL)
    {
        return;
    }

    //when traverse type = Preorder
    if (Type == PreTV)
    {
        std::cout << root->data << " ";
        traverse(root->left, PreTV);
        traverse(root->right, PreTV);
    }
    //when traverse type = Postorder
    else if (Type == PostTV)
    {
        traverse(root->left, PostTV);
        traverse(root->right, PostTV);
        std::cout << root->data << " ";
    }
    //when traverse type = Inorder
    else if (Type == InTV)
    {
        traverse(root->left, InTV);
        std::cout << root->data << " ";
        traverse(root->right, InTV);
    }
}
