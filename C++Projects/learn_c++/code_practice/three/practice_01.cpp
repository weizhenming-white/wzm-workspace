// practice_01.cpp -- test practice input
#include <iostream>
#include <cctype>
#include <unistd.h>

using namespace std;

int main()
{
    cout << "Please enter characters (type @ to stop):";
    char ch;
    cin.get(ch);
    while (ch != '@')
    {
        if (islower(ch))
            ch = toupper(ch);
        else if (isupper(ch))
            ch = tolower(ch);
        if (!isdigit(ch))
            cout << ch;
        cin.get(ch);
    }
    pause();
    return 0;
}