import threading

# Define dimensions
M = 2  # Number of rows in A
N = 3  # Number of columns in A and rows in B
P = 2  # Number of columns in B

# Input matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Result matrix C (M x P)
C = [[0 for _ in range(P)] for _ in range(M)]

# Thread function
def multiply_element(i, j, result_holder):
    sum = 0
    for k in range(N):
        sum += A[i][k] * B[k][j]
    result_holder[i][j] = sum
    # Simulate pthread_exit with a return (but store result in shared matrix)
    return

# Main function
def main():
    threads = []
    result_holder = [[0 for _ in range(P)] for _ in range(M)]  # Shared matrix

    # Create threads for each cell C[i][j]
    for i in range(M):
        for j in range(P):
            thread = threading.Thread(target=multiply_element, args=(i, j, result_holder))
            threads.append(thread)
            thread.start()  # Simulates pthread_create

    # Wait for threads to complete
    for thread in threads:
        thread.join()  # Simulates pthread_join

    # Final result handled in main thread
    print("Resultant Matrix (C = A x B):")
    for row in result_holder:
        print(row)

if __name__ == "__main__":
    main()
