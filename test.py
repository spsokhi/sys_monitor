import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    return disk_info.percent

def get_network_io():
    network_info = psutil.net_io_counters()
    return network_info.bytes_sent, network_info.bytes_recv

if __name__ == "__main__":
    print(f"CPU Usage: {get_cpu_usage()}%")
    print(f"Memory Usage: {get_memory_usage()}%")
    print(f"Disk Usage: {get_disk_usage()}%")
    sent, recv = get_network_io()
    print(f"Bytes Sent: {sent}")
    print(f"Bytes Received: {recv}")
