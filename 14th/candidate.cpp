#include <iostream>
#include <vector>
#include <fstream>
#include <string>

#include <map>

using namespace std;

bool check[21];
bool visit[8];
vector<int> vi;
vector<vector<int>> vvi;
vector<vector<string>> vec;
int result= 0;

bool check(int R){//vi에 어느column을 참조할지 정해졌음.
    for(int i = 0 ; i<vi.size(); i++)
    {
        int col = vi[i];
        map<int,string> m;
        for(int j= 0; j< R ; j++)
        {
            
        }
    }

}
void dfs(int end, int d)
{

    if(d >=end)
    {

        vvi.push_back(vi);

        return;
    }
    if( check()){
        result++;
        return;
    }
    //포함하지 않는경우
    dfs(end, d+1);

    //포함하는 경우.
    
    vi.push_back(d);
    dfs(end,d+1);
    vi.pop_back();

}
void solution(vector<vector<string>> relation){
    int R = relation.size();
    int C = relation[0].size();
    int numbering=0;
    dfs(C-1,0);


}

int main(void)
{
    vec = {{"100","ryan","music","2"},{"200","apeach","math","2"},{"300","tube","computer","3"},{"400","con","computer","4"},{"500","muzi","music","3"},{"600","apeach","music","2"}};
    solution(vec);
}

