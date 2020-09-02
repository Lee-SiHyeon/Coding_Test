#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <queue>

#include <fstream>

using namespace std;


int T, N;
char board[300][300] = { 'N' };
bool visit[300][300] = { false };
int dx[8] = { -1, -1, 0, 1, 1, 1, 0 , -1 };
int dy[8] = { 0, 1, 1, 1, 0 , -1, -1, -1 };
int result = 0;
queue<pair<int, int>> q;
void print_board()
{
	cout << "print board" << endl;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cout << board[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

void print_visit()
{
	cout << "print visit" << endl;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cout << visit[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

void solve()
{
	//8방향이 모두 지뢰가 없는 칸을 기준으로 bfs탐색할것.
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (board[i][j] == '*') continue;
			bool flag = true;
			for (int a = 0; a < 8; a++)
			{
				int nx = i + dx[a];
				int ny = j + dy[a];
				if (nx <0 || nx > N - 1 || ny < 0 || ny > N - 1) continue;
				if (board[nx][ny] == '*')  
				{
					flag = false;
					break;
				}
			}
			if (flag && visit[i][j] ==false)
			{
				
				//cout << "x = " << i << ", y = " << j << endl;
				q.push({ i,j });
				while (!q.empty())
				{

					int x = q.front().first;
					int y = q.front().second;
					q.pop();
					if (visit[x][y] == true) continue;

					visit[x][y] = true;
					board[x][y] = '0';

					for (int a = 0; a < 8; a++)
					{
						int nx = x + dx[a];
						int ny = y + dy[a];
						if (nx <0 || nx > N - 1 || ny <0 || ny > N - 1) continue;
						board[nx][ny] = '0';
						bool flag = true;
						for (int b = 0; b < 8; b++)
						{
							int nnx = nx + dx[b];
							int nny = ny + dy[b];
							if (nnx < 0 || nnx>N - 1 || nny <0 || nny > N - 1) continue;
							if (board[nnx][nny] == '*')
							{
								flag = false;
								break;
							}
						}
						if (flag) q.push({ nx,ny });
					}
					//print_board();
				}
				result++;
			}
		}
	}
	

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (board[i][j] == '.')
				result++;
		}
	}
}
int main(void)
{
	ifstream in("input.txt");

	in >> T;

	string st;
	for (int i = 0; i < T; i++)
	{
		in >> N;

		for (int j = 0; j < N; j++)
		{
			in >> st;
			for (int a = 0; a < N; a++)
			{
				board[j][a] = st[a];
				
			}
		}
		//print_board();
		//print_visit();
		solve();
		cout << "#"<<i+1<< " " << result << endl;
		result = 0;
		memset(board, 'N' , sizeof(board));
		memset(visit, false, sizeof(visit));
	}
}