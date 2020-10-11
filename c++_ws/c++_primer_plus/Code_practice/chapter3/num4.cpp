// num4.cpp -- 4.编写一个程序，要求用户以整数方式输入秒数（使用long或long long变量存储），
// 然后以天、小时、分钟和秒的方式显示这段时间。使用符号常量来表示每天有多少小时、
// 每小时有多少分钟以及每分钟有多少秒。该程序的输出应与下面类似：
//                              Enter the number of seconds:3160000
//                              3160000 seconds = 365 days,17 hours,46 minutes,40 seconds

#include <iostream>
using namespace std;
const int Sec_per_min = 60;
const int Min_per_hour = 60;
const int Hour_per_day = 24;
int main()
{
    cout << "Enter the number of seconds:";
    long long total_sec;
    cin >> total_sec;

    int sec = total_sec%Sec_per_min;
    int total_min = total_sec / Sec_per_min;

    int min = total_min%Min_per_hour;
    int total_hour = total_min / Min_per_hour;
     
    int hour= total_hour%Hour_per_day;
    int day = total_hour / Hour_per_day;

    cout << total_sec << " seconds = " << day << " days," << hour << " hours," << min << " minutes," << sec << " seconds\n";
    return 0;
}