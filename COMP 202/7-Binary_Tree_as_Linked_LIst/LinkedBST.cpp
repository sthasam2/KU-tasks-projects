#include <iostream>
#include "LinkedBST.h"

//PUBLIC
LinkedBST::LinkedBST()
{
    root = NULL;
}

//add data
void LinkedBST::add(int dataUser)
{
    add(root, dataUser);
}

void LinkedBST::add(Node *&root, int dataUser)
{
    Node *newNode = new Node();
    newNode->data = dataUser;
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

//search
bool LinkedBST::search(int dataUser)
{
    return find(root, dataUser);
}

//Traversal
//pre
void LinkedBST::preorderTraversal()
{
    traverse(root, PreTV);
}

//post
void LinkedBST::postorderTraversal()
{
    traverse(root, PostTV);
}

//in
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
        return;

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
