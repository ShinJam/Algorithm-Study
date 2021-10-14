#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<set>
#include<vector>

using namespace std;

typedef struct info{
	int day;
	int money;
};

int n,day,money;
vector<info>v;
int dp[16];

int main() {

	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> day>>money;
		v.push_back({ day,money });
	}

	for (int j = v.size()-1; j >= 0; j--) {
		if (v[j].day > n - j) dp[j] = dp[j + 1];
		else dp[j] = max(v[j].money + dp[j + v[j].day], dp[j + 1]);
	}

	cout << dp[0];

}