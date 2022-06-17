#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

const long long INF = 100000000001;

int main(){
    std::ifstream fin("pathmgep.in");
    std::ofstream fout("pathmgep.out");
    long long n, start, finish;
    fin >> n >> start >> finish;
    std::vector<long long> nodes;
    std::vector<long long> visits;
    std::vector<std::vector<long long>> matrix;
    matrix.resize(n, std::vector<long long>(n, INF));
    nodes.resize(n, INF);
    visits.resize(n, 0);
    for(long long i = 0; i < n; i++){
        for (long long j = 0; j < n; j++){
            fin >> matrix[i][j];
            if (matrix[i][j] < 0){
                matrix[i][j] = INF;
            }
        }
    }   
    nodes[start - 1] = 0;
    for (long long i = 0; i < n; i++){
        long long v = -1;
        for (long long j = 0; j < n; j++)
		    if (!visits[j] && (v == -1 || nodes[j] < nodes[v]))
			    v = j;
        if (nodes[v] == INF)
            break;
	    visits[v] = 1;
	    for (long long j = 0; j < n; j++)
            nodes[j] = std::min(nodes[j], nodes[v] + matrix[v][j]);
    } 
    if (nodes[finish - 1] >= INF){
        fout << -1;
    }else{
        fout << nodes[finish - 1];
    }
    fin.close();
    fout.close();
    return 0;
}