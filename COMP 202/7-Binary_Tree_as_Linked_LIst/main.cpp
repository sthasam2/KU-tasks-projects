#include "LinkedBST.cpp"
// #include "ArrayBST.h"

int main()
{
    std::cout << "\tBinary Search Tree as Linked List\n"
              << "-------------------------------------------------\n";
    LinkedBST lBST; //creating Linked BST instance
    //add
    lBST.add(55);
    lBST.add(122);
    lBST.add(136);
    lBST.add(21);
    lBST.add(11);
    lBST.add(33);
    lBST.add(47);

    //traverse
    std::cout << "\nPreorderTraversal: ";
    lBST.preorderTraversal();
    std::cout << "\nPostorderTraversal: ";
    lBST.postorderTraversal();
    std::cout << "\nInorderTraversal: ";
    lBST.inorderTraversal();

    //search
    std::cout << "\n";
    //1st data
    int query = 11;
    bool found = lBST.search(query);
    if (found)
        std::cout << "\nSearched data (" << query << ") FOUND in tree.";
    else
        std::cout << "\nSearched Data (" << query << ") NOT found in tree.";
    //2nd data
    int query2 = 14;
    bool found2 = lBST.search(query2);
    if (found2)
        std::cout << "\nSearched data (" << query2 << ") FOUND in tree.";
    else
        std::cout << "\nData (" << query2 << ") NOT found in tree.";

    //MIN/MAX
    std::cout << "\n";
    std::cout << "\nMinimum sized data in tree:" << lBST.min(); //min
    std::cout << "\nMaximum sized data in tree:" << lBST.max(); //max

    return 0;
}