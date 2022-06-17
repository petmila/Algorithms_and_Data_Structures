#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <bits/stdc++.h>

const int INF = 1000000000;

double weight(int x_1, int y_1, int x_2, int y_2){
    return pow(pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2), 0.5);
}

int main(){
    std::ifstream fin("spantree.in");
    std::ofstream fout("spantree.out");
    int n;
    fin >> n;
    std::vector<double> nodes;
    std::vector<int> visits;
    std::vector<std::pair<int, int>> list_nodes;
    double **matrix;
    matrix = new double*[n];
    for( int i = 0; i < n; i++){
        matrix[i] = new double [n];
    }
    nodes.resize(n, INF);
    visits.resize(n, 0);
    int x, y;
    for(int i = 0; i < n; i++){
        fin >> x >> y;
        list_nodes.push_back(std::make_pair(x, y));
    }
    for(int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
           
            matrix[i][j] = weight(list_nodes[i].first, list_nodes[i].second, list_nodes[j].first, list_nodes[j].second);
            matrix[j][i] = weight(list_nodes[i].first, list_nodes[i].second, list_nodes[j].first, list_nodes[j].second);
            
        }
    }   
    double summ = 0;
    nodes[0] = 0;
    for (int i = 0; i < n; i++){
	    int v = -1;
	    for (int j = 0; j < n; j++)
		    if (!visits[j] && (v == -1 || nodes[j] < nodes[v]))
			    v = j;
	    visits[v] = 1;
	    for (int j = 0; j < n; j++)
            if (!visits[j] && matrix[v][j] < nodes[j] && v != j)
				nodes[j] = matrix[v][j];
    }
    for (int i = 0; i < n; i++){
        summ += nodes[i];
    }
    fout << std::setprecision(15) << summ;
    fin.close();
    fout.close();
    return 0;
}