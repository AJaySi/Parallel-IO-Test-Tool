# mp-file-crt-del
Using python multiprocess module for creating and deleting files in a loop, based on a condition.

Multiprocessing IO Workload Automation

Workload details : 
- Multi client Orchastration (TBD). There is option to use fabric, smallfiles. Pyhton pp module is also a good choice.
- Multiprocess IO
- MP Logging 

Prerequisites :

- Two Linux machines (Physical/Virtual) with 2/3 NIC installed.
- Object storage. Copy the code-drop directory on one Linux machine
- Shared storage attached to both the Linux machine
- python 2.7

Following Config values needs to be edited :

- Edit the config.py file for user input
- Provide details of IP Address and user credentials
- Provide the mount point
- In DISK_SIZE_THRESHOLD 
  

Steps to run the script :
Enter a command from "python run_io.py"


View the logs :

- Log file "MP-POC.log" will be generated at current working directory.


Summary : 

Create and delete processes continue to run, until interrupted. ForkBombs.
There is multiprocessing logging for each process spawned and maintained/logged for its lifetime.



