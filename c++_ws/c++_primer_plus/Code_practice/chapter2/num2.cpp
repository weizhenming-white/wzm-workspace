// num2.cpp -- 要求用户输入一个以long为单位的距离，然后将它转换为码（一long等于220码）

#include <iostream>

int main()
{
    using namespace std;
    cout << "Enter the distance in long: ";
    int distance;
    cin >> distance;
    int yard = distance * 220;
    cout << distance << " long = ";
    cout << yard << " yard." << endl;
    return 0;
}