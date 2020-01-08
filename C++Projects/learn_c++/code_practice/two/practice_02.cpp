// practice_02.cpp -- one to one_hundred factorials
#include <iostream>
const int Arsize = 100;
int main()
{
    using namespace std;
    long double factorials[Arsize];
    factorials[1] = factorials[0] = 1;

    for (int i = 2; i < Arsize; i++)
    {
        factorials[i] = i * factorials[i - 1];
    }
    for (int i = 0; i < Arsize; i++)
    {
        cout << i << "! = " << factorials[i] << std::endl;
    }
    return 0;
}