#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>

const int INF = 100000000;
 std::vector<int> nodes;
std::vector<int> visits;
std::vector<std::vector<std::pair<int, int>>> matrix;

void deikstra(int start, int n){
    nodes[start] = 0;
    std::priority_queue <std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> queue;
    queue.push(std::make_pair(0, start));
    while (!queue.empty()){
        
        std::pair<int, int> pair = queue.top();
        int x = pair.second;
        queue.pop();
        for (int i = 0; i < matrix[x].size(); i++){
           
            int y = matrix[x][i].first;
            int w = matrix[x][i].second;
            if (nodes[x] + w < nodes[y]){
                nodes[y] = w + nodes[x];
                queue.push(std::make_pair(nodes[y], y));
            }
        }
    }
}
int main(){
    std::ifstream fin("pathbgep.in");
    std::ofstream fout("pathbgep.out");
    int n, m;
    fin >> n >> m;
    matrix.resize(n);
    nodes.resize(n, INF);
    visits.resize(n, 0);
   
    for(int i = 0; i < m; i++){
        int x, y, w;
        fin >> x >> y >> w;
        matrix[x - 1].push_back(std::make_pair(y - 1, w));
        matrix[y - 1].push_back(std::make_pair(x - 1, w));
    } 
    
    deikstra(0, n);
    for (int j = 0; j < n; j++){
        fout << nodes[j] << " ";
    }
    
    fin.close();
    fout.close();
    return 0;
}