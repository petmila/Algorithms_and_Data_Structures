#include <iostream>
#include <vector>
#include <string.h>

int main(){
    std::string p;
    int alphabet;
    std::cin >> alphabet;
    std::cin >> p;
    int n = p.size();
    std::vector<int> answer(p.size() + 1);
    int j = 0, i = 1;
    while (i < p.size())
    {
        if (p[i] == p[j]){
            answer[i + 1] = j + 1;
            i++;
            j++;
        }else{
            if (j > 0){
                j = answer[j];
            }else{
                answer[i + 1] = 0;
                i++;
            }
        }
    }
    std::vector <std::vector<int>> aut(n + 1, std::vector<int> (alphabet));
    for (int i = 0; i < n + 1; ++i){
        for (int c = 0; c < alphabet; ++c){
            if (i > 0 && c + 'a' != p[i]){
                aut[i][c] = aut[answer[i]][c];
            }else{
                aut[i][c] = i + (c + 'a' == p[i]);
            }
        }
    }

    for (int i = 0; i < p.size() + 1; ++i)
    {
        for (int j = 0; j < alphabet; j++)
            std::cout << aut[i][j] << ' ';
        std::cout << std::endl;
    }

    return 0;			
}