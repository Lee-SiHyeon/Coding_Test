#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <fstream>

using namespace std;

int board[100][100];
int temp_board[100][100];
bool visit[100][100] = { false, };
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0 , -1 };


int N, M;
queue<pair<int, int>> q;
queue<pair<int, int>> q1;

int time = 0;

bool check()
{
   for (int i = 0; i < N; i++)
   {
      for (int j = 0; j < M; j++)
      {
         if (board[i][j] == 1) return false;
      }
   }
   return true;
}
void bfs()
{
    int cnt = 0;
    while (1) 
    {
        memcpy(temp_board, board,sizeof(temp_board));
        memset(visit,false,sizeof(visit));
        
        q.push({0,0});
        while (!q.empty())
        {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            if (visit[x][y] == true) continue;
            visit[x][y] = true;
            for (int a = 0; a < 4; a++)
            {
                int nx = x + dx[a];
                int ny = y + dy[a];
                if (nx<0 || nx > N - 1 || ny < 0 || ny >M - 1) continue;
                if (temp_board[nx][ny] == 1) continue;
                temp_board[nx][ny] = 5;
                
                q.push({ nx,ny });
            }
        }
       

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                if (temp_board[i][j] == 1) 
                {
                    int count = 0;
                    for (int a = 0; a < 4; a++)
                    {
                        int nx = i + dx[a];
                        int ny = j + dy[a];
                        if (nx < 0 || nx > N - 1 || ny < 0 || ny > M - 1) continue;
                        if (temp_board[nx][ny] == 5) count++;
                    }
                    if (count >= 2) {
                        q1.push({ i,j }); //나중에 지워야 하는 치즈.
                    }
                }
            }
        }
        
        while (!q1.empty())
        {
            int x = q1.front().first;
            int y = q1.front().second;
            board[x][y] = 0;
            q1.pop();
        }
        time++;
        if (check()) { break; }
        }
   
}

int main(void)
{
   cin >> N >> M;

   for (int i = 0; i < N; i++)
   {
      for (int j = 0; j < M; j++)
      {
         cin >> board[i][j];
      }
   }

   
   bfs();

   cout << time;

}