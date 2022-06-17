#include <iostream>
#include <fstream>
#include <vector>
#include <stack>

int state = 0;
std::stack <int> stack;
std::stack <int> stack_circle;
int circle_end = -1;

struct item{
    int name = 0;
    char status = 'n';
    std::vector<int> connections;
};

std::vector<item> matrix;

void dfs(int a){
    matrix[a].status = 's'; //seen
    stack.push(matrix[a].name);
    for(int i = 0; i < matrix[a].connections.size(); i++){
        if ((matrix[matrix[a].connections[i]].status == 's')&&(stack_circle.empty() == true)){
            state = -1;
            circle_end = matrix[matrix[a].connections[i]].name;
            while(stack.top() != circle_end){
                stack_circle.push(stack.top());
                stack.pop();
            }
            stack_circle.push(stack.top());
            return;
        }
        if (matrix[matrix[a].connections[i]].status == 'n'){ //not_seen
            dfs(matrix[a].connections[i]);
        }
    }
    if(stack.empty() == false){
        stack.pop();
    }
    
    matrix[a].status = 'c'; // circle   
}
int main(){
    std::ifstream fin("cycle.in");
    std::ofstream fout("cycle.out");

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
    int size = stack_circle.size();
    if ((state == -2)||(state == -1)){
        fout << "YES\n";
        for(int i = 0; i < size; i++){
            fout << stack_circle.top() + 1 << ' ';
            stack_circle.pop();
        }
    }else if (state == 0){
        fout << "NO";
    }

    fin.close();
    fout.close();
    return 0;
}
