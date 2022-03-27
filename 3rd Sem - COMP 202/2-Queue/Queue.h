#ifndef Queue_h
#define Queue_h

#define MAX_SIZE 10

class queue
{
public:
    queue(int size = MAX_SIZE); //constructor
    ~queue();                   //destructor

    void dequeue();
    void enqueue(char x);
    char peek();
    bool isEmpty();
    bool isFull();
    int size();
    int sizeQueue();
    int getCurrentPosition();
    void displayQueue();

private:
    int front;      //points to the front of queue
    int rear;       //point to the back of queue
    int count;      //current size of queue
    int capacity;   //max capacity of queue
    char *elements; //array to store queue elements
};
#endif // !Queue_h
