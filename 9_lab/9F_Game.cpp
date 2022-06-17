
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>

struct item
{
    int path = 0;
    int path_to_end = 100001;
    int name = 0;
    char status = 'n';
    char label = 'c'; // 'e' - end, 'c' - continue
    int who_wins = 0;
    std::vector<int> connections;

};
std::stack <int> stack;
std::vector<item> matrix;

void dfs(int a){
    matrix[a].status = 's'; //seen
    for(int i = 0; i < matrix[a].connections.size(); i++){
        if (matrix[matrix[a].connections[i]].status == 'n'){ //not_seen
            dfs(matrix[a].connections[i]);
        }
    }
    int min_path_to_end = 100001;
    int min_index = 0;
    if (matrix[a].label == 'e'){
        matrix[a].path_to_end = 0;
        if (matrix[a].path %2 == 0){
            matrix[a].who_wins = 2;
        }else{
            matrix[a].who_wins = 1;
        }
    }else if (stack.empty() == false){
        int path_to_end = matrix[stack.top()].path - matrix[a].path;
        if (path_to_end < matrix[a].path_to_end){
            matrix[a].path_to_end = path_to_end;
        }
        min_index = matrix[a].connections[0];
        for(int i = 0; i < matrix[a].connections.size(); i++){
            if (matrix[matrix[a].connections[i]].path_to_end < min_path_to_end){
                min_path_to_end = matrix[matrix[a].connections[i]].path_to_end;
                min_index = matrix[a].connections[i];
            }
        }
        matrix[a].who_wins = matrix[min_index].who_wins;
    }
    stack.push(matrix[a].name);

}
int main()
{
    std::ifstream fin("game.in");
    std::ofstream fout("game.out");

    int n, m, s;
    fin >> n >> m >> s;
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
    std::queue <int> queue;
    queue.push(s - 1);
    while (!queue.empty()){
        int index = queue.front();
        queue.pop();
        if (matrix[index].status == 's'){
                    break;
                }
        matrix[index].status = 's';
        if (matrix[index].connections.empty() == true){
            matrix[index].label = 'e';
        }
        for (int next_item = 0; next_item < matrix[index].connections.size(); next_item++){
            if (matrix[matrix[index].connections[next_item]].status == 's'){
                continue;
            }
            if (matrix[matrix[index].connections[next_item]].path > 0){
                continue;
            }
            matrix[matrix[index].connections[next_item]].path = matrix[index].path + 1;
            queue.push(matrix[index].connections[next_item]);
        }
    }
    for(int j = 0; j < n; j++){
        matrix[j].status = 'n';
    }
    dfs(s - 1);
    if (matrix[s - 1].who_wins == 1){
        fout << "First player wins";
    }else{
        fout << "Second player wins";
    }
    fin.close();
    fout.close();
    return 0;
}