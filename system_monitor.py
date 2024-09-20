import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from threading import Thread
import time

# Initialize lists to store data
cpu_data, memory_data, disk_data = [], [], []

# Refresh rate (default 1000 ms)
refresh_rate = 1000  # 1 second

# Function to fetch system metrics
def get_system_metrics():
    while True:
        cpu_usage = psutil.cpu_percent(interval=0.5)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        cpu_data.append(cpu_usage)
        memory_data.append(memory_usage)
        disk_data.append(disk_usage)

        # Limit data lists to the last 50 entries for better performance
        cpu_data[:] = cpu_data[-50:]
        memory_data[:] = memory_data[-50:]
        disk_data[:] = disk_data[-50:]

        time.sleep(refresh_rate / 1000)  # Sleep for the refresh rate in seconds

# Function to update the plot
def update_plot(frame):
    plt.cla()  # Clear the current plot

    if cpu_data and memory_data and disk_data:
        # Plot CPU, memory, and disk usage
        plt.plot(cpu_data, label=f"CPU Usage ({cpu_data[-1]:.1f}%)")
        plt.plot(memory_data, label=f"Memory Usage ({memory_data[-1]:.1f}%)")
        plt.plot(disk_data, label=f"Disk Usage ({disk_data[-1]:.1f}%)")

        plt.ylim(0, 100)  # Set Y-axis limit from 0% to 100% for CPU, memory, and disk
        plt.legend(loc="upper right")
        plt.title("Real-Time System Metrics")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Usage (%)")

# Start fetching system metrics in a separate thread
metrics_thread = Thread(target=get_system_metrics, daemon=True)
metrics_thread.start()

# Create the plot
fig = plt.figure()

# Animate the plot, updating every `refresh_rate` ms
ani = FuncAnimation(fig, update_plot, interval=refresh_rate, cache_frame_data=False)

# Show the plot
plt.tight_layout()
plt.show()
