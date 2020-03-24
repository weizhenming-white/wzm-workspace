// 03test-calculator.cpp -- calculator simple data
#include <iostream>
using namespace std;
 
int main()
{
    char op;
    float num1, num2;
 
    cout << "Please enter operator：+、-、*、/ : ";
    cin >> op;
 
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;
 
    switch(op)
    {
        case '+':
            cout << num1+num2 << endl;
            break;
 
        case '-':
            cout << num1-num2 << endl;
            break;
 
        case '*':
            cout << num1*num2 << endl;
            break;
 
        case '/':
            cout << num1/num2 << endl;
            break;
 
        default:
            // 如果运算符不是 +, -, * 或 /, 提示错误信息
            cout << "Error!  Please enter the correct operator: ";
            break;
    }
 
    return 0;
}