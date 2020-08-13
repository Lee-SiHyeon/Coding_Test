#include <iostream>
#include <fstream>
#include <string>

#include <deque>
#include <queue>
#include <cmath>

using namespace std;

deque<int> dq[4];

queue<pair<int, int>> q;
int K;
queue<int> rotateQ;
int visited[4];
void rotate(int Gnum, int dir)
{
    
    if (dir == 1) { //dir ==1
        int temp = dq[Gnum].back();
        dq[Gnum].pop_back();
        dq[Gnum].push_front(temp);
    }
    else
    {
        int temp = dq[Gnum].front();
        dq[Gnum].pop_front();
        dq[Gnum].push_back(temp);
    }


}

void check(int Gnum)
{
    
    //left check
    if ( Gnum >= 1 && dq[Gnum][6] != dq[Gnum - 1][2] && visited[Gnum - 1] == 0 )
    {
        rotateQ.push(Gnum - 1);
        visited[Gnum - 1] = 1;
        check(Gnum - 1);
        visited[Gnum - 1] = 0;
    }

    //right check
    if (Gnum <= 2 &&dq[Gnum][2] != dq[Gnum + 1][6] && visited[Gnum + 1] == 0 )
    {
        rotateQ.push(Gnum+1);
        visited[Gnum + 1] = 1;
        check(Gnum + 1);
        visited[Gnum + 1] = 0;
    }

    return;

}
int solve()
{
    while (!q.empty())
    {
        pair<int, int> tmp = q.front();
        int Gnum = tmp.first - 1;
        int dir = tmp.second;
        q.pop();
        //dfs로 어디까지 들어가야하는지 탐색하고 (check)
        rotateQ.push(Gnum);
        visited[Gnum] = 1;
        check(Gnum);
        visited[Gnum] = 0;

        while (!rotateQ.empty())
        {
            int RoGnum = rotateQ.front();
            rotateQ.pop();
            if (abs(Gnum - RoGnum) % 2 == 0) {
                if (dir == 1) {
                    rotate(RoGnum, 1);

                }
                else rotate(RoGnum, -1);
            }
            else {
                if (dir == 1) {
                    rotate(RoGnum, -1);
                }
                else rotate(RoGnum, 1);
            }
        }

        //해당 톱니바퀴들 rotate
    }

    //점수계산
    int res = 0;
    for (int i = 0; i < 4; i++)
    {
        if (dq[i][0] == 1) res += (int)pow(2, i);
    }
    return res;

}

int main(void)
{

    string str_arr[4];
    for (int i = 0; i < 4; ++i)
    {
        string temp;
        cin >> temp;
        str_arr[i] = temp;
    }
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 8; ++j)
        {
            dq[i].push_back(str_arr[i][j]-'0');
        }
    }

    cin >> K;
    for (int i = 0; i < K; i++)
    {
        int temp1, temp2;
        cin >> temp1 >> temp2;
        q.push({ temp1,temp2 });
    }

    cout << solve();

}