#!/usr/bin/env python
import psutil
import os 
process = psutil.Process(os.getpid())
def get_usage():    
    #print(process.memory_info().rss)  # in bytes 
    return {
        "CPU":psutil.cpu_percent()
        #,"MEMUSED":dict(psutil.virtual_memory()._asdict())["used"]
        ,"MEMUSED":process.memory_info().rss
    }
