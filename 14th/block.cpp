#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;
void print_board(const vector<string>& board,int m, int n)
{
    for(int i =0 ; i<m; i++)
    {
        for(int j= 0 ; j<n ; j++)
        {
            cout << board[i][j]<< " ";
        }
        cout << endl;
    }
    cout << endl;
}
queue<pair<int,int>> q, q_del;
bool visit[30][30];
int dx[3] = { 0, 1, 1};
int dy[3] = {1, 1, 0};

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    bool flag =true;
    int stop = 0;
    while(flag)
    {
        for(int i = 0 ; i< m; i++)
        {
            for(int j = 0 ; j< n; j++)
            {
                if(visit[i][j] ==true) continue;
                if(board[i][j] == '0') continue;
                else
                {
                    q.push({i,j});
                    visit[i][j] = true;
                    while(!q.empty())
                    {
                        int x=q.front().first;
                        int y=q.front().second;
                        q.pop();
                        bool check=true; // 없앨수있을거란 가정하에 시작.
                        for(int a = 0 ; a<3; a++)
                        {
                            int nx = x+dx[a];
                            int ny = y+dy[a];
                            if(nx <0 || ny <0|| nx >m-1 || ny > n-1){
                                check = false;
                                continue;
                            } 
                            
                            if(board[nx][ny] != board[x][y]) //새로 간 곳이 기존이랑 다른거면. 
                            {
                                check = false;
                                break;
                                //없앨 수 없다고 표시하고 브레이크.
                            }
                        }
                        if(check) //위 for문을 정상적으로 나오면, 없앨 수 있으면
                        {
                            if(board[i][j] != '0') q_del.push({i,j});
                            for(int a = 0 ; a<3; a++)
                            {
                                if(visit[x+dx[a]][y+dy[a]] == true) continue;
                                visit[x+dx[a]][y+dy[a]] =true;
                                q.push({x+dx[a], y+dy[a]}); // 다시 탐색. 없앨 수 있는거 세개 다 큐에 푸쉬.
                                q_del.push({x+dx[a], y+dy[a]}); //나중에 한번에 지울 큐.
                            }
                        }
                    }
                }    
            
            }
        }
        while(!q_del.empty()) 
        {
            int x = q_del.front().first;
            int y = q_del.front().second;
            q_del.pop();
            //기존 보드에 0채워주기
            if(board[x][y] !='0')
            {
                board[x][y] = '0';
                answer ++;
            }
        }
        print_board(board, m,n);
        
        //보드 옮겨주기.
        for(int j = 0; j<n; j++)
        {
            int ins=0, del=0;
            bool ck = false; //지울게 없을수도 있어서.
            for(int i = m-1; i>=1 ; i--)
            {
                
                if(board[i][j] != '0' && board[i-1][j] == '0' || board[i][j] =='0' && board[i-1][j] =='0')
                {
                    if(ins !=0) continue;
                    ins = i-1;
                }
                if(board[i][j] == '0' && board[i-1][j] !='0')
                {
                    ck = true;
                    del = i-1;
                }
            }
            cout << "ins = " << ins << ", del = " << del << endl;
            if(ck)
            {
                while(del >=0)
                {
                    board[ins][j] = board[del][j];
                    board[del][j] = '0';
                    ins--;
                    del--;
                }
            }
            print_board(board, m,n);
        }
        memset(visit,false,sizeof(visit));
        cout << "pop block = " << answer << endl;
        
        if(stop == answer) break;

        stop = answer;
        
        int x ;
        cin >> x;
        
        
        
        
    }
    

    return answer;
}

int main()
{
    vector<string> vec = {"AAAAA","AUUUA","AUUAA","AAAAA"};
    print_board(vec,4,5);
    solution(4,5,vec);
}