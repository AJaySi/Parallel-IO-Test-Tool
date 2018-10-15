#!/usr/bin/env python
import paramiko
import config
import time
from manager import MPfileops

# Read the test threshold values from the config.py
logger = config.LOGGER
upper_threshold = config.DISK_SIZE_THRESHOLD['up']
lower_threshold = config.DISK_SIZE_THRESHOLD['down']
current_disk_size = 0

# This function will check the disk size periodically and compare with thresholds.
# When disk size is greater than upper threshold, delete file threads are called, else
# files are created by threads to fill disk.
def execute():
    global current_disk_size
    mpops_obj = MPfileops()
    while True:
        if get_disk_size() <= upper_threshold:
            logger.info('Threshold reached: create to add files +++++++')
            time.sleep(2)
            mpops_obj.create()

        elif get_disk_size() >= upper_threshold:
            while get_disk_size() >= lower_threshold:
                logger.info('Threshold Reached: delete to remove files --------')
                mpops_obj.delete() 


# util function to fetch current disk usage size from host to compare with thresholds.
# TBD: validate the disk size across all the remote nodes as an additional check
# return: current used disk size in int
def get_disk_size():
    
    global current_disk_size
	# create the SSH client and maybe put in conf file. Will give abstraction from paramiko.
	# Lets try and fail.
    client = paramiko.SSHClient()  
    logger.info('Creating the SSH Client now') ##TBD: Offload  the below in utils
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_server = config.REMOTE_MACHINES['MACHINE2_IP']
    remote_user = config.REMOTE_MACHINES['MACHINE2_UNAME']
    remote_pwd = config.REMOTE_MACHINES['MACHINE2_PWD']
    try:
		# connect the remote machine
        client.connect(remote_server, username= remote_user, password=remote_pwd)  
        logger.info('connected to the host : {}'.format(remote_server))
    except Exception as e:
        logger.error('Error during server connection: {}'.format(e))

	# TBD: decide on using mountpoint from config
    check_disk_usage = "df -h | grep test_vol | awk '{print $5}'| sed 's/%//g'" 
    try:
		# Execute command on machine.
		# TBD: this can be done locally on the same node with storage with fabric.
        stdin, stdout, stderr = client.exec_command(check_disk_usage)  
        logger.info('Executing Disk usage command')
		# We will need to manage the local and remote test machines as per request
        output = stdout.readlines()                 
        current_disk_size = int(''.join(output))
    except Exception as e:
        logger.error('Error during Disk Usage command: {}'.format(e))

	# Close the paramiko connection	
    client.close()  
    logger.info('current disk usage size is:{}'.format(current_disk_size))
    return current_disk_size

if __name__ == '__main__':
	# Call the execute function to set things in motion.
    execute()
