#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
 
const long long INF = 5e18;
 
struct edge{
    long long x = 0;
    long long y = 0;
    long long weight = INF;
};
 
std::vector<long long> nodes;
std::vector<bool> visits;
std::vector<edge> edges;
std::vector<std::vector<long long>> matrix;
 
void DFS(long long start){
    visits[start] = true;
    for (long long i = 0; i < matrix[start].size(); i++){
        if (!(visits[matrix[start][i]])){
            DFS(matrix[start][i]);
        }
    }
}
void BF(long long start, long long n, long long m){
    nodes[start] = 0;
    for (long long i = 0; i < n; i++){
        for (long long j = 0; j < m; j++){
            if (nodes[edges[j].x] < INF){
                if (nodes[edges[j].y] > edges[j].weight + nodes[edges[j].x]){
                    nodes[edges[j].y] = std::max(-INF, nodes[edges[j].x] + edges[j].weight);
                }
            }
        }
    }
} 
 
int main(){
    std::ifstream fin("path.in");
    std::ofstream fout("path.out");
    long long n, m, s;
    fin >> n >> m >> s;
    nodes.resize(n, INF);
    visits.resize(n);   
    matrix.resize(n);
 
    for(long long i = 0; i < m; i++){
        long long x, y, w;
        fin >> x >> y >> w;
        edge my_edge;
        my_edge.x = x - 1;
        my_edge.y = y - 1;
        my_edge.weight = w;
        edges.push_back(my_edge);
        matrix[x - 1].push_back(y - 1);
    } 
     
    BF(s - 1, n, m);  
    for (long long i = 0; i < m; i++){
        if (!visits[edges[i].x] && nodes[edges[i].x] < INF && nodes[edges[i].y] > nodes[edges[i].x] + edges[i].weight){
            visits[edges[i].x] = true;
            DFS(edges[i].x);
        }
    }
    for (long long i = 0; i < n; i++){
        if (visits[i]){
            fout << "-\n";
        }else if(nodes[i] == INF){
            fout << "*\n";
        }else{
            fout << nodes[i] << '\n';
        }
    }
    fin.close();
    fout.close();
    return 0;
}