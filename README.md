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



Updated


Energy-Efficient CPU Scheduling Simulator

Overview

This is a Python-based CPU Scheduling Simulator built using Tkinter for the graphical user interface and Matplotlib for visualizing scheduling algorithms through Gantt charts. The simulator supports three scheduling algorithms:

First Come First Serve (FCFS)

Shortest Job First (SJF)

Round Robin (RR)

Features

Add processes with Arrival Time and Burst Time.

Choose between different scheduling algorithms.

If Round Robin is selected, enter a Time Quantum.

Simulate CPU scheduling and visualize the Gantt Chart.

Uses Tkinter for GUI and Matplotlib for graphical representation.

Installation

Clone the repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo

Install required dependencies:

pip install matplotlib tkinter

Run the application:

python cpu_scheduler.py

How to Use

Select a scheduling algorithm from the dropdown menu.

Enter Arrival Time and Burst Time for each process and click Add Process.

If using Round Robin, specify a Time Quantum.

Click Run Simulation to generate the Gantt Chart.

File Structure

📂 cpu-scheduler
 ├── cpu_scheduler.py  # Main script for the simulator
 ├── README.md          # Project documentation
 ├── requirements.txt   # Dependencies list

Dependencies

Python 3.x

Matplotlib (for plotting Gantt Charts)

Tkinter (for GUI)

Future Enhancements

Add more scheduling algorithms like Priority Scheduling.

Improve UI design.

Display Turnaround Time and Waiting Time for each process.

Contributing

Feel free to fork this repository, make improvements, and submit a pull request!

License

This project is licensed under the MIT License.


Updated 2.0

Energy-Efficient CPU Scheduling Simulator

Overview

This Python-based GUI application simulates various CPU scheduling algorithms while optimizing energy efficiency using Dynamic Voltage and Frequency Scaling (DVFS). The simulator supports First Come First Serve (FCFS), Shortest Job First (SJF), and Round Robin (RR) scheduling policies, displaying execution order and energy consumption through a Gantt chart.

Features

FCFS (First Come First Serve): Executes processes in the order of arrival.

SJF (Shortest Job First): Selects the shortest process available at any given time.

Round Robin (RR): Uses a time quantum to fairly distribute CPU time among processes.

Energy Efficiency Optimization: Adjusts CPU frequency dynamically to minimize power consumption.

Graphical User Interface (GUI): Built using Tkinter for ease of interaction.

Gantt Chart Visualization: Displays process execution sequence and energy analysis.

Prerequisites

Ensure you have the following dependencies installed:

pip install matplotlib numpy

How to Run

Download the Python script.

Run the script using:

python script.py

Use the GUI to:

Select a scheduling algorithm.

Input process details (Arrival Time & Burst Time).

For Round Robin, specify a time quantum.

Click "Run Simulation" to view results.

Usage

Adding Processes:

Enter arrival time and burst time.

Click "Add Process" to queue the process.

Selecting Scheduling Algorithm:

Choose FCFS, SJF, or Round Robin from the dropdown.

Running Simulation:

Click "Run Simulation" to process jobs and display results.

Reset Fields:

Clears input fields for new entries.

Energy Calculation Model

DVFS Simulation:

High burst time → Lower frequency (1.5 GHz).

Low burst time → Higher frequency (2.5 GHz).

Power Model:

Power = CPU Frequency × 0.5.

Energy = Power × Execution Time.

Visualization

The Gantt chart shows process execution over time.

Displays total energy consumed in Joules.

Example Output

Total Energy Consumed: 12.50 Joules

A graphical Gantt chart will be displayed representing the scheduling process.

Author

Your Name

License

This project is licensed under the MIT License.

