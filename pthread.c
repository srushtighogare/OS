#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define M 2 // Rows in A
#define N 3 // Columns in A / Rows in B
#define P 2 // Columns in B

int A[M][N] = {
    {1, 2, 3},
    {4, 5, 6}
};

int B[N][P] = {
    {7, 8},
    {9, 10},
    {11, 12}
};

int C[M][P]; // Result matrix

// Struct to pass multiple arguments to thread
typedef struct {
    int row;
    int col;
} ThreadArgs;

// Thread function
void* multiply_element(void* args) {
    ThreadArgs* data = (ThreadArgs*) args;
    int i = data->row;
    int j = data->col;

    int* result = (int*) malloc(sizeof(int)); // Value to return
    *result = 0;
    for (int k = 0; k < N; k++) {
        *result += A[i][k] * B[k][j];
    }

    pthread_exit(result); // Return result
}

int main() {
    pthread_t threads[M][P];
    ThreadArgs args[M][P];
    void* ret_val;

    // Create threads
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < P; j++) {
            args[i][j].row = i;
            args[i][j].col = j;
            pthread_create(&threads[i][j], NULL, multiply_element, &args[i][j]);
        }
    }

    // Join threads and collect results
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < P; j++) {
            pthread_join(threads[i][j], &ret_val);
            C[i][j] = *(int*)ret_val;
            free(ret_val); // Free allocated memory
        }
    }

    // Display result matrix
    printf("Resultant Matrix (C = A x B):\n");
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < P; j++) {
            printf("%d\t", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}
