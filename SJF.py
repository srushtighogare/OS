# Shortest Job First (Non-Preemptive) Scheduling

def find_waiting_time(processes, n, bt, wt):
    # Sort processes based on burst time
    sorted_processes = sorted(zip(processes, bt), key=lambda x: x[1])
    
    wt[0] = 0  # Waiting time for the shortest (first) process is 0

    # Calculate waiting time for each process
    for i in range(1, n):
        wt[i] = sorted_processes[i - 1][1] + wt[i - 1]

    return [p[0] for p in sorted_processes], [p[1] for p in sorted_processes]

def find_turn_around_time(bt, wt, tat):
    for i in range(len(bt)):
        tat[i] = bt[i] + wt[i]

def find_avg_time(processes, n, bt):
    wt = [0] * n
    tat = [0] * n

    # Sort processes and calculate waiting times
    sorted_processes, sorted_bt = find_waiting_time(processes, n, bt, wt)

    # Calculate turnaround times
    find_turn_around_time(sorted_bt, wt, tat)

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"{sorted_processes[i]}\t\t{sorted_bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turnaround Time = {total_tat / n:.2f}")

# Driver code
if __name__ == "__main__":
    processes = [1, 2, 3, 4]
    burst_time = [6, 8, 7, 3]  # Burst times
    n = len(processes)

    find_avg_time(processes, n, burst_time)
