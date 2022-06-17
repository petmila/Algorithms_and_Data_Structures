#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
 
int state = 0;
int time = 0;
std::stack <int> stack;
 
 
struct item{
    int name = 0;
    int time = 0;
    char status = 'n';
    std::vector<int> connections;
};
 
std::vector<item> matrix;
 
void dfs(int a){
     
    time ++;
    matrix[a].status = 's'; //seen
    for(int i = 0; i < matrix[a].connections.size(); i++){
        if (matrix[matrix[a].connections[i]].status == 's'){
            state = -1;
        }
        if (matrix[matrix[a].connections[i]].status == 'n'){ //not_seen
            dfs(matrix[a].connections[i]);
        }
    }
    time++;
    matrix[a].status = time;
    matrix[a].status = 'c'; // circle
    stack.push(matrix[a].name);
    
}
int main(){
    std::ifstream fin("topsort.in");
    std::ofstream fout("topsort.out");
 
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
        if (matrix[r].status == 'n'){
            dfs(r);
        }
    }
    if (state == 0){
        for(int i = 0; i < n; i++){
            fout << stack.top() + 1 << ' ';
            stack.pop();
        }
    }else{
        fout << state << ' ';
    }
 
    fin.close();
    fout.close();
    return 0;
}