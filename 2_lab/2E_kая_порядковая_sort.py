#include <stdio.h>
#include <stdlib.h>
 
void quicksort(int start, int end, int *array, int k)
{
    if (start < end)
    {
        int pivot = array[start+rand()%(end - start)];
        int i = start;
        int j = end;
        while (i <= j)
        {
            while (array[i] < pivot)
                ++i;
            while (pivot < array[j])
                --j;
            if (i <= j)
            {
                int swap;
                swap = array[i];
                array[i] = array[j];
                array[j] = swap;
                ++i;
                --j;
            }
        }
 
        if ((start < j) && (k <= j))
        {
            quicksort(start, j, array, k);
        }
        if ((i < end) && (k >= i))
        {
            quicksort(i, end, array, k);
        }
        if ((start < j) && (end > i) && (j < k < i))
        {
            quicksort(j, i, array, k);
        }
    }
}
int main()
{
    int n, k;
    int A, B, C;
    FILE *fin, *fout;
    fin = fopen("kth.in", "r");
    fout = fopen("kth.out", "w");
    fscanf(fin, "%d%d", &n, &k);
    int array[n];
    if (n == 1)
    {
        fscanf(fin, "%d%d%d%d", &A, &B, &C, &array[0]);
    }
    else
    {
        fscanf(fin, "%d%d%d%d%d", &A, &B, &C, &array[0], &array[1]);
    }
    for (int i = 2; i < n; i++)
        array[i] = A * array[i - 2] + B * array[i - 1] + C;
    quicksort(0, n - 1, array, k - 1);
 
    //for (int i = 0; i < n; i++)
    //    printf(" %d ", array[i]);
 
    fprintf(fout, "%d", array[k - 1]);
    fclose(fin);
    fclose(fout);
    return 0;
}
