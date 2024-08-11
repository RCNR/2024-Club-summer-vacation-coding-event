#include <bits/stdc++.h>
#define endl "\n"
#define rep(i, a, n) for(auto i = a; i < n; i++)
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)

using namespace std;

int main() {
	FAST_IO;
	
	string str;
	int cnt = 0;
	
	cin >> str;
	for(int i = 0; i < str.size(); i+=2) {
		if(str[i] == 'S' && str[i+1] == 'M') {
			cnt++;
		}
	}
	cout << cnt << '\n';
}