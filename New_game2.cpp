#include <iostream>
#include <vector>

using namespace std;



struct robot{
    int x;
    int y; 
    int dir;
};
int dx[5] = {0, 0, 0, -1, 1};
int dy[5] = {0, 1, -1, 0, 0};
int N,K;
int arr[12][12] = {0};
vector<int> stack_arr[12][12];
vector<robot> rb_arr;





int solve(){
    for(int iter = 0 ; iter<1000; iter++)
    {
        for(int i = 0; i<K; i++)//첫 로봇부터 하나씩 가져옴
        {
            
            int x = rb_arr[i].x;
            int y=  rb_arr[i].y;
            int dir = rb_arr[i].dir;

            //이동할 위치 정하고.
            int xx = x + dx[dir];
            int yy = y + dy[dir];

            if(xx <0 || xx > N || yy <0 || yy >N) //벽에 부딪히면.
            {
                //dir반대로 해줌. 한칸 전진시킴. ( 전진시킬 칸 확인해줘야함.)
                if(dir ==1) dir = 2;
                else if( dir ==2) dir =1;
                else if( dir ==3) dir =4;
                else if(dir ==4) dir =3;
                //방향 바꾸고 가야할 곳.
                xx = x+dx[dir];
                yy = y+dy[dir];
            }

            // x,y 는 기존의 위치, xx,yy는 가야하는 위치.
            int idx = 0;
            for(idx = 0; idx < stack_arr[x][y].size(); idx++) // i번 로봇이 기존의 위치(stack_arr)에서 몇번쨰에 위치하는지 알아야함.
            {
                if(stack_arr[x][y][idx] == i) break; // 로봇번호랑 같아지면 break;
            }
            idx --; // idx ++되서 브레이크 되나 ?
            if ( arr[xx][yy] ==0) //가려는 곳이 흰색이면. 그냥 이동하면 됨... 이 아니라 위에 쌓인것들 ... 같이 움직여야되네
            { 

                for(int j = idx; j < stack_arr[x][y].size() ; j++) // 
                {
                    int rb_num=stack_arr[x][y][j]; //그자리에 있는 로봇들의 로봇 번호.
                    rb_arr[rb_num].x = xx;
                    rb_arr[rb_num].y = yy; //위치 옮겨줌.
                    stack_arr[x][y].pop_back(); //이동했으니 뺴주고.
                    stack_arr[xx][yy].push_back(rb_num); //이동할 위치에 다시 푸쉬.
                }
            }
            else if(arr[xx][yy] ==1) //가려는 곳이 빨간색이면
            {

            }
            else {
                
            }//가려는 곳이 파란색이면.

            //말이 4개가 쌓였는지 체크하고 return i+1;
        }
    }
    return -1;// 1000번 반복했는데 안되면 return -1;
}
int main(void)
{
    cin >> N >> K;

    for(int i = 0 ; i < N; i++)
    {
        for(int j= 0 ; j< N; j++)
        {
            cin >> arr[i][j];
        }
    }
    for(int i = 0 ; i < K; i++)
    {
        robot temp;
        int x,y;
        cin >> x >> y >> temp.dir;
        temp.x = x-1;
        temp.y = y-1;
        stack_arr[temp.x][temp.y].push_back(i);
        rb_arr.push_back(temp);
    }

    cout << solve();

}