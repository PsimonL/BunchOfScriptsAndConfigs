import psutil

cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True) # for each core
cpu_count = psutil.cpu_count(logical=False) # total number of CPU cores

memory = psutil.virtual_memory()
memory_percent = memory.percent



print("Memory Usage: {:.2f}%".format(memory_percent)) # RAM usage
