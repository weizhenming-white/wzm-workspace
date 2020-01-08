// practice_03.cpp -- test create function

#include <iostream>

using namespace std;

void test_01();
void test_02();

int main()
{
    test_01();
    cout << endl;
    test_01();
    cout << endl;
    test_02();
    cout << endl;
    test_02();
    cout << endl;
    return 0;
}

void test_01()
{
    cout << "Three blind mice";
}
void test_02()
{
    cout << "See how they run";
}