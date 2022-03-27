#include <string>

using namespace std;
#define MAX_STACK_SIZE 100

class stack
{
public:
    stack();
    ~stack();

    void push(string ele);
    string pop();
    string topc();
    bool isEmpty();
    bool isFull();
    // char preToPost(char pre_exp);

    string elements[MAX_STACK_SIZE];
    char top;
};
