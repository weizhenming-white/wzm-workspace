// num1.cpp -- 编写一个小程序，要求用户使用一个整数指出自己的身高（单位为英寸），
// 然后将身高转换为英尺和英寸，改程序使用下划线字符来指示输入的位置。
// 另外，使用一个const符号常量来表示转换因子。
//                              1米等于39.37英寸（in），1英尺（ft）等于12英寸（in）

#include <iostream>

const double Inch_per_feet = 12.0;
using namespace std;
int main()
{
    cout << "Please enter your height:_____\b\b\b\b\b";
    double ht_inch;
    cin >> ht_inch;

    double ht_feet = ht_inch / Inch_per_feet;
    cout << "Your height is:" << ht_feet << " feets" << endl;    
    
    return 0;
}
