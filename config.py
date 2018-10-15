#################################################################################################################################
#
# Conf File Driven Approach :
# This is important to encapsulate MP logic and abstract and encapsulate it for ease of extendibility and maintence.
# The testers need not know python MP to make use of this script.
#
# With conf file approach, automating future IO workload tests cases is simply passing a different conf file.
# The intention of this framework is to rely on conf files for manipulating TCs and Not library code itself.
#
# It is also important to note that changing Conf inputs will also help in clasification of test cases as Sanity, Funcational,
# Stress, Load, Performance test suites for regression runs.
#
# TBD : The intention is to use different conf files divided based on Test funcationality, coverage and stage of release.
# Ex : SimpleTC.xml can be a single conf for All simple Cases.
#	 functionalTCs.xml can be a single conf for automated functional TCs.
#	 BVTConf.xml, StressTCs.xml et al.
#
# TBD : Most of the test framework library remains same but is polymorphic depending on Type of Conf file passed.
# This approach helps in least code modification for passing new TC inputs and is easy to maintain and modify.
# The complexity of the test framework should be abstracted as much as possible in the framework libraries.
#
###############################################################################################################################

#####################################################################################################
#
# Loggingv : To Save MP Logging to a file for debugging and analysis. Be verbose.
# Logging to a single file from multiple processes.
#
# TBD : Sending and receiving logging events across clients.
# TBD : Dealing with log handlers that block.
# TBD : Adding contextual information, filters to logging output
# TBD : Dedicate one thread in one of the existing processes to perform this function
#
#####################################################################################################
import multiprocessing
import logging

def crt_mp_logger():

    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("crt-del-test.log")
    fmt = '%(levelname)s: %(asctime)s - %(processName)s - %(name)s - %(process)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

# Export it for common logging practises throughout the framework.
LOGGER = crt_mp_logger()

# TBD: This value should be self populated. It is not easy to mention tens of machines details like below.
# Test environment will contain hundereds of test VMs. We need to deploy our own Infra to discover and query it.
REMOTE_MACHINES = {
    'MACHINE1_IP':'192.xxx.xx.xx',
    'MACHINE1_UNAME':'ajay',
    'MACHINE1_PWD':'ajaypwd',
    'MACHINE2_IP':'192.xxx.xx.xx',
    'MACHINE2_UNAME':'test',
    'MACHINE2_PWD':'test1234',
    }

# We want the create-delete file loop to continue forever. We keep a watch of the disk utilization.
# Create file threads are spawned and allowed to create files till the "up threashold", after which,
# the delete threads start to delete the files till the disk usage does not <= "down" threshold.
# This is better than saying, run for x duration, there is manual cleanup required for different setups.
DISK_SIZE_THRESHOLD = {
    'up':80,
    'down':10,
    }

# Location to create, delete files from.
DISK_MOUNT = {
    'mount_path':'/AWS-S3/Bucket'
    }

   
###############################################################################################################################
#
# 'bucket_test_prefix' : All test bucketss created by the framework will have this prefix for easy identifcation and test
#						 manipulation.
#
###############################################################################################################################

#dir_test_prefix = 'bucket_test'
#dir_test_size = 'TESTBUCKETSIZE'

###############################################################################################################################
#
# 'object_name_prefix' : All objects created through the automated suite use this prefix for easy identifcation and test
#                        manipulation.
#
###############################################################################################################################

#file_test_prefix = 'object_test'

###############################################################################################################################
#
# object_size : Workload characterization is an important factor. Every software behaves differently depending on
#               the workload it is subjected to. 'Object_sizes' input should depict real world workloads.
#               The problem with comma-separated-values is that they are 'fixed' till values are explicitly changed.
#               It is important to Randomize selection of object size programtcially, thus mitigating the need of manually changing
#               test input for each run.
#
##############################################################################################################################

#file_sizes =

##############################################################################################################################
#
# 'storage_fill_level' : This input is the amount of storage to fill for triggering other test scenarios.
#                        The test framework spawns a threads to keep a track of memory usuage and when storage_fill_level is met, exits.
# default : The input is a decimal represenatation of the storage percent to fill up. Ex : 0.8 represents 80% of storage fill.
#
# 'storage_empty_level' : Storage Threshold value to reach for a trigger point Or meeting a workload test conditons.
#  Ex : This flag is useful to start creating files after mentioned storage threshold is reached. 0.7 represents storage as 70% empty.
#
##############################################################################################################################

#storage_fill_level  = 0.8
#storage_empty_level = 0.7


#  no_write_process : TBD : NOTES/COMMENTS
#  no_del_process : TBD : NOTES/COMMENTS
