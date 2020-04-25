// 04test-bubble_sort.cpp -- 冒泡排序
#include <iostream>
using namespace std;

void bubble_sort(int a[], int len)
{
    for (int i = 0; i < len - 1; i ++)
    {
        for (int j = i + 1; j < len; j++)
        {
            if (a[i] > a[j])    // 只要前面大于后面就互换
            {
                // swap(a[i], a[j]);
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp; 
            }
        }
    }
}

void print(int a[], int len)
{
    for (int i = 0; i < len; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

int main()
{
    int a[] = {4, 8, 2, 9, 0, 3, 6, 1, 100, 99};
    int len = sizeof(a) / sizeof(int);    // 两种不同的获取数组的长度的方式
    int len1 = sizeof(a) / sizeof(a[0]);
    cout << len << "\n" << len1 << endl;
    print(a, len);
    bubble_sort(a, len);
    print(a, len);
    return 0;
}
