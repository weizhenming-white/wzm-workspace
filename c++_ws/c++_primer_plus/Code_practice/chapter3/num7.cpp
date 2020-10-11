// num7.cpp -- 编写一个程序，要求每个用户按欧洲风格输入汽车的耗油量
// （每100公里消耗汽油量（升 ）），然后将其转换为美国风格的耗油量-每加仑多少英里。
// 注意，除了使用不同的单位计量外，美国方法（距离/燃料）与欧洲方法（燃料/距离）相反。
// 100公里等于62.14英里，1加仑等于3.875升。因此，19mpg大约合12.41/100km,127mpg大约合8.71/100km。
#include <iostream>
using namespace std;
int main()
{
    cout << "Please enter fuel consumption per 100 km(UN):";
    double UN;
    cin >> UN;

    cout <<" Gallons per mile(US) : "<< 1 / UN*62.14*3.875;
    return 0;
}