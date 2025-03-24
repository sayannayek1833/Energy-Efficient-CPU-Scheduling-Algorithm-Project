import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Energy-Efficient First Come First Serve (FCFS) Scheduling
def energy_efficient_fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])  # Sort by arrival time
    time = 0
    total_energy = 0

    for process in processes:
        if time < process['arrival']:  
            time = process['arrival']  # If CPU is idle, move to process arrival time

        # Dynamic Voltage and Frequency Scaling (DVFS) Simulation
        cpu_frequency = 1.5 if process['burst'] > 5 else 2.5  # Reduce frequency for long tasks
        
        process['completion'] = time + process['burst']
        process['turnaround'] = process['completion'] - process['arrival']
        process['waiting'] = process['turnaround'] - process['burst']

        # Energy Calculation: Energy = Power × Time
        power_consumption = cpu_frequency * 0.5  # Simulated power model
        energy_used = power_consumption * process['burst']
        total_energy += energy_used

        time = process['completion']

    print(f"\nTotal Energy Consumed: {total_energy:.2f} Joules")
    return processes


# Energy-Efficient Shortest Job First (SJF) Scheduling
def energy_efficient_sjf(processes):
    processes.sort(key=lambda x: (x['arrival'], x['burst']))  # Sort by arrival & burst time
    time = 0
    total_energy = 0
    completed = []

    while processes:
        available_processes = [p for p in processes if p['arrival'] <= time]

        if not available_processes:
            time = processes[0]['arrival']  # If CPU is idle, move to the next process arrival
            continue

        current = min(available_processes, key=lambda x: x['burst'])  # Select shortest job
        processes.remove(current)

        # DVFS Simulation
        cpu_frequency = 1.5 if current['burst'] > 5 else 2.5  # Reduce frequency for long tasks

        current['completion'] = time + current['burst']
        current['turnaround'] = current['completion'] - current['arrival']
        current['waiting'] = current['turnaround'] - current['burst']

        # Energy Calculation
        power_consumption = cpu_frequency * 0.5  # Simulated power model
        energy_used = power_consumption * current['burst']
        total_energy += energy_used

        time = current['completion']
        completed.append(current)

    print(f"\nTotal Energy Consumed: {total_energy:.2f} Joules")
    return completed


# Energy-Efficient Round Robin Scheduling
def energy_efficient_round_robin(processes, quantum):
    queue = deque()
    time = 0
    total_energy = 0

    for process in processes:
        process['remaining'] = process['burst']
        process['completion'] = 0

    processes.sort(key=lambda x: x['arrival'])
    queue.append(processes[0])
    index = 1

    while queue:
        current = queue.popleft()

        if time < current['arrival']:  
            time = current['arrival']  # If CPU is idle, move forward

        # DVFS Simulation
        cpu_frequency = 1.8 if current['remaining'] > quantum else 2.2  # Lower frequency for long tasks

        execution_time = min(current['remaining'], quantum)
        time += execution_time
        current['remaining'] -= execution_time

        # Energy Calculation
        power_consumption = cpu_frequency * 0.4  # Simulated power model
        energy_used = power_consumption * execution_time
        total_energy += energy_used

        if current['remaining'] == 0:  
            current['completion'] = time
            current['turnaround'] = current['completion'] - current['arrival']
            current['waiting'] = current['turnaround'] - current['burst']
        else:
            queue.append(current)  # Requeue unfinished process

        while index < len(processes) and processes[index]['arrival'] <= time:
            queue.append(processes[index])
            index += 1

    print(f"\nTotal Energy Consumed: {total_energy:.2f} Joules")
    return processes


# Function to run the selected scheduling algorithm
def run_scheduling():
    global process_list
    algo = algo_var.get()
    
    if not process_list:
        messagebox.showerror("Error", "No processes added!")
        return

    if algo == "FCFS":
        results = energy_efficient_fcfs(process_list)
    elif algo == "SJF":
        results = energy_efficient_sjf(process_list)
    elif algo == "Round Robin":
        results = energy_efficient_round_robin(process_list, quantum=int(quantum_entry.get()))
    else:
        messagebox.showerror("Error", "Select a valid algorithm")
        return

    show_results(results)

# Function to add process to the list
def add_process():
    try:
        pid = len(process_list) + 1
        arrival = int(arrival_entry.get())
        burst = int(burst_entry.get())

        process_list.append({'id': pid, 'arrival': arrival, 'burst': burst})
        process_display.insert("", "end", values=(pid, arrival, burst))

    except ValueError:
        messagebox.showerror("Error", "Invalid input! Enter integers.")

# Function to show results (Gantt Chart & Energy Analysis)
def show_results(results):
    fig, ax = plt.subplots()
    y_labels = []
    start_time = 0
    total_energy = 0

    for process in results:
        y_labels.append(f"P{process['id']}")
        ax.broken_barh([(start_time, process['burst'])], (len(y_labels) * 10, 9), facecolors=('tab:blue'))
        
        energy_used = (2.5 if process['burst'] < 5 else 1.5) * process['burst'] * 0.5
        total_energy += energy_used
        
        start_time += process['burst']

    ax.set_yticks([i * 10 + 5 for i in range(len(y_labels))])
    ax.set_yticklabels(y_labels)
    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title(f"Energy-Efficient {algo_var.get()} Scheduling (Total Energy: {total_energy:.2f}J)")

    plt.show()

# Function to reset input fields
def reset_fields():
    arrival_entry.delete(0, tk.END)
    burst_entry.delete(0, tk.END)

# Tkinter Main Window
root = tk.Tk()
root.title("Energy-Efficient CPU Scheduling Simulator")
root.geometry("600x500")

process_list = []

# Algorithm Selection
tk.Label(root, text="Select Scheduling Algorithm:").pack()
algo_var = tk.StringVar(value="FCFS")
algo_dropdown = ttk.Combobox(root, textvariable=algo_var, values=["FCFS", "SJF", "Round Robin"])
algo_dropdown.pack()

# Process Input
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Arrival Time:").grid(row=0, column=0)
arrival_entry = tk.Entry(frame)
arrival_entry.grid(row=0, column=1)

tk.Label(frame, text="Burst Time:").grid(row=1, column=0)
burst_entry = tk.Entry(frame)
burst_entry.grid(row=1, column=1)

tk.Button(frame, text="Add Process", command=add_process).grid(row=2, column=0, columnspan=2)

# Round Robin Quantum Input
tk.Label(root, text="Time Quantum (for RR):").pack()
quantum_entry = tk.Entry(root)
quantum_entry.pack()

# Display Process Table
process_display = ttk.Treeview(root, columns=("ID", "Arrival", "Burst"), show="headings")
process_display.heading("ID", text="PID")
process_display.heading("Arrival", text="Arrival Time")
process_display.heading("Burst", text="Burst Time")
process_display.pack()

# Run Simulation Button
tk.Button(root, text="Run Simulation", command=run_scheduling).pack(pady=5)
tk.Button(root, text="Reset Fields", command=reset_fields).pack(pady=5)

root.mainloop()
