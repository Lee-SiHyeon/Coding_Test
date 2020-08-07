#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
int N;
int arr[20][20];   //인구정보
int block[20][20]; //블록정보

int dx[4] = { -1, 0, 1, 0};
int dy[4] = { 0, 1, 0, -1};


void fill(int x,int y, int block_num)
{
    if(x <0 || y<0 || x>N-1 || y>N-1) return;
    if(block[x][y] !=0 ) return;

    block[x][y] = block_num;
    for(int i = 0; i<4; i++)
    {
        fill(x+dx[i], y+dy[i], block_num);
    }
}
int solve()
{
    int ret=2147000000;
    for(int x =0 ; x<N-2 ; ++x)// x가 움직일 수 있는범위
    { 
        for(int y =1; y<N-1 ; ++y )// y가 움직일 수 있는 범위
        { 
            for(int d1=1 ; x+d1 <N-1 && y-d1 >=0 ;++d1)// d1이 늘어날 수 있는 범위
            { 
                for(int d2=1; x+d1+d2 <N-1 && y+d2 <N; ++d2 )// d2가 늘어날 수 있는 범위
                { 
                    memset(block, 0, sizeof(block));
         
                    for(int i = 0; i<= d1 ; ++i)
                    {
                        block[x+i][y-i] = 5;
                        block[x+d2+i][y+d2-i] = 5;
                    }
                    for(int i = 0; i<=d2 ; ++i)
                    {
                        block[x+i][y+i]=5;
                        block[x+d1+i][y-d1+i] =5;
                    }

                    for(int r = x-1; r >=0 ; --r)
                    {
                        block[r][y] = 1;
                    }
                    for(int r = x+d1+d2+1; r<N; ++r)
                    {
                        block[r][y-d1+d2] =4;
                    }
                    for(int c = y+d2+1; c <N ; ++c)
                    {
                        block[x+d2][c] = 2;
                    }
                    for(int c = y-d1-1; c>=0 ; --c )
                    {
                        block[x+d1][c] =3;
                    }

                    fill(0,0,1);
                    fill(0,N-1,2);
                    fill(N-1,0,3);
                    fill(N-1,N-1,4);
                    int SumArr[6] = {0};
                    for(int i = 0 ; i<N; ++i)
                    {
                        for(int j= 0 ; j< N; ++j)
                        {
                            SumArr[block[i][j]] += arr[i][j];
                        }
                    }

                    SumArr[5] += SumArr[0];

                    //구역별 최대 최소 찾기
                    int SumMin= 2147000000, SumMax = 0;
                    for(int i = 1 ; i<6; ++i)
                    {
                        if(SumArr[i] < SumMin) SumMin = SumArr[i];
                        if(SumArr[i] > SumMax) SumMax = SumArr[i];
                    }
                    int minusMin = SumMax -SumMin;
                    if(minusMin < ret) 
                    {
                        ret = minusMin;
                    }

                }
            }
        }
    }
    return ret;
}

int main()
{
    cin >> N;
    for(int x = 0 ; x<N; ++x){
        for(int y = 0 ; y<N; ++y)
        {
            cin >> arr[x][y];
        }
    }

    cout << solve()<< endl;
}