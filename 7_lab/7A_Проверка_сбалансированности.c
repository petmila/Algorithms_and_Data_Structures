#include <stdio.h>
int array[200000][3];
int balance[200000];
 
int height(int  i, int left, int  right, int  n, int i_left, int i_right)
{
    if (n == 0)
    {
        return 0;
    }
    if (array[i][1] != 0)
    {
        left = height(array[i][1] - 1, left, right, n, i_left, i_right);
    }
    else
    {
        left = 0;
    }
    if (array[i][2] != 0)
    {
        right = height(array[i][2] - 1, left, right, n, i_left, i_right);
 
    }
    else
    {
        right = 0;
    }
    if (right > left)
    {
        //printf("!%d!\n",right- left);
        balance[i] = right - left;
        return right + 1;
    }
    else
    {
        //printf("!%d!\n",right- left);
        balance[i] = right - left;
        return left + 1;
    }
}
int main()
{
    FILE *fin, *fout;
    fin = fopen("balance.in", "r");
    fout = fopen("balance.out", "w");
    int n;
    fscanf(fin, "%d", &n);
      
    int value;
    int left;
    int right;
    for (int i = 0; i < n; i++)
    {
        fscanf(fin, "%d %d %d", &value, &left, &right);
        array[i][0] = value;
        array[i][1] = left;
        array[i][2] = right;
    }
    int result = height(0,0,0,n, 1, 2);
    // if (result == 0)
    // {
    //     fprintf(fout, "%d\n", 0);
    // }
    for (int i = 0; i < n; i++)
    {
        fprintf(fout, "%d\n", balance[i]);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
