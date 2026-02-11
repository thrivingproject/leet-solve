#include <stdlib.h>

int **flipAndInvertImage(int **image, int imageSize, int *imageColSize,
                         int *returnSize, int **returnColumnSizes) {
    *returnSize = imageSize;
    *returnColumnSizes = (int *)malloc(imageSize * sizeof(int));
    int columns = *imageColSize;
    int **new_image = (int **)malloc(imageSize * sizeof(int *));
    for (int i = 0; i < imageSize; i++) {
        (*returnColumnSizes)[i] = columns;
        new_image[i] = (int *)malloc(columns * sizeof(int));
        int l = 0, r = columns - 1;
        while (l <= r) {
            new_image[i][l] = image[i][r] ^ 1;
            new_image[i][r] = image[i][l] ^ 1;
            l++;
            r--;
        }
    }
    return new_image;
}