#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>

using namespace std;

int L, C;
char ch;
vector<char> v;

void dfs(int index,int collection, string tmp) {
	
	if (tmp.length() == L&&collection>0&&tmp.length()-collection>1) {
		cout << tmp<<'\n';
		return;
	}

	for (int i = index; i < v.size(); i++) {
		tmp.push_back(v[i]);
		if (v[i] == 'a' || v[i] == 'e' || v[i] == 'i' || v[i] == 'o' || v[i] == 'u')
			dfs(i + 1, collection + 1, tmp);
		else
			dfs(i + 1, collection, tmp);
		tmp.pop_back();
	}
}

int main(){
	
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> L >> C;
	for (int i = 0; i < C; i++) {
		cin >> ch;
		v.push_back(ch);
	}
	sort(v.begin(), v.end());
	string tmp = "";
	dfs(0, 0,tmp);


}