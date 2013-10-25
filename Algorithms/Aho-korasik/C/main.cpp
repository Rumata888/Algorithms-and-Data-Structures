#include <string>
#include <vector>
using namespace std;
struct bohr_vrtx {
	int next_vrtx[26], pat_num;
	int auto_move[26],par;
	char symb;
	bool flag;
	int suff_link;
};

vector<bohr_vrtx> bohr;
vector<string> pattern;

bohr_vrtx make_bohr_vrtx(int p, char c) {
	bohr_vrtx v;
	memset(v.next_vrtx, 255, sizeof(v.next_vrtx));
	memset(v.auto_move, 255, sizeof(v.auto_move));
	v.flag = false;
	v.par=p;
	v.symb=c;
	v.suff_link=-1;
	return v;
}
void bohr_ini() {
	bohr.push_back(make_bohr_vrtx());
}
void add_string_to_bohr(string &s) {
	int index = 0;
	for (int i = 0; i < s.length(); i++) {
		char zh = s[i] - 'a';
		if (bohr[index].next_vrtx[zh] == -1) {
			bohr.push_back(make_bohr_vrtx());
			bohr[index].next_vrtx[zh] =bohr.size()-1;
		}
		index=bohr[index].next_vrtx[zh];
	}
	bohr[index].flag=true;
	pattern.push_back(s);
	bohr[index].pat_num=pattern.size()-1;
}

bool check_if_in_bor(string &s)
{
	int index=0;
	for(int i=0;i<s.length();i++)
	{
		if(bohr[index].next_vrtx[s[i]-'a']==-1)
		{
			return false;
		}
		index=bohr[index].next_vrtx[s[i]-'a'];
	}
	return true;
}
