#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> GraphArr[300001];
int N;
long long num_D=0, num_G = 0;
void solve(){
    for(int i = 1 ; i<=N ; ++i)
    {
        for(int j = 0 ; j<GraphArr[i].size(); ++j)
        {
            num_D += ((long long)GraphArr[i].size()-1)*((long long)GraphArr[GraphArr[i][j]].size()-1);
        }
        //num_G += ((long long)GraphArr[i].size()*((long long)GraphArr[i].size()-1)*((long long)GraphArr[i].size()-2))/6;
        long long temp = GraphArr[i].size();
        num_G += temp*(temp-1)*(temp-2)/6;
        num_D/=2;
    }
}



int main(void)
{
    ios::sync_with_stdio(false);
	cin.tie(NULL);
    cin >> N;

    //양방향 그래프 생성.
    for(int i = 1; i<N; ++i)
    {
        int a, b;
        cin >> a >> b;
        GraphArr[a].push_back(b);
        GraphArr[b].push_back(a);
    }

    solve();
    if(num_D > num_G*3) cout << "D" << "\n";
    else if( num_D < num_G*3) cout << "G" << "\n";
    else cout << "DUDUDUNGA";
    return 0;
}