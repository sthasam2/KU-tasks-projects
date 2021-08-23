#include <iostream>
#include <unistd.h>

using namespace std;

int main()
{
    pid_t pid;

    int i;

    for (i = 0; i < 4; i++)
    {
        cout << i << endl;
        pid = fork();
        sleep(2);
    }
    return 0;
}
