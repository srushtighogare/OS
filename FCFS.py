# FCFS Scheduling Algorithm

# Function to find the waiting time for all processes
def find_waiting_time(processes, n, bt, wt):
    wt[0] = 0  # waiting time for first process is 0

    # calculating waiting time
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

# Function to calculate turn around time
def find_turn_around_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

# Function to calculate average time
def find_avg_time(processes, n, bt):
    wt = [0] * n
    tat = [0] * n

    # Function to find waiting time of all processes
    find_waiting_time(processes, n, bt, wt)

    # Function to find turn around time for all processes
    find_turn_around_time(processes, n, bt, wt, tat)

    print("Processes Burst time Waiting time Turn around time")

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(f" {processes[i]}\t\t {bt[i]}\t\t {wt[i]}\t\t {tat[i]}")

    print(f"\nAverage waiting time = {total_wt / n:.2f}")
    print(f"Average turn around time = {total_tat / n:.2f}")


# Driver code
if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)
    burst_time = [10, 5, 8]  # Burst time for each process

    find_avg_time(processes, n, burst_time)
