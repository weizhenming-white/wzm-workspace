// practice_06.cpp -- practice call function

#include <iostream>

double calculation(double);

int main()
{
    using namespace std;

    double m;
    cout << "Enter the number of light years: ";
    cin >> m;
    double num = calculation(m);
    cout << m << " lights years = " << num << " astronomical units." << endl;
    return 0;
}

double calculation(double n)
{
    return n *63240;
}