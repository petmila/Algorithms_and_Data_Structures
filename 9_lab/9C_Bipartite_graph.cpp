#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
 
int state = 0;
int label = 1;
 
 
struct item{
    int name = 0;
    int label = 0;
    char status = 'n';
    std::vector<int> connections;
};
 
std::vector<item> matrix;
 
void dfs(int a, int label){
     
    //matrix[a].status = 's'; //seen
    if (label == 1){
        matrix[a].label = 2;
    }else{
        matrix[a].label = 1;
    }
    
    for(int i = 0; i < matrix[a].connections.size(); i++){
        // if (matrix[matrix[a].connections[i]].status == 's'){
        //     state = -1;
        // }
        if (matrix[matrix[a].connections[i]].label == 0){ //not_seen
            dfs(matrix[a].connections[i], matrix[a].label);
        }else if (matrix[matrix[a].connections[i]].label == matrix[a].label){
            state = -1;
            return;
        }
    }
    //matrix[a].status = 'c'; // circle
    
}
int main(){
    std::ifstream fin("bipartite.in");
    std::ofstream fout("bipartite.out");
 
    int n, m;
    fin >> n >> m;
     
    for( int i = 0; i < n; i++){
        item my_item;
        matrix.push_back(my_item);
        matrix[i].name = i;
    }
     
    int start, end;
    for (int i = 0; i < m; i++){
        fin >> start >> end;
        matrix[start - 1].connections.push_back(end - 1); 
        matrix[end - 1].connections.push_back(start - 1);
    }
    for(int r = 0; r < n; r++){
        if (matrix[r].label == 0){
            dfs(r, 1);
        }
    }
    if (state == 0){
        fout << "YES";
    }else{
        fout << "NO";
    }
 
    fin.close();
    fout.close();
    return 0;
}