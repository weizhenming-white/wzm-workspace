// practice_03.cpp -- input a integers and count
#include <iostream>
int main()
{
    using namespace std;
    int count = 0;
    int tmp;

    while (true)
    {
        cout << "Please input an integer: ";
        cin >> tmp;
        cout << endl;
        if (tmp == 0)
        {
            cout << "Exit!!!" << endl;
            break;
        }
        count = count + tmp;
        cout << "Up to now, Cumulative sum of all inputs is : " << count << endl;
    }
    return 0;
}