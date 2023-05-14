#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "merge_sort.h"
#include "selection_sort.h"

#define SIZE 10000
#define MAX 10000

void generateRandomArray(int arr[])
{

    for (int i = 0; i < SIZE; ++i)
    {
        arr[i] = rand() % MAX;
    }
}

void printArray(int arr[])
{
    for (int i = 0; i < 3; ++i)
    {
        printf("%d ", arr[i]);
    }
    printf("... ");
    for (int i = SIZE - 4; i < SIZE; ++i)
    {
        printf("%d ", arr[i]);
    }
    puts("");
}

int main(void)
{

    srand(time(NULL));
    puts("");
    puts("Starting comparison:\n");
    puts("\tGiven values are:");
    printf("\t%d items in an array from 0 to %d.\n", SIZE, MAX);
    puts("");

    {
        puts("MERGE SORT routine:\n");
        int *arr = (int *)malloc(SIZE * sizeof(int));
        generateRandomArray(arr);
        printf("\tExisting array is: ");
        printArray(arr);
        puts("");
        clock_t t;
        t = clock();
        mergeSort(arr, 0, SIZE - 1);
        t = clock() - t;
        double elapsed = ((double)t) / CLOCKS_PER_SEC;
        printf("\tIt took %f secs for the MERGE SORT algorithm to execute.\n", elapsed);
        puts("");
        printf("\tSorted array is: ");
        printArray(arr);
        puts("");
    }

    {
        puts("SELECTION SORT routine:\n");
        int *arr = (int *)malloc(SIZE * sizeof(int));
        generateRandomArray(arr);
        printf("\tExisting array is: ");
        printArray(arr);
        puts("");
        clock_t t;
        t = clock();
        selectionSort(arr, SIZE);
        t = clock() - t;
        double elapsed = ((double)t) / CLOCKS_PER_SEC;
        printf("\tIt took %f secs for the SELECTION SORT algorithm to execute.\n", elapsed);
        puts("");
        printf("\tSorted array is: ");
        printArray(arr);
        puts("");
    }
    return 0;
}