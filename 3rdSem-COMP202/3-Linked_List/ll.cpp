#include <iostream>
#include <stddef.h>
#include "ll.h"

using namespace std;

ll::ll()
{
        HEAD = NULL;
        TAIL = NULL;
}

ll::~ll()
{
}

bool ll::isEmpty()
{
        return HEAD == NULL;
}

void ll::addToHead(int data)
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

void ll::addToTail(int data)
{
        node *newNode = new node();
        newNode->info = data;
        newNode->next = NULL;
        TAIL->next = newNode;
        TAIL = newNode;
}

void ll::add(int data, node *predecessor)
{
        node *newNode = new node();
        newNode->info = data;
        newNode->next = predecessor->next;
        predecessor->next = newNode;
}

void ll::removeFromHead()
{
        node *deleteNode = new node();
        deleteNode = HEAD;
        HEAD = deleteNode->next;
        delete deleteNode;
}

void ll::remove(int data)
{
        if (isEmpty())
        {
                std::cout << "List is Empty" << std::endl;
        }
        else
        {
                if (HEAD->info == data)
                {
                        removeFromHead();
                }
                if (HEAD == NULL)
                {
                        TAIL = NULL;
                }
                else
                {
                        node *temp = HEAD->next;
                        node *prev = HEAD;

                        while (temp != NULL)
                        {
                                if (temp->info == data)
                                {
                                        prev->next = temp->next;
                                        temp = NULL;
                                }
                                if (prev->next == NULL)
                                {
                                        TAIL = prev;
                                }
                                else
                                {
                                        prev = prev->next;
                                        temp = temp->next;
                                }
                        }
                }
        }
}

bool ll::retrieve(int data, node *&outputPtr)
{
        node *temp = HEAD;

        while (temp != NULL && temp->info != data)
        {
                temp = temp->next;
        }
        if (temp == NULL)
        {
                return false;
        }
        else
        {
                outputPtr = temp;
                return true;
        }
}

void ll::traverse()
{
        node *temp = HEAD;

        while (temp != NULL)
        {
                std::cout << temp->info << " ";
                temp = temp->next;
        }
}

bool ll::search(int data)
{
        node *temp = HEAD;

        while (temp != NULL)
        {
                if (temp->info == data)
                        return true;
                else
                        temp = temp->next;
        }

        return false;
}

int main()
{
        ll l;
        int option, data;
        char proceed;
        bool found;
        std::cout << ".........................................................." << endl
                  << "|  1. Add        2. Add to Head          3. Add to Tail  |" << endl
                  << "|  4. Remove     5. Remove from Head     6. Search       |" << endl
                  << "|  7. Retrieve   8. Traverse                             |" << endl
                  << ".........................................................." << endl;
        do
        {
                std::cout << endl
                          << "_________________________________________________________" << endl
                          << "Please choose the option from the top menu :: ";
                std::cin >> option;
                switch (option)
                {

                //Curly brackets {} used in cases to avoid compilation error in visual studio while initializing node
                case 1:
                {
                        int predecessor;
                        std::cout << endl
                                  << "Please enter the data : ";
                        std::cin >> data;
                        std::cout << "Please enter the data after which you want to add new data : ";
                        std::cin >> predecessor;
                        node *p = new node();
                        found = l.retrieve(predecessor, p);
                        if (found)
                        {
                                l.add(data, p);
                                std::cout << "***" << data << " successfully added succesive to " << predecessor << "***";
                        }
                        else
                        {
                                std::cout << "ERROR : Existing data not found in list";
                        }
                        break;
                }

                case 2:
                {
                        std::cout << endl
                                  << "Please enter the data to add to HEAD: ";
                        std::cin >> data;
                        l.addToHead(data);
                        std::cout << "***" << data << " successfully added HEAD***";
                        break;
                }

                case 3:
                {
                        std::cout << endl
                                  << "Please enter the data to add to TAIL: ";
                        std::cin >> data;
                        if (l.isEmpty())
                        { //if empty tail=nullptr and nullptr cannot store newnode
                                l.addToHead(data);
                        }
                        else
                        {
                                l.addToTail(data);
                        }
                        std::cout << "***" << data << " successfully added TAIL***";
                        break;
                }

                case 4:
                {
                        std::cout << endl
                                  << "Please enter the data to remove: ";
                        std::cin >> data;
                        found = l.search(data);
                        if (found)
                        {
                                l.remove(data);
                                std::cout << "***Successfully removed " << data << " from list***";
                        }
                        else
                        {
                                std::cout << "ERROR: Data not found";
                        }
                        break;
                }

                case 5:
                {
                        if (l.isEmpty())
                        {
                                std::cout << endl
                                          << "List is Empty";
                        }
                        else
                        {
                                l.removeFromHead();
                                std::cout << endl
                                          << "***Successfully removed data from HEAD***";
                        }
                        break;
                }

                case 6:
                {
                        std::cout << endl
                                  << "Enter the data to be searched: ";
                        std::cin >> data;
                        found = l.search(data);
                        if (found)
                        {
                                std::cout << data << " has been found in the list.";
                        }
                        else
                        {
                                std::cout << data << " was not found in the list.";
                        }
                        break;
                }

                case 7:
                {
                        std::cout << endl
                                  << "Enter the data to be retrieved: ";
                        std::cin >> data;
                        found = l.search(data);
                        if (found)
                        {
                                std::cout << data << " has been retrieved from the list.";
                        }
                        else
                        {
                                std::cout << data << " was not found in the list.";
                        }
                        break;
                }

                case 8:
                {
                        l.traverse();
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
