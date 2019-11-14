#include <iostream>
using namespace std;
int main() {
    int first_num, second_num, sum;
    cout << "please input two int: ";
    cin >> first_num >> second_num;

    sum = first_num + second_num;
    cout << first_num << "+" << second_num << "=" << sum;
    
    return 0;
}