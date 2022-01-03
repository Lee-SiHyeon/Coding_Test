#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int W[100], V[100];
int N,K;
int dp[101][10001];

int go(int i , int w)
{
    if (dp[i][w] >0) return dp[i][w];
    if(i==N) return 0;
    int n1=0;
    if(w+W[i] <= K)
     n1 = V[i] + go(i+1, w+ W[i]); // 포함
    int n2 = 0 + go(i+1, w); //미포함
    return dp[i][w] = max(n1,n2); 
    // 채워들어갈때 cache에 저장하고, line 12에서 동일한 곳에 들어가려고 하면 바로 리턴.
}


int main(void)
{
    ifstream in("input.txt");
    in >> N >> K;

    cout << N << " " << K << endl;
    for ( int i = 0 ; i<N; i++)
    {
        in >> W[i] >> V[i];
        cout << W[i] << " " << V[i]<<endl;
    }
    
    cout << go(0,0);
}