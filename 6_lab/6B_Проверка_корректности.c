#include <stdio.h>
int array[200000][5];
char result = 'Y';
int height(int  i, int n)
{
    int null;
    if (n == 0)
    {
        return 0;
    }
    if (array[i][1] != 0)
    {
        int key = array[i][1] - 1;
        array[key][4] = array[i][0];
        if (array[i][3] > array[key][3])
        {
            array[key][3] = array[i][3];
        }
        if (array[key][3] < array[key][0] && array[key][0] < array[key][4])
        {
            null = 0;
            //printf("%d %d %d\n", array[key][0], array[key][3], array[key][4]);
        }
        else
        {
            result = 'N';
        }
        null = height(key, n);
    }
    if (array[i][2] != 0)
    {
        int key = array[i][2] - 1;
        array[key][3] = array[i][0];
        if (array[i][4] < array[key][4])
        {
            array[key][4] = array[i][4];
        }
        if (array[key][3] < array[key][0] && array[key][0] < array[key][4])
        {
            null = 0;
            //printf("%d %d %d\n", array[key][0], array[key][3], array[key][4]);
        }
        else
        {
            result = 'N';
        }
        null = height(key, n);
    }
    return 0;
}
int main()
{
    FILE *fin, *fout;
    fin = fopen("check.in", "r");
    fout = fopen("check.out", "w");
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
        array[i][3] = -1000000001;
        array[i][4] = 1000000001;
    }
    int null;
    null = height(0, n);
    if (result == 'Y')
    {
        fprintf(fout, "%s", "YES");
    }
    if (result == 'N')
    {
        fprintf(fout, "%s", "NO");
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
