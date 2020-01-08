// practice_05.cpp -- practice call function

#include <iostream>

double calculation(double);

int main()
{
    using namespace std;

    double num;
    cout << "Please enter a Celsius value: " ;
    cin >> num;
    double msg = calculation(num);
    cout << num << " degrees Celsius is " << msg << " degrees Fahrenheit." << endl;
    return 0;
}
double calculation(double n)
{
    using namespace std;

    return n * 1.8 + 32;
}