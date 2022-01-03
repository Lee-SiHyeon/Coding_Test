#include <iostream>
#include <string>

using namespace std;


int R, C, N;
char board[200][200];
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0, 1, 0, -1 };
int time_board[200][200];


int main(void)
{
	string st;

	cin >> R >> C >> N;

	for (int i = 0; i < R; ++i)
	{
		cin >> st;
		for (int j = 0; j < C; ++j)
		{
			board[i][j] = st[j];
			if (board[i][j] == 'O')
			{
				time_board[i][j] = 2; //�ʱ� - 1�ʿ� �ƹ��͵� ���ؼ� ��ó�� ��ź�� 2�� ����.
			}
		}
	}
	N--; //�ʱ� ����, 1�� �ƹ��͵� ���ϰ� ����.

	while (N != 0)
	{
		for (int i = 0; i < R; ++i)
		{
			for (int j = 0; j < C; ++j)
			{
				if (board[i][j] == '.')
				{
					board[i][j] = 'O';
					time_board[i][j] = 3;
				}
				else {
					time_board[i][j]--;
				}
			}
		}
		N--;
		if (N == 0) break;

		for (int i = 0; i < R; ++i)
		{
			for (int j = 0; j < C; ++j)
			{
				time_board[i][j]--;
				if (time_board[i][j] == 0)
				{
					board[i][j] = '.';
					for (int a = 0; a < 4; ++a)
					{
						int nx = i + dx[a];
						int ny = j + dy[a];
						if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
						board[nx][ny] = '.';
					}
				}
			}
		}
		N--;
	}
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cout << board[i][j];
		}
		cout << endl;
	}

}