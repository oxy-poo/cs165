#include <iostream>
#include <valarray>
#include "md5.h"
using namespace std;
 //$1$4fTgjp6q$nd4.kYa98cdFa3X85Ho8j1

 //zhgnnd
 //hfT7jp2q
int main(int argc, char *argv[])
{
    string pw = "zhgnnd";
    string s = "hfT7jp2q";
    string as = pw + s + pw;
    int pwlen = pw.length();
    cout << (string)md5(as) << endl;
    as = (string)md5(as);
    string pw_m_s = pw + "$1$" + s;
    
    for(pwlen;pwlen > 0;pwlen-=16){
        pw_m_s += as.substr(0,(pwlen > 16) ? 16 : pwlen);
        cout << pw_m_s << endl;
    }

    for(int i = pw.length(); i != 0; i >>=1){
        pw_m_s += (i & 1) ? '0' : pw.at(0);
        cout << pw_m_s << endl;
    }

    cout << md5(pw_m_s) << endl;


    return 0;
}