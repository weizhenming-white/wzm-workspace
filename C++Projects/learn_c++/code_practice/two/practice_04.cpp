// practice_04.cpp -- calc Invest in Jia
#include <iostream>
int main()
{
    using namespace std;
    double Daphne_money = 100;
    double Cleo_money = 100;
    int count = 0;
    while (true)
    {
        count += 1;
        Daphne_money += 10;
        double tmp;
        tmp = Cleo_money * 0.05;
        Cleo_money = Cleo_money + (Cleo_money * 0.05);
        cout << count << " year, " << "Daphne's money is "
            << Daphne_money << "\tCleo's money is " << Cleo_money
            << endl;
        cout << "Daphne's profit is 10\tCleo's profit is " << tmp << endl << endl;
        if (Daphne_money < Cleo_money)
        {
            cout << "Now Cleo's money is exceed Daphne's money\n";
            break;
        }
    }
    return 0;
}