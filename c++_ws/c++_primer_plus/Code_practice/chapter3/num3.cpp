// num3.cpp -- 编写一个程序，要求用户以度分秒的方式输入一个纬度，然后以度为单位显示该纬度。
// 1度为60分，1分等于60秒，请以符号常量的方式表示这些值。对于每个输入值，
// 应使用一个独立的变量存储它。下面是该程序运行时的情况：
//                      Enter a latitude in degrees,minutes,and seconds:
//                      First,enter the degrees:37
//                      Next,enter the minutes of arc:51
//                      Finally,enter the seconds of arc:19
//                      37 degrees,51 minutes,19 seconds =37.8553 degrees

#include <iostream>
using namespace std;
const double Minute_per_degree = 60.0;
const double Second_per_minute = 60.0;
int main()
{
    cout << "Enter a latitude in degrees,minutes,and seconds:"<<endl;
    cout << "First,enter the degrees:";
    int degrees;
    cin >> degrees;

    cout << "Next,enter the minutes of arc:";
    int minutes;
    cin >> minutes;

    cout << "Finally,enter the seconds of arc:";
    int seconds;
    cin >> seconds;

    double Degree = degrees + minutes / Minute_per_degree + seconds / Second_per_minute / Minute_per_degree;

    cout << degrees << " degrees, " << minutes << " minutes, " << seconds << " seconds = " << Degree<< " degrees\n";
    return 0;
}