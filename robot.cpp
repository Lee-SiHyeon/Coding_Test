#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;


struct robot {
    int x;
    int y;
    int dir;
};
int A, B;
int map[100][100];
int dx[4] = { -1, 0 , 1, 0};
int dy[4] = { 0 , 1, 0, -1};
int N, M;
vector<robot> v;

int move(int robot_num, int cnt)
{
    int dir = v[robot_num].dir;
    int x = v[robot_num].x;
    int y = v[robot_num].y;
    for (int i = 0; i < cnt; i++)
    {
        int xx = x + dx[dir];
        int yy = y + dy[dir];
        if (xx < 0 || xx >= A || yy < 0 || yy >= B) return -1; // 벽에 부딪히는 경우
        if (map[xx][yy] == 1)
        {
            for (int j = 0; j < v.size(); j++)
            {
                if (v[j].x == xx && v[j].y == yy) return j;
            }
        }
        x = xx;
        y = yy;
    }
    map[v[robot_num].x][v[robot_num].y] = 0;
    v[robot_num].x = x;
    v[robot_num].y = y;
    map[x][y] = 1;
    return 1000;
}
void rotate(int robot_num, char ord, int cnt)
{
    int sum = 0;
    if (ord == 'R') {
        sum = cnt + v[robot_num].dir;
    }
    else sum = 3 * cnt + v[robot_num].dir;

    v[robot_num].dir = sum % 4;
}
string solve(int rb, char ord, int cnt)
{
    
    int robot_num = rb - 1;
    if (ord == 'F') {
        int res = move(robot_num, cnt);
        if (res == -1) {
            cout << "Robot " << rb << " crashes into the wall";
            return "CRASH";
        }
        else if (res == 1000) return "OK";
        else {
            cout << "Robot " << rb << " crashes into robot " << res+1;
            return "CRASH";
        }
    }
    else {
        rotate(robot_num, ord, cnt);
        return "OK";
    }
}

int main(void)
{
    cin >> A >> B >> N >> M;
    for (int i = 0; i < N; ++i)
    {
        int x, y;
        char dir;
        robot temp;
        cin >> temp.x >> temp.y >> dir;
        temp.x--;
        temp.y--;
        map[temp.x][temp.y] = 1;
        if (dir == 'N') temp.dir = 1;
        else if (dir == 'E') temp.dir = 2;
        else if (dir == 'S') temp.dir = 3;
        else temp.dir = 0;
        v.push_back(temp);
    }

 

    for (int i = 0; i < M; i++)
    {
        int rb, cnt;
        char ord;
        cin >> rb >> ord >> cnt;
        string res = solve(rb, ord, cnt);
        if (res =="CRASH") break;
        if (i == M - 1 && res == "OK") cout << "OK"; // 마지막 명령 수행하고 OK 가 리턴되어 오면 OK출력.
    }
}