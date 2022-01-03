//https://jaimemin.tistory.com/572
#include <bits/stdc++.h>
using namespace std;

int N,M,K;
int cache[101][101]; //cache[A][Z], A의 개수(N), Z의 개수(M)로 만들 수 있는 사전의 수.
bool noresult = false;
string word;
int HowMany(int A, int Z)
{
    if(A == 0 || Z == 0 ) return 1;

    if(cache[A][Z] != -1) return cache[A][Z];

    return cache[A][Z] = min(HowMany(A-1, Z)+ HowMany(A, Z-1), 1000000000+1);
}

void getWord(int A, int Z, int skip)
{
    if( A==0){
        for(int i = 0; i<Z; i++) word += 'z';
        return;
    }
    if( Z==0){
        for(int i = 0 ; i<A; i++)  word += 'a';
        return;
    }

    int idx = HowMany(A-1,Z); // a를 썼을때 idx 값.
    if(skip < idx)
    {
        word += 'a';
        getWord(A-1,Z, skip);
    }
    else 
    {
        word += 'z';
        getWord(A, Z-1, skip-idx);
    }
    // else {
    //     noresult = true;
    // }

}

int main(void)
{
    cin >> N >> M >> K;

    memset(cache, -1, sizeof(cache));

    if(K > HowMany(N,M)) {
        cout << -1 ;
        return 0;
    }
    else{
        getWord(N,M, K-1);
    }
    // if(noresult ==true)
    //     cout << -1 << endl;

    cout << word<< endl;

    return 0;

}