// practice_01.cpp -- test practice add
#include <iostream>
int main()
{
    using namespace std;
    int m, n;
    cout << "Please input first int: ";
    cin >> m;
    cout << endl << "Please input second int: ";
    cin >> n;
    cout << endl;

    int count = 0;
    if (m > n)
    {
        do
        {
            count = count + m;
            m--;
        } while (m >= n);
        cout << "Sum of two integers is: " << count << endl;    
    }
    else if (m == n)
    {
        count = m + n;
        cout << "Sum of two integers is: " << count << endl;    
    }
    else
    {
        do
        {
            count = count + m;
            m++;
        } while (m <= n);
        cout << "Sum of two integers is: " << count << endl;    
    }
    return 0;
}