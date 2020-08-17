// num4.cpp 让用户输入其年龄，然后显示该年龄包含多少个月，如下所示：
//                                      Enter your age: 29

#include <iostream>
int main()
{
    using namespace std;

    cout << "Enter your age: ";
    int ages;
    cin >> ages;
    cout << "Your age is " << ages << " include " << ages * 12 << " month." << endl;
    return 0;
}