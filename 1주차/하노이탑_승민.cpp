#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<set>
#include<vector>

using namespace std;

int n;

void recursion(int from, int to, int tmp, int cnt) {
	if (cnt == 1) {
		cout << from << ' ' << to << '\n';
	}
	else {
		recursion(from, tmp, to, cnt - 1);
		cout << from << ' ' << to << '\n';
		recursion(tmp, to, from, cnt - 1);
	}
	return;
}

int main() {

	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	
	string ans = to_string(pow(2, n));//2의 N승을 스트링으로 변환
	ans = ans.substr(0, ans.find('.'));//뒤에 소숫점 제거

	if (ans[ans.length() - 1] == '0') {
		ans[ans.length() - 2] -= 1;
		ans[ans.length() - 1] = '9';
	}

	else {
		ans[ans.length() - 1] -= 1;
	}

	cout << ans << '\n';
	
	if(n<=20)recursion(1, 3, 2, n);

}