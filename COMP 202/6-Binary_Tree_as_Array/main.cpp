#include <iostream>
#include "ArrayBT.h"
#include "ArrayBT.cpp"

using namespace std;

int main()
{
	ArrayBT bt;
	int option, data;
	char proceed;
	std::cout << "................................................................................." << endl
			  << "|  1. Confirm Existence     2. Traverse     3. Add     4. Remove     5. Search  |" << endl
			  << "................................................................................." << endl;

	do
	{
		std::cout << endl
				  << "_________________________________________________________" << endl
				  << "     Please choose the option from the top menu :: ";
		std::cin >> option;
		switch (option)
		{

		case 1:
			int query;
			std::cout << "\nEnter data to check existence of : ";
			std::cin >> query;
			if (bt.dataExists(query))
				std::cout << "\n!!! " << query << " exists !!!";
			else
				std::cout << "\n!!! " << query << " does not exist !!!";
			break;

		case 2:
			std::cout << "\nChoose Traversal Type:\n1. LVR     2. LRV     3.VLR\n";
			std::cin >> option;
			if (option == 1)
				bt.traverse(LVR);
			else if (option == 2)
				bt.traverse(LRV);
			else if (option == 3)
				bt.traverse(VLR);
			else
				cout << "\nWrong Option!\n";
			break;

		case 3:
			std::cout << "\nEnter data to be added : ";
			std::cin >> data;
			bt.add(data);
			std::cout << "\n+++ " << data << " added succesfully! +++";
			break;

		case 4:
			std::cout << "\nEnter data to be removed : ";
			std::cin >> data;
			bt.remove(data);
			std::cout << "\n--- " << data << " removed succesfully! ---";
			break;

		case 5:
		{
			std::cout << "\nEnter data to be searched : ";
			std::cin >> data;
			int queryKey = 0;
			queryKey = bt.search(data);
			if (queryKey == 0)
				std::cout << "\n*** " << data << " not found! ***";
			else
				std::cout << "\n*** " << data << " succesfully found in key" << queryKey << "! ***";
			break;
		}

		default:
			std::cout << "\nWrong Option";
			break;
		}

		std::cout << "\n\nDo you want to continue? (y/n) : ";
		std::cin >> proceed;
	} while (proceed == 'y' | proceed == 'Y');
	return 0;
}