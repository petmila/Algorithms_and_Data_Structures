
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

struct item
{
    int path = 0;
    int name = 0;
    int component = 0;
    char status = 'n';
    std::vector<int> connections;
};

int main()
{
    std::ifstream fin("components.in");
    std::ofstream fout("components.out");

    int n, m;
    fin >> n >> m;
    struct item *matrix = new struct item[n];
    int *array = new int[n];
    
    for( int i = 0; i < n; i++)
    {
        matrix[i].name = i;
        array[i] = i;
    }
    int start, end;
    for (int i = 0; i < m; i++)
    {
        fin >> start >> end;
        matrix[start - 1].connections.push_back(end - 1);
        matrix[end - 1].connections.push_back(start - 1);
    }
    
    std::queue <int> queue;
    int k = 1;
    for(int r = 0; r < n; r++)
    {
        if (matrix[r].component == 0)
        {
            queue.push(array[r]);
            while (!queue.empty())
            {
                int index = queue.front();
                queue.pop();
                if (matrix[index].status == 's')
                {
                    break;
                }
                matrix[index].status = 's';
                matrix[index].component = k;
                for (int next_item = 0; next_item < matrix[index].connections.size(); next_item++)
                {
                    if (matrix[matrix[index].connections[next_item]].status == 's')
                    {
                        continue;
                    }
                    if (matrix[matrix[index].connections[next_item]].path > 0)
                    {
                        continue;
                    }
                    matrix[matrix[index].connections[next_item]].path = matrix[index].path + 1;
                    queue.push(matrix[index].connections[next_item]);
                }
            }
            k++;
        }
    }
    fout << k - 1 << '\n';
    for(int i = 0; i < n; i++)
    {
        fout << matrix[i].component << ' ';
    }
    fin.close();
    fout.close();
    return 0;
}