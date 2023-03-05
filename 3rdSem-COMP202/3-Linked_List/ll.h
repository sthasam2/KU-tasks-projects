#ifndef ll_h
#define ll_h

class node
{
public:
    node(){};
    int info;
    node *next;
};

class ll
{
public:
    //constructors
    ll();
    ~ll();

    //functons
    bool isEmpty();

    void addToHead(int data);
    void addToTail(int data);
    void add(int data, node *predecessor);

    void removeFromHead();
    void remove(int data);

    bool search(int data);
    void traverse();
    bool retrieve(int data, node *&outputPtr);

private:
    node *HEAD;
    node *TAIL;
};
#endif
