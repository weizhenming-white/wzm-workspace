// num6.cpp -- 编写一个程序，其main()调用一个用户定义的函数（以光年值为参数，
// 并返回对应天文单位的值）。该程序按下面的格式要求用户输入光年值，并显示结果：
// Enter the number of light years: 4.2
// 4.2 light years = 265608 astronomical units.
// 天文单位是从地球到太阳的平均距离（约150000000公里或930000000英里），光年
// 是光一年走的距离（约10万亿公里或6万亿英里）（除太阳外，最近的恒星大约离地球
// 4.2 光年）。请使用double类型（参见程序清单2.4），转弯公式为：
//                                      1 光年 = 63240 天文单位

#include <iostream>
int calc(float n);
int main()
{
    using namespace std;
    cout << "Enter the number of light years: ";
    float tmp;
    cin >> tmp;
    int distan = calc(tmp);
    cout << tmp << " light years = " << distan << " astronomical units." << endl;
    return 0;
}

int calc(float n)
{
    return n * 63240;
}