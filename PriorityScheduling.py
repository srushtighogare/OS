# Priority Scheduling (Non-Preemptive)

def find_waiting_time(processes, n, bt, priority, wt):
    # Sort processes based on priority (lower value means higher priority)
    sorted_processes = sorted(zip(processes, bt, priority), key=lambda x: x[2])

    wt[0] = 0  # First process has 0 waiting time

    # Calculate waiting time
    for i in range(1, n):
        wt[i] = sorted_processes[i - 1][1] + wt[i - 1]

    # Return sorted process info
    return (
        [p[0] for p in sorted_processes],  # Process IDs
        [p[1] for p in sorted_processes],  # Burst Times
        [p[2] for p in sorted_processes]   # Priorities
    )

def find_turn_around_time(bt, wt, tat):
    for i in range(len(bt)):
        tat[i] = bt[i] + wt[i]

def find_avg_time(processes, n, bt, priority):
    wt = [0] * n
    tat = [0] * n

    # Get sorted processes by priority and calculate WT
    sorted_processes, sorted_bt, sorted_priority = find_waiting_time(processes, n, bt, priority, wt)

    # Calculate TAT
    find_turn_around_time(sorted_bt, wt, tat)

    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"{sorted_processes[i]}\t\t{sorted_bt[i]}\t\t{sorted_priority[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turnaround Time = {total_tat / n:.2f}")

# Driver Code
if __name__ == "__main__":
    processes = [1, 2, 3, 4]
    burst_time = [10, 1, 2, 1]
    priority = [3, 1, 4, 2]  # Lower number = higher priority
    n = len(processes)

    find_avg_time(processes, n, burst_time, priority)
