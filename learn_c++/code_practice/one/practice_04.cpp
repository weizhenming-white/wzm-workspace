// practice_04.cpp -- Enter your age

#include <iostream>

using namespace std;

int main()
{
    int age;
    cout << "Enter your age: ";
    cin >> age;
    int month_all = age * 12;
    cout << "You've been through " << month_all << " months" << endl;
    return 0;
}