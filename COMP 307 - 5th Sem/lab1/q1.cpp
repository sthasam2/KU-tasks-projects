#include <iostream>
#include <unistd.h>

using namespace std;

int factorial(int num)
{
    int fact = 1;

    if (num == 0)
    {
        return 0;
    }
    else
    {
        for (int i = 1; i <= num; i++)
        {
            fact *= i;
        }
    }
    return fact;
}

int sumOfNaturalNumbers(int num)
{
    int sum = 0;

    if (num == 0)
    {
        return 0;
    }
    else
    {
        for (int i = 1; i <= num; i++)
        {
            sum += i;
        }
    }
    return sum;
}

int main()
{
    cout << "#########################" << endl
         << "\tOS LAB 1" << endl
         << "#########################" << endl;

    cout << "Before fork, Process id = " << getpid() << endl
         << endl;

    pid_t pid;
    pid = fork();

    if (pid < 0)
    {
        cout << "fork() failed!" << endl;
    }
    else if (pid == 0)
    {
        cout << "Child process. process id= " << getpid() << endl;
        int fact = factorial(5);
        cout << "Factorial of 5 = " << fact << endl;
        cout << "END Child Process\n\n";
    }
    else
    {
        cout << "Parent Process. process id= " << getpid() << endl;
    }

    cout << "END Parent Process\n\n";

    return 0;
}