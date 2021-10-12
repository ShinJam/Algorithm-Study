#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<vector>

using namespace std;

int cnt = 0;
int n, r, c;

void search(int x, int y, int size) {
	if (x == r && y == c) {
		cout << cnt;
		return;
	}

	if ((x <= r && r < x + size) && (y <= c && c < y + size))//내가 찾고자 하는 좌표가 포함되어있을시 4분할로 탐색
	{
		search(x, y, size / 2);
		search(x, y + size / 2, size / 2);
		search(x + size / 2, y, size / 2);
		search(x + size / 2, y + size / 2, size / 2);
	}
	else cnt += size * size;//1사분면부터 차례대로 포함되어있지 않다면 size*size만큼 더해준다
	return;
}

int main() {
	
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> r >> c;
	search(0, 0, pow(2, n));
}