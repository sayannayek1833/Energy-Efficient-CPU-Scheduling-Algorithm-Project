Project Overview
This project simulates CPU scheduling while focusing on reducing energy consumption by dynamically adjusting CPU frequency based on the burst time of processes. It visualizes the execution of processes through a Gantt Chart and calculates the total energy consumed by different scheduling algorithms.

Key Features:
Scheduling Algorithms Implemented:

FCFS (First-Come, First-Serve): Executes processes in the order of arrival.

SJF (Shortest Job First): Picks the process with the shortest burst time.

Round Robin (RR): Cycles through processes with a defined time quantum.

Energy Optimization with DVFS:

Reduces CPU frequency for long processes to save energy.

Increases CPU frequency for short tasks to ensure minimal delay.

Gantt Chart and Energy Analysis:

Displays process execution order.

Shows total energy consumption after simulation.

Dynamic GUI with Tkinter:

Add processes dynamically.

Select desired algorithms.

View results interactively.

How Energy Efficiency is Achieved
1. Dynamic Voltage and Frequency Scaling (DVFS) Simulation
Short Tasks (burst ≤ 5): CPU operates at a higher frequency (2.5 GHz) to reduce latency.

Long Tasks (burst > 5): CPU operates at a lower frequency (1.5 GHz) to conserve energy.
Code Components Overview
1. Energy-Efficient FCFS Scheduling
Sorts processes based on arrival time.

Applies DVFS to adjust CPU frequency dynamically.

Calculates turnaround time, waiting time, and energy usage.

2. Energy-Efficient Round Robin Scheduling
Uses time quantum to cycle through processes.

Requeues unfinished processes until completion.

Dynamically adjusts CPU frequency to reduce energy consumption.

3. Energy-Efficient SJF Scheduling
Selects the shortest burst task available at any time.

Optimizes energy by dynamically adjusting CPU frequency.

Computes waiting time, turnaround time, and energy used.

4. Gantt Chart and Energy Visualization
Displays a Gantt Chart to show process execution.

Annotates the chart with process names and timelines.

Displays total energy consumption post-simulation.
