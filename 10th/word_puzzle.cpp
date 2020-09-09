#include <iostream>
#include <string>
#include <vector>
using namespace std;

//주어진 것으로 못만들면 -1을 return
// t는 1이상 20,000 이하

int dp[20000];

int solution(vector<string> strs, string t)
{
	int answer = 0;
	
	for (int p = 0; p < t.size(); p++) {

		int index = p;
		char c = t[p];
		dp[index] = t.size() + 1; //디폴트값, 만들 수 없는 최대값

		for (int i = 0; i < strs.size(); i++) {
			bool same = true;
			int length = strs[i].size() - 1;
			if (strs[i][length] == c) { //마지막 문자가 같을 때

				for (int k = 0; k <= length; k++) { // 부분 문자열 비교
					if (t[index - k] != strs[i][length - k]) {
						same = false;
						break;
					}
				}

				if (same) { //부분 문자열이다.
					if (index - length - 1 == -1) { // 시작지점일때
						dp[index] = 1;
					}
					else {// 시작지점이아니면 최소값을 찾아 dp에 갱신
						if (dp[index - length - 1] + 1 < dp[index]) { 
							dp[index] = dp[index - length - 1] + 1;
						}
					}
				}
			}
		}
	}


	answer = dp[t.size() - 1];
	if (answer >= t.size()+1) {
		answer = -1;
	}


	return answer;
}