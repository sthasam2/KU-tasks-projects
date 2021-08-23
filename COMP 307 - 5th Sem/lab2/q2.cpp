#include <iostream>
#include <pthread.h>
#include <time.h>
#include <unistd.h>

float turnAroundTime = 0;
int order = 0;

struct process
{
    char name[50];
    int order;
    float arrivalTime;
    float burstTime;
    float waitingTime;
    float turnAroundTime;
    bool finish;
};

// calculate average waiting time
float avgWaitTime(process *p1, process *p2, process *p3, process *p4, process *p5)
{
    return (p1->waitingTime + p2->waitingTime + p3->waitingTime + p4->waitingTime + p5->waitingTime) / 5;
}

//calculate average turnaround time
float avgToTime(process *p1, process *p2, process *p3, process *p4, process *p5)
{
    return (p1->turnAroundTime + p2->turnAroundTime + p3->turnAroundTime + p4->turnAroundTime + p5->turnAroundTime) / 5;
}

//print process data
void printData(process *P)
{
    std::cout << P->order << "\t" << P->name << "\t" << P->arrivalTime << "\t" << P->burstTime << "\t" << P->waitingTime << "\t" << P->turnAroundTime << std::endl;
}

// print Table of processes
void printTable(process p1, process p2, process p3, process p4, process p5)
{

    std::cout << "Order\tProcess\tArrival\tBurst\tWaiting\tTurnaround" << std::endl
              << "--------------------------------------------------------" << std::endl;

    process p[5] = {p1, p2, p3, p4, p5};

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (p[j].order == i + 1)
                printData(&p[j]);
        }
    }

    std::cout << std::endl
              << "Average waiting time = " << avgWaitTime(&p1, &p2, &p3, &p4, &p5);
    std::cout << std::endl
              << "Average turnaround time = " << avgToTime(&p1, &p2, &p3, &p4, &p5);
    std::cout << "\n";
}

void *calculateTimes(void *arg)
{
    order += 1;
    process *P = (process *)arg;
    usleep(P->arrivalTime);

    float prevToT = turnAroundTime;

    if (P->arrivalTime > prevToT)
    {
        P->waitingTime = 0;
        turnAroundTime = prevToT + (P->arrivalTime - prevToT) + P->burstTime;
        P->turnAroundTime = turnAroundTime;
        P->order = order;
    }
    else
    {
        P->waitingTime = prevToT - P->arrivalTime;
        turnAroundTime = prevToT + P->burstTime;
        P->turnAroundTime = turnAroundTime;
        P->order = order;
    }

    pthread_exit(NULL);
}

// First come first serve
void firstComeFirstServe(process process1, process process2, process process3, process process4, process process5)
{
    std::cout << "\n----------------------------------------\n\tFIRST COME FIRST SERVE\n----------------------------------------\n\n";
    pthread_t p1, p2, p3, p4, p5;

    pthread_create(&p1, NULL, calculateTimes, &process1);
    pthread_create(&p2, NULL, calculateTimes, &process2);
    pthread_create(&p3, NULL, calculateTimes, &process3);
    pthread_create(&p4, NULL, calculateTimes, &process4);
    pthread_create(&p5, NULL, calculateTimes, &process5);

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);
    pthread_join(p3, NULL);
    pthread_join(p4, NULL);
    pthread_join(p5, NULL);

    printTable(process1, process2, process3, process4, process5);
    turnAroundTime = 0, order = 0;
}

void shortestJobFirst(process process1, process process2, process process3, process process4, process process5)
{
    std::cout << "\n----------------------------------------\n\tSHORTEST JOB FIRST\n----------------------------------------\n\n";

    pthread_t sjpt[5];

    // sorting by burst time using bubble sort

    process sjp[5] = {process1, process2, process3, process4, process5};
    process temp;
    int n = 5;

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (sjp[j].burstTime > sjp[j + 1].burstTime)
            {
                temp = sjp[j];
                sjp[j] = sjp[j + 1];
                sjp[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < 5; i++)
    {
        pthread_create(&sjpt[i], NULL, calculateTimes, &sjp[i]);
        usleep(0.3);
    }

    for (int i = 0; i < 5; i++)
    {
        pthread_join(sjpt[i], NULL);
    }

    printTable(sjp[0], sjp[1], sjp[2], sjp[3], sjp[4]);
    turnAroundTime = 0, order = 0;
}

void priorityScheduling(process process1, process process2, process process3, process process4, process process5)
{
    std::cout << "\n----------------------------------------\n\tPRIORITY SCHEDULING\n----------------------------------------\n\n";

    pthread_t pt[5];

    // sorting by burst time using bubble sort

    process queue[5] = {process1, process2, process3, process4, process5};

    process temp;
    int n = 5;

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (queue[j].order > queue[j + 1].order)
            {
                temp = queue[j];
                queue[j] = queue[j + 1];
                queue[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < 5; i++)
    {
        pthread_create(&pt[i], NULL, calculateTimes, &queue[i]);
        usleep(0.3);
    }

    for (int i = 0; i < 5; i++)
    {
        pthread_join(pt[i], NULL);
    }

    printTable(queue[0], queue[1], queue[2], queue[3], queue[4]);
    turnAroundTime = 0, order = 0;
}

int main()
{
    process process1 = {"P1", 5, 0.0, 6.5, 0, 0, false};
    process process2 = {"P2", 2, 0.3, 0.5, 0, 0, false};
    process process3 = {"P3", 1, 2.2, 16.5, 0, 0, false};
    process process4 = {"P4", 4, 1.5, 1, 0, 0, false};
    process process5 = {"P5", 3, 0.0, 3, 0, 0, false};

    firstComeFirstServe(process1, process2, process3, process4, process5);
    shortestJobFirst(process1, process2, process3, process4, process5);
    priorityScheduling(process1, process2, process3, process4, process5);
}