#include <iostream>
#include <map>
#include <thread>
#include "md5.h"
using namespace std;

map<string,string> complete_table;

string strToBinary(string s){
	string bin = "";
	int n = s.length();
	for(int i = 0 ;i <=n;i++){
		int val = int(s[i]);
		while(val > 0){
			bin = bin + (val % 2)? '1' : '0';
			val/=2;
		}
	}
	reverse(bin.begin(),bin.end());
}


int main(){

//team9:$1$4fTgjp6q$nd4.kYa98cdFa3X85Ho8j1:16653:0:99999:7:::
	string password = "aaaaaa";
	string magic = "$1";
	string salt = "4fTgjp6q";
	string pwlen = (string)length(password)
	string hash = "nd4.kYa98cdFa3X85Ho8j1"; 
	string alternate_sum = md5(password + salt + password);
	string intermediate_0 = md5(password + magic + salt);
	string itoa64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	
	for(int i = pwlen,pwlen >0;pw-=16){
		intermediate_0 = intermediate_0 + 
	}
	return 0;

}
