// floatnum.cpp -- floating-point types

#include <iostream>
int main()
{
    using namespace std;
    cout.setf(ios_base::fixed, ios_base::floatfield);               // fixed-point
    float tub = 10.0 / 3.0;                     // good to about 6 places
    double mint = 10.0 /3.0;                // good to about 15 places
    const float millon = 1.0e6;

    cout << "tub = " << tub;    
    cout << ", a millon tubs = " << millon * tub;
    cout << "\nand ten millon tubs = ";
    cout << 10 * millon * tub << endl;

    cout << "mint = " << mint << " and a millon mints = ";
    cout << millon * mint << endl;
    return 0;
}