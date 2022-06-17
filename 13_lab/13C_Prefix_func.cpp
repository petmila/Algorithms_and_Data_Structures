#include <fstream>
#include <vector>
#include <string.h>

int main()
{
    std::ifstream fin("prefix.in");
    std::ofstream fout("prefix.out");
    std::string p;
    fin >> p;
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

    for (int i = 0; i < answer.size(); ++i)
        fout << answer[i] << ' ';
    return 0;
}