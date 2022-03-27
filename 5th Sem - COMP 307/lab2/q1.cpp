#include <pthread.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0,
    out = 0,
    count = 0;

int turn;
int writer = 0,
    reader = 1;
bool interested[2];

int randomGenerator()
{
    return rand() / 1000;
}

void *writerExecuter(void *arg)
{
    int MAX = *(int *)arg;
    int itemToWrite;

    for (int i = 0; i < MAX; i++)
    {

        interested[writer] = true;
        turn = reader;
        // Buffer full, wait
        while (((in + 1) % BUFFER_SIZE) == out)
            ;

        itemToWrite = randomGenerator();
        printf("Writing %d into the buffer\n", itemToWrite);
        buffer[in] = itemToWrite;    // write into buffer
        in = (in + 1) % BUFFER_SIZE; // increase in count
        // wait if turn is reader and they're interested
        while (interested[reader] && turn == reader)
            ;
        // critical section start
        count += 1;
        // critical section end
        interested[writer] = false;
    }
    pthread_exit(NULL); // terminate thread
}

void *readerExecuter(void *arg)
{
    int MAX = *(int *)arg;
    int itemToRead;

    for (int i = 0; i < MAX; i++)
    {

        interested[reader] = true;
        turn = writer;
        // buffer is empty, wait
        while (in == out)
            ;
        ;
        itemToRead = buffer[out];
        printf("Reading %d from buffer and removing it...\n", itemToRead);
        out = (out + 1) % BUFFER_SIZE;
        // wait if turn is writer and writer interested
        while (interested[writer] && turn == writer)
            ;
        ;
        // critical start
        count -= 1;
        // critical end
        interested[reader] = false;
    }
    pthread_exit(NULL);
}

int main(void)
{
    int writerCount = 10,
        readerCount = 8;

    pthread_t pid_writer, pid_reader;

    pthread_create(&pid_writer, NULL, writerExecuter, &writerCount);
    pthread_create(&pid_reader, NULL, readerExecuter, &readerCount);

    pthread_join(pid_writer, NULL);
    pthread_join(pid_reader, NULL);

    printf("\nDifference (writes - reads) count = %d\n", count);
    return 0;
}