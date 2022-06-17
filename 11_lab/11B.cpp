#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

const long long INF = 1000000;
 std::vector<long long> nodes;
std::vector<long long> visits;
std::vector<std::vector<long long>> matrix;

void deikstra(long long start, long long n){
    nodes.assign (n, INF);
    visits.assign (n, 0);
    nodes[start] = 0;
    for (long long i = 0; i < n; i++){
        long long v = -1;
        
        for (long long j = 0; j < n; j++)
		    if (!visits[j] && (v == -1 || nodes[j] < nodes[v]))
			    v = j;
        
        if (nodes[v] == INF)
            break;
	    visits[v] = 1;
        
	    for (long long j = 0; j < n; j++){
            if (nodes[j] > nodes[v] + matrix[v][j]){
                nodes[j] = nodes[v] + matrix[v][j];
            }
           
        }
    } 
}
int main(){
    std::ifstream fin("pathsg.in");
    std::ofstream fout("pathsg.out");
    long long n, m;
    fin >> n >> m;
    matrix.resize(n, std::vector<long long>(n, INF));
    nodes.resize(n, INF);
    visits.resize(n, 0);
   
    for(long long i = 0; i < m; i++){
        int x, y, w;
        fin >> x >> y >> w;
        matrix[x - 1][y - 1] = w;
    } 
    
    for (long long i = 0; i < n; i++){
        deikstra(i, n);
        for (int j = 0; j < n; j++){
            fout << nodes[j] << " ";
        }
        fout << "\n";
        

    }
    
    fin.close();
    fout.close();
    return 0;
}