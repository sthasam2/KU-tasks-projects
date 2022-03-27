#ifndef quickSort_H
#define quickSort_H

#include <iostream>

#define MAX_SIZE 20
static int length;
void getData(int list[]);
void quickSort(int list[], int low, int high);
void display(int sortedList[]);
int partition(int arr[], int low, int high);
void swap(int *a, int *b);

// definitions

//function to get data list from the user
void getData(int list[])
{
    std::cout << "Enter the size of data: ";
    std::cin >> length;
    std::cout << "Enter the data:\n";
    for (int i = 0; i < length; i++)
    {
        std::cout << "Data no. " << (i + 1) << ": ";
        std::cin >> list[i];
    }
}

// quick sort function
void quickSort(int list[], int low, int high)
{
    if (low < high)
    {
        int pivot = partition(list, low, high);
        quickSort(list, low, pivot - 1);
        quickSort(list, pivot + 1, high);
    }
}

// function to display the ordered list
void display(int sortedList[])
{
    std::cout << "The sorted list is:" << std::endl;
    for (int i = 0; i < length; i++)
    {
        if (i < (length - 1))
        {
            std::cout << sortedList[i] << ", ";
        }
        else
        {
            std::cout << sortedList[i] << ".";
        }
    }
}

// function to create partitions
int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++)
    {

        if (arr[j] < pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

// swap function
void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

#endif // SORTING_H
