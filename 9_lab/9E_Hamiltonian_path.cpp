#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
 
int state = 0;
std::stack <int> stack;
 
 
struct item{
    int name = 0;
    char status = 'n';
    std::vector<int> connections;
};
 
std::vector<item> matrix;
 
void dfs(int a){
     
    matrix[a].status = 's'; //seen
    for(int i = 0; i < matrix[a].connections.size(); i++){
        if (matrix[matrix[a].connections[i]].status == 'n'){ //not_seen
            dfs(matrix[a].connections[i]);
        }
    }
    matrix[a].status = 'c'; // circle
    if (state != -1){
        if (stack.empty() == true){
            state = 1;
        }
        for (int i = 0; i < matrix[a].connections.size();i++){
            if ((stack.empty() == false)&&(matrix[a].connections[i] == stack.top())){
                state = 1;
            }
        }
        if (state == 1){
            stack.push(matrix[a].name);
            state = 0;
        }else{
            state = -1;    
            return;
        }
    }
    
}
int main(){
    std::ifstream fin("hamiltonian.in");
    std::ofstream fout("hamiltonian.out");
 
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
    }
    for(int r = 0; r < n; r++){
        if (state == -1){
            break;
        }
        if (matrix[r].status == 'n'){
            dfs(r);
        }
        if (state == -1){
            break;
        }
    }
    if (state != -1){
        fout << "YES"; 
    }else{
        fout << "NO";
    }
 
    fin.close();
    fout.close();
    return 0;
}