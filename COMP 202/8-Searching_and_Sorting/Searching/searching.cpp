#include "../Sorting/quickSort.h" // linking QuickSort for sorting the list

#include <iostream>
using namespace std;

// Binary Search
int BinarySearch(int list[], int target, int size)
{
	int min = 0;
	int max = size - 1;
	int mid;
	while (max >= min)
	{
		mid = (min + max) / 2;
		if (list[mid] == target)
		{
			return mid;
		}
		else if (list[mid] < target)
		{
			min = mid + 1;
		}
		else if (list[mid] > target)
		{
			max = mid - 1;
		}
	}
	return -1;
}

// search result display
void searchResult(int index, int searchData)
{
	if (index != -1)
	{
		std::cout << "\n|\tSearched data '" << searchData << "' found in index: " << index << "\t|";
	}
	else
	{
		std::cout << "\n|\tSearched data '" << searchData << "' not found\t|";
	}
}

//driver module
int main()
{
	std::cout << "\n.......................................................\n"
			  << "\t\tSearching Implementation"
			  << "\n.......................................................\n";

	int list[] = {1, 2, 3, 5, 4, 7, 10, 15, 55, 200, 2, 33, 690, 20, 30, 32, 45, 87, 125, 265, 320, 420};
	int index = -1, size;
	size = sizeof(list) / sizeof(list[0]);
	quickSort(list, 0, size - 1);

	int searchData = 690;
	index = BinarySearch(list, searchData, size);

	searchResult(index, searchData);
}