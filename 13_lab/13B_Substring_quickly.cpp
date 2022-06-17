#include <fstream>
#include <iostream>
#include <vector>
#include <string.h>

std::vector<int> prefix(std::string p){
    std::vector<int> answer(p.size());
    for (int i = 1; i < answer.size(); ++i)
    {
        int k = answer[i - 1];
        while (k > 0 && p[i] != p[k])
            k = answer[k - 1];
        if (p[i] == p[k])
            ++k;
        answer[i] = k;
    }
    return answer;
}

int main()
{
    std::ifstream fin("search2.in");
    std::ofstream fout("search2.out");
    std::string p, t;
    fin >> p >> t;
    std::vector<int> answer = prefix(p + '#' + t);
    std::vector<int> result;

    for (int i = 0; i < t.size(); i++){
        if (answer[p.size() + i + 1] == p.size()){
            result.push_back(i - p.size() + 2);
        }
    }
    fout << result.size() << "\n";
    for (int i = 0; i < result.size(); ++i)
        fout << result[i] << ' ';
    return 0;
}