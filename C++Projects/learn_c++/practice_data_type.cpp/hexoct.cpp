// hexoct.cpp -- shows hex and octal literals
#include <iostream>
int main()
{
    using namespace std;

    int chest = 42;                     // decimal integer literals
    int waist = 0x42;                   // hexadecimal integer literals
    int inseam = 042;               // octal integer literals

    cout << "Monsieur cuts a striking figure!" << endl;
    cout << "chest = " << chest << " (42 in decimal)" << endl;
    cout << "waist = " << waist << " (0x42 in hex)" << endl;
    cout << "instram = " << inseam << " (042 in octal)" << endl;
    return 0;
}