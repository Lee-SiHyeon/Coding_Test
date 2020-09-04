#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <fstream>
#include <algorithm>

using namespace std;

//node[0], node[1] = source, destination 노드넘버
//distance 거리
class Edge{
public:
    int node[2];
    int distance;
    Edge(int a, int b, int distance)
    {
        this->node[0] = a;
        this->node[1] = b;
        this->distance = distance;
    }
    //distance 오름차순으로 정렬.
    bool operator <(Edge &edge){
        return this->distance < edge.distance;
    }
};
int N,M;
int board[10][10];
bool visit[10][10] = {false};
int dx[4] = { -1, 0 , 1, 0};
int dy[4] = { 0, 1, 0, -1};
queue<pair<int,int>> q;

int graph[7][7]= {1000};

int numbering = 1;
vector<Edge> v;

int getParent(int parent[], int a)
{
    if(parent[a] == a) return a;
    return parent[a] = getParent(parent, parent[a]);
}
void unionParent(int parent[], int a, int b)
{
    a = getParent(parent, a);
    b = getParent(parent,b);
    if(a<b) parent[b] = a;
    else parent[a] = b;
}
int findParent(int parent[], int a, int b)
{
    a = getParent(parent, a);
    b = getParent(parent, b);
    if(a == b) return 1;
    else return 0;
}

int main(void)
{
    memset(graph, 100, sizeof(graph));
    
    
    cin >> N >> M;
    for(int i = 0 ; i< N; ++i)
    {
        for(int j=  0 ; j< M; ++j)
        {
            cin >> board[i][j];
        }
    }

    //인풋값들 다 받았고, bfs써서 섬들 구분할거임.

    //번호로 섬 구별하기
    for(int i = 0 ; i< N; ++i)
    {
        for(int j = 0 ; j< M ; ++j)
        {
            if(board[i][j] != 0 && visit[i][j] == false)
            {
                visit[i][j] = true;
                q.push({i,j});
                while(!q.empty())
                {
                    int x = q.front().first;
                    int y = q.front().second;
                    int temp_num = board[x][y];
                    board[x][y] = numbering;
                    q.pop();

                    for(int a = 0; a<4; ++a)
                    {
                        int nx = x+dx[a];
                        int ny = y+dy[a];
                        if(nx <0 || ny <0 || nx >N-1 || ny >M-1) continue;
                        if(temp_num ==board[nx][ny] && visit[nx][ny] ==false)
                        {
                            visit[nx][ny] = true;
                            q.push({nx,ny});
                        }
                    }
                }
                numbering++;
            }
        }
    }
    
    //섬들간 거리측정.
    for(int i= 0 ; i<N; ++i)
    {
        for(int j = 0 ; j<M; ++j)
        {
            if(board[i][j] != 0)
            {
                for(int a = 0; a<4; ++a)
                {
                    int nx = i+dx[a];
                    int ny = j+dy[a];
                    if(nx<0 || ny < 0 || nx >N-1 || ny > M-1 || board[nx][ny] !=0) continue;
                    int count = 1;
                    while(1)
                    {
                        nx += dx[a];
                        ny += dy[a];
                        if(nx <0 || ny<0 || nx > N-1 || ny > M-1)
                        {
                            break;
                        } 
                        if(board[nx][ny] !=0 && count ==1) break;
                        //가도 괜찮은 곳임.
                        //여기까지 왔으면 가도 괜찮은 곳인데, 0이다가 숫자를 마주칠거임.
                        if(board[nx][ny] != 0 && count != 1) //숫자를 마주치면.
                        {
                            if(graph[board[i][j]][board[nx][ny]] >count){
                                graph[board[i][j]][board[nx][ny]] = count;
                            }
                            break;
                        }

                        //0을 마주치면 count 하나 추가.
                        count++;

                    }

                }
            }
        }
    }
    //간선정보를 만들어주고.
    for(int i = 1 ; i< 7; i++)
    {
        for(int j= i ; j< 7; j++)
        {
            if(graph[i][j] < 100)
            {
                v.push_back(Edge(i,j,graph[i][j]));
            }
        }
    }

    //class operator <에 따라서 distance정렬
    sort(v.begin(), v.end());

    //모든정점이 자기 자신을 가리키게끔.
    int parent[7];
    for(int i = 1 ; i< 7 ;i++)
    {
        parent[i] = i;
    }

    //거리의 합 =0
    int sum = 0;
    for(int i = 0 ; i< v.size(); i++)
    {
        //사이클이 발생하지 않는경우 그래프에 포함.
        if(!findParent(parent, v[i].node[0], v[i].node[1]))
        {
            sum += v[i].distance;
            unionParent(parent, v[i].node[0], v[i].node[1]);
        }
        
    }
    
    //완전히 연결된 것인지 혹은 bridge가 없는 것인지 확인.
    for(int i = 2; i<numbering ; i++)
    {
        if(findParent(parent,1,i) == false){
            cout << -1;
            return 0;
        }
    }
    cout << sum;
    return 0;
}