// practice_02.cpp -- test double list avg
#include <iostream>
#include <array>
using namespace std;
int main()
{
    array<double,10>donations;
    double sum=0;
    cout<<"Please enter donation(non-number to stop):";
    int i;
    double donation;
    for(i=0;(i<10)&&(cin>>donation);++i)
    {
        donations[i]=donation;
        // cout << "donations[i] = " << donations[i] << endl;
        sum+=donations[i];
    }    
    cout << "sum = " << sum << endl;
    double avg=sum/(i+1);
    cout<<"Average:"<<avg<<endl;
    cout<<"Number larger than average:";
    for(int j=0;j<i;j++)
     {
        if(donations[j]>avg)
            cout<<donations[j]<<" ";
     }   
    cout<<endl;
    return 0;
}
