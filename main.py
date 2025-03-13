def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival'])  # Sort processes by arrival time
    time = 0  # Tracks the current time in the CPU

    for process in processes:
        if time < process['arrival']:  # If the CPU is idle, jump to the arrival time
            time = process['arrival']

        process['completion'] = time + process['burst']  # Completion time = current time + burst time
        process['turnaround'] = process['completion'] - process['arrival']  # Turnaround time = completion - arrival
        process['waiting'] = process['turnaround'] - process['burst']  # Waiting time = turnaround - burst

        time = process['completion']  # Update current time for the next process

def get_process_input():
    processes = []
    n = int(input("Enter number of processes: "))

    for i in range(n):
        arrival = int(input(f"Enter arrival time for Process p{i+1}: "))
        burst = int(input(f"Enter burst time for Process {i+1}: "))
        processes.append({'id': i+1, 'arrival': arrival, 'burst': burst})
    
    return processes

processes = get_process_input()
fcfs_scheduling(processes)

for p in processes:
    print(f"Process {p['id']}: Completion={p['completion']}, Waiting={p['waiting']}, Turnaround={p['turnaround']}")
