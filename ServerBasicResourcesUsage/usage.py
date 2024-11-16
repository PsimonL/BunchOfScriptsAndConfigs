import psutil

cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True) # for each core
cpu_count = psutil.cpu_count(logical=False) # total number of CPU cores

memory = psutil.virtual_memory()
memory_percent = memory.percent

for core, usage in enumerate(cpu_percent_per_core):
    print("CPU Core {}: {:.2f}%".format(core, usage)) # print usage per core

total_usage = sum(cpu_percent_per_core) / cpu_count
print("Overall CPU Usage: {:.2f}%".format(total_usage)) # overall CPU usage

print("Memory Usage: {:.2f}%".format(memory_percent)) # RAM usage
