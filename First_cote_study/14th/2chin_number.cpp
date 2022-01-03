#include <iostream>
#include <vector>
using namespace std;

vector<long long> vec;
long long K;

vector<long long> f_arr;

vector<long long> g_arr;
long long answer=0;
long long calcul_arr(long long num)
{
    int idx = 1;
    cout << "num = " << num << ", g_arr[idx] = " <<  g_arr[idx]<<endl;
    while(num >g_arr[idx] )
    {
        idx++;
        f_arr.push_back(f_arr[idx-1] + f_arr[idx-2]);
        g_arr.push_back(g_arr[idx-1] + f_arr[idx]);
        cout << "num = " << num << ", g_arr[idx] = " <<  g_arr[idx]<<endl;
    }
    // 뒤에 숫자가 필요해서 한번 더해주고.
    //num - g_arr[idx-1] 한게 그 층에서 몇번쨰 숫자인지.

    return idx;
}

void dfs(int primary , int depth, int idx,long long count) // 몇층까지 가야해 ?
{
    if(depth == idx){
        answer++;
        if(answer == count)
        {
            for(int i =0; i< vec.size(); i++)
            {
                cout << vec[i];
            }
            cout << endl;
        }
        return;
    }
    //0을 선택할때
    vec.push_back(0);
    dfs(0, depth+1, idx, count);
    vec.pop_back();
    


    //1을 선택할때 
    if(primary == 1) return; //1을 두번 연속 선택할 수 없으므로.

    vec.push_back(1);
    dfs(1,depth+1, idx, count);
    vec.pop_back();
       
    
}


int main(void)
{
    cin >> K;
    if(K==1){
        cout << 1;
        return 0;
    }
    f_arr.push_back(1);
    f_arr.push_back(1);
    g_arr.push_back(1);
    g_arr.push_back(2);
    //계산 초기화.


    int idx=calcul_arr(K);
    long long count = K-g_arr[idx-1];
    cout << "idx = " << idx << ", count =" << count << endl;
    vec.push_back(1);
    dfs(1, 0, idx, count); // 시작은 1로 시작,, 0층부터 해서 idx층 도달하면 return까지.
    return 0;
    
}