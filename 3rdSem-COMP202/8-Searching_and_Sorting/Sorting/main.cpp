#include "quickSort.h"

int main()
{
    int list[MAX_SIZE];

    std::cout << "DATA ENTRY:\n\n";
    getData(list);
    int low = 0, high = length - 1;

    quickSort(list, low, high);

    std::cout << "\nSORTED DATA LIST:\n\n";
    display(list);

    return 0;
}
