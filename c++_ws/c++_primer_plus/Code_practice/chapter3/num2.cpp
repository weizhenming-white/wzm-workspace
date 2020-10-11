// num1.cpp -- 编写一个程序，要求以几英尺几英寸的方式输入其身高，并以磅为单位输入其体重。
//（使用3个变量来存储这些信息。）该程序报告其BMI（Body Mass Index ,体重指数）。
// 为了计算BMI，该程序以英寸的方式指出用户的身高（一英尺为十二英寸），
// 并将以英寸为单位的身高身高转换为以米为单位的身高（1英寸=0.0254米）。
// 然后，将以磅为单位的体重转换为千克为单位的体重（1千克=2.2磅）。
// 最后，计算相应的BMI-体重（千克）除以身高（米）的平方。用符号常量表示各种转换因子。


#include <iostream>
using namespace std;
const double Inch_per_feet = 12.0;
const double Meter_per_inch = 0.0254;
const double Pound_per_kilogram = 2.2;
int main()
{
    cout << "Enter your height of feet:";
    double ht_feet;
    cin >> ht_feet;

    cout << "Enter your height of inch:";
    double ht_inch;
    cin >> ht_inch;

    double ht_meter = (ht_feet*Inch_per_feet + ht_inch)*Meter_per_inch;

    cout << "Enter your weight in pound: ";
    double wt_pound;
    cin >> wt_pound;

    double wt_kilogram = wt_pound / Pound_per_kilogram;

    double BMI = wt_kilogram / ht_meter/ht_meter;
    cout << "BMI:" << BMI << endl;
    return 0;
}