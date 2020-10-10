#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
int solution(int n, vector<int> weak, vector<int> dist) {
 
    int answer = -1;
 
    //next_permutation을 사용하기 위한 정렬
    sort(dist.begin(), dist.end());
    


    //원형탐색 weak.size()만큼 반복
    for (int i = 0; i < weak.size(); i++) {
 
        //취약지점 순환
        int tmp = weak[0] + n;
        for (int j = 1; j < weak.size(); j++) {
            weak[j - 1] = weak[j];
        }
        weak[weak.size() - 1] = tmp;
        
        while(1)
        {
            for(int a = 0 ; a<dist.size() ; a++)
            {
                cout << dist[a] << " ";
            }
            cout << endl;
            if(next_permutation(dist.begin(), dist.end())) break;
        }
        //친구들 배치
        do {
            for(int a = 0 ; a < dist.size(); a++)
            {
                cout << dist[a] << " ";
            }
            cout << endl;
            
            //w : 취약지점 index, d : 친구들 index
            int w = 0;
            int d = 0;
 
            //친구 한명이 갈 수 있는 취약지점 까지 모두 탐색
            for (d = 0; d < dist.size(); d++) {
                int fin = weak[w] + dist[d];
                //cout << "weak[w] = " << weak[w] << ", dist[d] = "<< dist[d]<<endl;
                while (fin >= weak[w]) {
                    w++;
                    if (w == weak.size()) {
                        break;
                    }
                }
                if (w == weak.size()) {
                    break;
                }
            }
 
            //모든 취약지점이 탐색 되었다면, 가장 적게 친구를 사용한 결과 저장
            if (w == weak.size()) {
                if (answer == -1 || d + 1 < answer) {
                    answer = d + 1;
                    //cout << "answer= " << answer << endl;
                }
            }
            
        } while (next_permutation(dist.begin(), dist.end()));
        cout << endl;
    }
    return answer;
}

int main()
{
    int n = 12;
    vector<int> weak = {1,5,6,10};
    vector<int> dist = {1,2,3,4};

    solution(n, weak, dist);
}