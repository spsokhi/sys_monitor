# System Monitoring Tool

A Python-based real-time system monitoring tool that tracks CPU, memory, and disk usage. The tool provides a live visualization of system metrics and can be customized for different refresh rates and thresholds.

## Features
- Real-time monitoring of:
  - **CPU Usage**
  - **Memory Usage**
  - **Disk Usage**
- Live updating graphs for system performance metrics.
- Adjustable refresh rate for updating the graph.
- Optimized for minimal resource consumption.

## Requirements
- Python 3.x
- Virtual environment (recommended)

### Python Packages
The tool uses the following Python libraries:
- `psutil` (for fetching system metrics)
- `matplotlib` (for visualizing system metrics)

## Installation

### 1. Clone the Repository
```
git clone https://github.com/spsokhi/sys_monitor.git
cd sys_monitor
```

### 2. Set up a Virtual Environment
```
python -m venv sys_monitor_venv
On Windows, use: sys_monitor_venv\Scripts\activate
On MacOs/Linux, use: source sys_monitor_venv/bin/activate
```

### 3. Install Dependencies
```
pip install psutil matplotlib win10toast
```

### 4. Run the Tool
```
python system_monitor.py
```

## Usage
Once you run the tool, you will see a real-time graph showing:
- **CPU Usage (%)**
- **Memory Usage (%)**
- **Disk Usage (%)**

### Adjusting the Refresh Rate
By default, the tool updates every 1 second (1000 milliseconds). You can adjust the refresh rate by modifying the `refresh_rate` variable in the `system_monitor.py` file.

```python
# Example: Setting refresh rate to 2 seconds (2000 ms)
refresh_rate = 2000
```

## Customization
The tool can be easily extended to include additional system metrics such as network usage or more detailed disk I/O statistics. You can also modify the graph’s appearance (colors, line styles) using `matplotlib`.

---

