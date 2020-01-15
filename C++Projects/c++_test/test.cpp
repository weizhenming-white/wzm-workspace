#include <iostream>
#include <string>
#include <stack>
//#define fin cin
//#define fo
using namespace std;
bool isOperator(char x)
{
    if(x=='('||x==')'||x=='+'||x=='-'||x=='*'||x=='/')
        return true;
    else
        return false;
}
int getPriority(char x)
{
    if(x=='+'||x=='-')
        return 1;
    if(x=='*'||x=='/')
        return 2;
    if(x=='(')
        return 0;
}
bool isBracket(char x)
{
    if(x=='('||x==')')
        return true;
    else
        return false;
}
int doOperate(int d1,int d2,char t)
{
    //cout<<d1<<" "<<t<<" "<<d2<<endl;
    if(t=='+')
        return (d1+d2);
    if(t=='-')
        return (d1-d2);
    if(t=='*')
        return (d1*d2);
    if(t=='/')
        return (d1/d2);
 
 
}
int main()
{
    stack<int> Q;
    stack<char> S;
    string str;
    cin>>str;
    char x;
    int opnum;
    string temp="";//临时存放操作数
    int d2,d1;
    char t;
    //cout<<str.size()<<endl;
    //cout<<str[str.size()-1]<<endl;
    for(int i=0;i<str.size();i++)
    {
        x=str[i];
        //cout<<x<<endl;
    }
    for(int i=0;i<str.size();i++)
    {
        x=str[i];
        //cout<<x<<endl;
        //如果是操作数
 
        if(x>=48&&x<=57)
        {
            temp.append(1,x);
        }
        if(isOperator(x))
        {
            if(temp!="")
            {
                opnum=stoi(temp);
                //cout<<opnum<<endl;
                Q.push(opnum);
                temp="";
            }
            if(S.empty())
                S.push(x);
            else{//栈中有一个（，然后压入一个+，由于（的优先级未知而出错
                if(x=='('||
                        ((!isBracket(x))&&
                         (getPriority(x)>getPriority(S.top()))))
                    S.push(x);
                else
                    if(x==')')
                    {
                        while(S.top()!='(')
                        {
                            d2=Q.top();
                            Q.pop();
                            d1=Q.top();
                            Q.pop();
                            t=S.top();
                            S.pop();
                            Q.push(doOperate(d1,d2,t));
                        }
                        S.pop();//弹出）
                    }
                    else
                    {
                        while(!S.empty()&&
                              ((getPriority(S.top())>getPriority(x))||(getPriority(x)==getPriority(S.top()))))
                        {
                            d2=Q.top();
                            Q.pop();
                            d1=Q.top();
                            Q.pop();
                            t=S.top();
                            S.pop();
                            Q.push(doOperate(d1,d2,t));
                        }
                        S.push(x);
                    }
            }
        }
        if(!isOperator(x)&&i==str.size()-1)
            Q.push(stoi(temp));
 
    }
    while(!S.empty())
    {
        d2=Q.top();
        Q.pop();
        d1=Q.top();
        Q.pop();
        t=S.top();
        S.pop();
        Q.push(doOperate(d1,d2,t));
    }
    cout<<Q.top();
    /*
    if(Q.size()==2)
    {
        d2=Q.top();
        Q.pop();
        d1=Q.top();
        Q.pop();
        t=S.top();
        S.pop();
        Q.push(doOperate(d1,d2,t));
    }
    */
    return 0;
}