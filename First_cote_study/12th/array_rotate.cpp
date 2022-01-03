#include <iostream>
#include <vector>
#include <cstring>
using namespace std;


struct cal {  //1씩 빼서 넣어줘야함.
	int r;
	int c;
	int s;
};

vector<cal> vec;
vector<int> permu;
vector<int> test;

int N, M, K;
int visit[6] = { 0 };
int res_mini = 2147000000;
int board[51][51];

void calculate(void)
{
	int tmp_board[51][51];
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
			tmp_board[i][j] = board[i][j];
	}
	//memcpy(tmp_board, board, sizeof(board));


	for (int i = 0; i < K; i++)
	{
		int r, c, s;
		r = vec[test[i]].r;
		c = vec[test[i]].c;
		s = vec[test[i]].s;

		for (int a = 1; a <= s; ++a)
		{

			// r-a ~ r+a까지.
			// c-a ~ c+a까지
			int temp = tmp_board[r - a][c - a];
			int rr = r - a;
			int cc = c - a;
			while (rr != r + a)
			{
				tmp_board[rr][cc] = tmp_board[rr + 1][cc];
				rr++;
			}

			while (cc != c + a)
			{
				tmp_board[rr][cc] = tmp_board[rr][cc + 1];
				cc++;
			}
			while (rr != r - a)
			{
				tmp_board[rr][cc] = tmp_board[rr - 1][cc];
				rr--;
			}
			while (cc != c - a)
			{
				tmp_board[rr][cc] = tmp_board[rr][cc - 1];
				cc--;
			}
			tmp_board[r - a][c - a + 1] = temp;
		}
	}
	//경우의 수 대로 연산 완료.
	int board_min = 2147000000;
	for (int i = 0; i < N; i++)
	{
		int sum = 0;
		for (int j = 0; j < M; j++)
		{
			sum += tmp_board[i][j];
		}
		if (sum < board_min) board_min = sum;

	}

	if (board_min < res_mini) res_mini = board_min;

}


void dfs(void)
{
	if (permu.size() == K) {
		test = permu;
		calculate();
		return;
	}
	for (int i = 0; i < K; i++)
	{
		if (visit[i] == 0)
		{
			visit[i] = 1;
			permu.push_back(i);
			dfs();
			permu.pop_back();
			visit[i] = 0;
		}
	}
}

int main(void)
{

	cin >> N >> M >> K;

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			cin >> board[i][j];
		}
	}
	for (int i = 0; i < K; ++i)
	{
		int r, c, s;
		cin >> r >> c >> s;
		r--; c--;
		vec.push_back({ r,c,s });
	}
	dfs();

	cout << res_mini;
}