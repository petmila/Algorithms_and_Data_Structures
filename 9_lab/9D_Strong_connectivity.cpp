#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
 
int component = 1;
std::stack <int> stack;
 
struct item{
    int name = 0;
    int component = 0;
    char status = 'n';
    std::vector<int> connections;
};
 
std::vector<item> matrix;
std::vector<item> matrix_invert;
 
void dfs_invert(int a){
    matrix_invert[a].status = 's'; //seen
    for(int i = 0; i < matrix_invert[a].connections.size(); i++){
        if (matrix_invert[matrix_invert[a].connections[i]].status == 'n'){ //not_seen
            dfs_invert(matrix_invert[a].connections[i]);
        }
    }
    stack.push(matrix_invert[a].name);
    
}
void dfs(int a){
    matrix[a].component = component; // in component
    for(int i = 0; i < matrix[a].connections.size(); i++){
        if (matrix[matrix[a].connections[i]].component == 0){ //not in component
            dfs(matrix[a].connections[i]);
        }
    }
    
}
int main(){
    std::ifstream fin("cond.in");
    std::ofstream fout("cond.out");
 
    int n, m;
    fin >> n >> m;
     
    for( int i = 0; i < n; i++){
        item my_item;
        matrix.push_back(my_item);
        matrix[i].name = i;
        item my_item_invert;
        matrix_invert.push_back(my_item_invert);
        matrix_invert[i].name = i;
    }
     
    int start, end;
    for (int i = 0; i < m; i++){
        fin >> start >> end;
        matrix_invert[start - 1].connections.push_back(end - 1); // поменяла invert и стандартный местами
        matrix[end - 1].connections.push_back(start - 1);
    }
    for(int r = 0; r < n; r++){
        if (matrix_invert[r].status == 'n'){
            dfs_invert(r);
        }
    }
    
    for(int r = 0; r < n; r++){
        if (matrix[stack.top()].component == 0){
            dfs(stack.top());
            component++;
        }
        
        stack.pop();
    }
    
    fout << component - 1 << '\n';
    for(int r = 0; r < n; r++){
        fout << matrix[r].component << ' ';
    }      
        

    fin.close();
    fout.close();
    return 0;
}