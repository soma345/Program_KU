import os
import psutil
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
print('memory use:', memoryUse)
print('cpu use', psutil.cpu_percent())
print('vm use ', psutil.virtual_memory())  # physical memory usage