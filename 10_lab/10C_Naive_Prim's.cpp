#include <iostream>
#include <cmath>
#include <fstream>
#include <set>
#include <bits/stdc++.h>

struct item{
    int name = 0;
    int status = 0;
};
struct edge{
    int weight = -1;
    item* x;
    item* y;
    bool operator<(const edge& b) const{
        return (weight <= b.weight);
    }
    
};
std::set<edge> edges;
std::vector<item> matrix;
int main(){
    std::ifstream fin("spantree3.in");
    std::ofstream fout("spantree3.out");
    int n, m;
    fin >> n >> m;
    int x, y, w;
    for (int i = 0; i < n; i++){
        item my_item;
        my_item.name = i;
        my_item.status = 0;
        matrix.push_back(my_item);
    }
    for( int i = 0; i < m; i++){
        fin >> x >> y >> w;
        edge my_edge;
        my_edge.x = &matrix[x - 1];
        my_edge.y = &matrix[y - 1];
        my_edge.weight = w;
        edges.insert(my_edge);
        
    }
    if (edges.size() == 0){
        fout << 0;
        return 0;
    }
    //std::sort(edges.begin(), edges.end(), compare);
    std::set <edge> :: iterator it = edges.begin();
    
    (*it).x->status = 1;
    (*it).y->status = 1;
    long long summ = (*it).weight;
    edges.erase(edges.begin());
    int len = 1;
    
    while ((len < n - 1)&&(edges.size() > 0)){
        for (std::set <edge> :: iterator i = edges.begin(); i != edges.end()++; i++){
            if ( (*i).y->status +(*i).x->status == 1){
                summ += (*i).weight;
                (*i).x->status = 1;
                (*i).y->status = 1;
                edges.erase(i);
                break;
            }
        }
        len++;
    }
    fout << summ;
    fin.close();
    fout.close();
    return 0;
}