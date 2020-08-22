// num.cpp -- 使用3个用户定义的函数（包括main()），并生成下面的输出：
//                              Three blind mice
//                              Three blind mice
//                              See how they run
//                              See how they run

#include <iostream>

void msg1();
void msg2();
int main()
{
    msg1();
    msg1();
    msg2();
    msg2();
    return 0;
}

void msg1()
{
    using namespace std;
    cout << "Three blind mice" << endl;
}

void msg2()
{
    using namespace std;
    cout << "See how they run" << endl;
}