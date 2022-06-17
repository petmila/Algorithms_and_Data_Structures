#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>
 
struct edge {
    long long x, y, weight;
};
 
const long long INF = 1e9 + 1;
long long n;
long long n_cycle = -1;
std::vector<edge> edges;
std::vector<long long> nodes;
std::vector<long long> previous;
 
void BF(long long start){
    nodes[start] = 0;
    n_cycle = -1;
    for (long long i = 0; i < n; i++) {
        for (edge edge : edges) {
            if (edge.weight != 1e9 && nodes[edge.y] > nodes[edge.x] + edge.weight) {
                nodes[edge.y] = std::max(-INF, nodes[edge.x] + edge.weight);
                n_cycle = edge.y;
                previous[n_cycle] = edge.x;
            }
        }
    }
}
 
int main(){
    std::ifstream fin("negcycle.in");
    std::ofstream fout("negcycle.out");
    fin >> n;
    nodes.resize(n, INF);
    previous.resize(n);
    for (long long i = 0; i < n; i++){
        for (long long j = 0; j < n; j++){
            long long weight;
            fin >> weight;
            edge my_edge;
            my_edge.x = i;
            my_edge.y = j;
            my_edge.weight = weight;
            if (weight != 1e9){
                edges.push_back(my_edge);
            }
        }
    }
    BF(0);
    for (edge edge : edges) {
        if (edge.weight != 1e9 && nodes[edge.y] > nodes[edge.x] + edge.weight) {
            std::vector<long long> way;
            n_cycle = edge.y;
            long long n_cycle_f = n_cycle;
            for (long long i = 0; i < n; i++){
                n_cycle_f = previous[n_cycle_f];
            }
            for (long long n_cycle_n = n_cycle_f; n_cycle_n != n_cycle_f || way.empty(); n_cycle_n = previous[n_cycle_n]){
                way.push_back(n_cycle_n);
            }
            way.push_back(n_cycle_f);
            fout << "YES\n";
            fout << way.size() << "\n";
            for (long long i = way.size(); i > 0; i--){
                fout << way[i - 1] + 1 << ' ';
            }
            return 0;
        }

    }
    fout << "NO";
    return 0;
}