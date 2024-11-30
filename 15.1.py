import multiprocessing
import os
import time     
import random 
from datetime import datetime

def job():
    #wait random number of seconds between 0-1
    wait_time = random.uniform(0,1)
    time.sleep(wait_time)
    #print current time
    current_time = datetime.now() .strftime("%Y-%m-%d %H:%M:%S")
    print(f"process {multiprocessing.current_process() .name} waited {wait_time: .2f} seconds and printed the time: {current_time}")
    
if __name__ == "__main__":
    #hold list
    processes = []
    #3 processes
    for i in range (3):
        process=multiprocessing.Process(target=job, name=f"Process-{i+1}")
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()