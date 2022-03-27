// Program to convert prefix expressions to postfix expressions

#include <iostream>
#include <string>

#include "pretopost.h" // includes the header file.

using namespace std;

//definitions of constructors and destructors

stack::stack()
{
    top = -1;
}

stack::~stack()
{
}

// definition of isEmpty function
bool stack::isEmpty()
{
    if (top < 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

// definition of isFull function
bool stack::isFull()
{
    if (top >= (MAX_STACK_SIZE - 1))
    {
        return true;
    }
    else
    {
        return false;
    }
}

// definition of push function
void stack::push(string ele)
{
    if (isFull())
    {
        cout << " cannot push " << ele << " \n Stack overflow";
    }
    else
    {
        top++;
        //cout << " \n pushed \n ";
        this->elements[top] = ele;
    }
}

// definition of pop function
string stack::pop()
{
    if (top < 0)
    {
        cout << " cannot pop \n stack underflow ";
    }
    else
    {
        //cout << "\n popped \n";
        return this->elements[top--];
    }
}

// definition of topc function
string stack::topc()
{
    if (isEmpty())
    {
        cout << "Stack underflow \n";
    }
    else
    {
        return this->elements[top];
    }
}

// funtion to check if the character is an operator or not
bool isOperator(char x)
{
    switch (x)
    {
    case '+':
    case '-':
    case '/':
    case '*':
        return true;
    }
    return false;
}

// the conversion happens here
string preToPost(string pre_exp)
{

    stack s;
    // getting the length of expression
    int length = pre_exp.size();
    // reading the expression from right to left
    for (int i = length - 1; i >= 0; i--)
    {
        // checking if the symbol is an operator
        if (isOperator(pre_exp[i]))
        {
            // pops two operands from the stack
            string op1 = s.topc();
            s.pop();
            string op2 = s.topc();
            s.pop();
            // concatenate the operands and the operator
            string temp = op1 + op2 + pre_exp[i];
            // Pushing the concatenated string back to stack
            s.push(temp);
        }
        // if the symbol is an operand
        else
        {
            if (pre_exp[i] == '(' || pre_exp[i] == ')')
            {
                // skipping brackets
                continue;
            }
            // pushing the operand to the stack
            s.push(string(1, pre_exp[i]));
        }
    }
    // returning the Postfix expression
    return s.topc();
}

// MAIN DRIVER CODE
int main()
{
    string pre_exp;
    cout << "\n ENTER ANY PREFIX EXPRESSION \n ";
    cin >> pre_exp;
    //Astring pre_exp = "*-A/BC-/AKL";
    cout << "Postfix : " << preToPost(pre_exp);
    return 0;
}
