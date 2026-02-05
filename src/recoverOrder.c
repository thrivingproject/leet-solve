/**
 * 3668
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>

int *recoverOrder(int *order, int orderSize, int *friends, int friendsSize,
                  int *returnSize) {
    int *arr = (int *)malloc(sizeof(int) * friendsSize);
    int i = 0;
    for (int j = 0; j < orderSize; j++) {
        for (int k = 0; k < friendsSize; k++) {
            if (friends[k] == order[j]) {
                arr[i++] = order[j];
            }
        }
    }
    *returnSize = i;
    return arr;
}

int main(void) {
    int order[] = {3, 1, 2, 5, 4};
    int friends[] = {1, 3, 4};
    int returnSize;
    int *result = recoverOrder(order, 5, friends, 3, &returnSize);

    printf("[");
    for (int i = 0; i < returnSize; i++) {
        printf("%d", result[i]);
        if (i < returnSize - 1)
            printf(", ");
    }
    printf("]\n");

    free(result);
    return 0;
}