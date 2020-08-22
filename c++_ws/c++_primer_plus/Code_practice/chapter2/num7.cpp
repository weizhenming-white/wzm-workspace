// num7.cpp -- 编写一个程序，要求用户输入小时数和分钟数。在main()函数中，将这两个
// 值传递给一个void函数，后者以下面这样的格式显示这两个值：
// Enter the number of hours: 9
// Enter the number of minutes: 28
// Time: 9:28
#include <iostream>
void display(int m, int n);
int main()
{
    using namespace std;
    int hour, minutes;
    cout << "Enter the number of hours: ";
    cin >> hour;
    cout << "Enter the number of minutes: ";
    cin >> minutes;
    display(hour, minutes);
    return 0;
}

void display(int m, int n)
{
    using namespace std;
    cout << "Time: " << m << ":" << n << endl;
}