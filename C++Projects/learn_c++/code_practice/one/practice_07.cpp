// practice_07.cpp -- practice call function to display hour and minute

#include <iostream>

using namespace std;

void display(int, int);

int main()
{
    cout << "Enter the number of hours: ";
    int hour;
    cin >> hour;
    cout << "Enter the number of minutes: ";
    int minute;
    cin >> minute;
    display(hour, minute);
    return 0;
}
void display(int a, int b)
{
    cout << "Time: " << a << ":" << b << endl;
}