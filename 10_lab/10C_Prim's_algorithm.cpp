#include <iostream>
#include <cmath>
#include <fstream>
#include <set>
#include <bits/stdc++.h>
 
int main(){
    std::ifstream fin("spantree3.in");
    std::ofstream fout("spantree3.out");
    int n, m;
    fin >> n >> m;
    std::vector<int> nodes;
    std::vector<std::pair<int, int>> matrix[n];
    nodes.resize(n, 0);
    int x, y, w;
    for(int i = 0; i < m; i++){
        fin >> x >> y >> w;
        matrix[x - 1].push_back(std::make_pair(y - 1, w));
        matrix[y - 1].push_back(std::make_pair(x - 1, w));
    }
    std::priority_queue <std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> queue;
    queue.push(std::make_pair(0,0));
    long long summ = 0;
    while (!queue.empty()){
        std::pair<int, int> pair = queue.top();
        queue.pop();
        if (nodes[pair.second]){
            continue;
        }
        nodes[pair.second] = 1;
        summ += pair.first;
        for (int i = 0; i < matrix[pair.second].size(); i++){
            if (!nodes[matrix[pair.second][i].first]){
                queue.push(std::make_pair(matrix[pair.second][i].second, matrix[pair.second][i].first));
            }
        }
    }
    fout << summ;
    fin.close();
    fout.close();
    return 0;
}