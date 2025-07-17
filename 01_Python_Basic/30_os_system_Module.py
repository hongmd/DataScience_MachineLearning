'''
"os" is a built-in Python module that provides a way of using operating system dependent functionality,
like reading or writing to the file system, executing shell commands, and more.

This module allows you to interact with the underlying operating system in a platform-independent way.
It includes functions to work with files and directories, manage processes, and perform other system-related tasks.
It is commonly used for tasks such as file manipulation, environment variable access, and executing system commands.

The "os" module is part of the Python Standard Library, 
so it is available in any Python installation without needing to install anything extra.
'''

######

'''
Flow of contents:
1. Basic Inspection: os.name, os.uname(), os.cpu_count()
2. Working Directory Navigation: os.getcwd(), os.chdir()
3. File and Directory Operations: os.listdir(), os.scandir(), os.mkdir(), os.makedirs(), os.rmdir(), os.remove(), os.rename()
4. Running System Commands: os.system(), os.popen(), os.execvp(), os.execvpe()
5. Environment Variables: os.environ, os.getenv(), os.putenv()
'''

import os


#----------------------------------------------------------------------------------------------------#
#------------------------------------ 1. Basic Inspection -------------------------------------------#
#----------------------------------------------------------------------------------------------------#

#############
## os.name ##
#############

# os.name returns the name of the operating system dependent module imported.
# It can return 'posix', 'nt', 'os2', 'ce', 'java', or 'riscos'.
# This can be useful to determine the platform your code is running on.

print(os.name)  # posix 
# (Linux, macOS)


# Example of using os.name to check the platform
if os.name == 'nt':
    print("Running on Windows")
elif os.name == 'posix':
    print("Running on Unix-like OS (Linux, macOS)")
else:
    print("Running on an unknown OS")

# >>> Running on Unix-like OS (Linux, macOS)


################
## os.uname() ##
################

# os.uname() returns a tuple containing information about the operating system.
# It includes the system name, node name (hostname), release, version, and machine type

print(os.uname())
# posix.uname_result(sysname='Linux', nodename='fedora', release='6.15.4-200.fc42.x86_64', 
#                    version='#1 SMP PREEMPT_DYNAMIC Fri Jun 27 15:32:46 UTC 2025', machine='x86_64')


# Example of using os.uname() to get system information
system_info = os.uname()
print(f"System: {system_info.sysname}") # System: Linux
print(f"Node Name: {system_info.nodename}") # Node Name: fedora
print(f"Release: {system_info.release}") # Release: 6.15.4-200.fc42.x86_64
print(f"Version: {system_info.version}") # Version: #1 SMP PREEMPT_DYNAMIC Fri Jun 27 15:32:46 UTC 2025
print(f"Machine: {system_info.machine}") # Machine: x86_64


####################
## os.cpu_count() ##
####################

# os.cpu_count() returns the number of CPUs in the system.

print(os.cpu_count()) # 32 
# 32 (threads)
# 16 (cores)


#---------------------------------------------------------------------------------------------#
#------------------------------- 2. Working Directory Navigation -----------------------------#
#---------------------------------------------------------------------------------------------#

#################
## os.getcwd() ##
#################

# os.getcwd() returns the current working directory as a string. (like "pwd" command in Linux)
print(os.getcwd())  # /home/longdpt/Documents/Academic/DataScience_MachineLearning


################
## os.chdir() ##
################

# os.chdir(path) changes the current working directory to the specified path. (like "cd" command in Linux)
os.chdir('/home/longdpt/Documents/Academic')  # Change to a different directory

# Change to the parent directory
os.chdir('..')  # The '..' means the parent directory of the current working directory

# Verify the change
print(os.getcwd())  # /home/longdpt/Documents/Academic


#----------------------------------------------------------------------------------------------#
#------------------------------- 3. File and Directory Operations -----------------------------#
#----------------------------------------------------------------------------------------------#

##################
## os.listdir() ##
##################

# os.listdir(path) returns a list of the entries in the directory given by path.

# List files in the current directory ('.' means current directory
print(os.listdir('.'))  
# ['01_Python_Basic', 'merge_mp4.sh', 'Unrar_file.txt', '.git', 'Python_Important_packages.txt', 'vscode_install_settings.txt', 'Calculus_ConvexOptimization', '.gitignore', '02_Python_class_OOP']


# List files in a specific directory
print(os.listdir('/home/longdpt/Documents/Academic'))
# ['Biotech_books_summary', 'MachineLearning_ThayLoi', 'Cancer_NGS_ThayLoi', 'DataScience_HCMUS', 'LDS9 Chapter 12 Cung cấp tài nguyên triển khai hệ thống Master - Workers.rar', 'LDS9 Bigdata.rar', 'LDS8.rar', 'HTDS_272.rar', 'Biotechnology_HCMUS', 'Toan_hoc_chan_phuong.pdf', 'git_practice', 'Bioinformatics_Linux_R_Python', 'DataScience_MachineLearning', 'Programming_Materials']


# Store output of os.listdir() in a variable
dir_contents = os.listdir('/home/longdpt/Documents/Academic')
print(dir_contents)


##################
## os.scandir() ##
##################

# os.scandir() is similar to os.listdir() but returns an iterator of DirEntry objects, which include file attributes.
# This is more efficient for large directories as it avoids multiple system calls.

# scan then printout each entry in the directory
with os.scandir('/home/longdpt/Documents/Academic') as entries:
    print(entries) # <posix.ScandirIterator object at 0x7f4da1f29930>
    for entry in entries:
        print(entry)
        # <DirEntry 'Biotech_books_summary'>
        # <DirEntry 'MachineLearning_ThayLoi'>
        # <DirEntry 'Cancer_NGS_ThayLoi'>
        # <DirEntry 'DataScience_HCMUS'>
        # <DirEntry 'LDS9 Chapter 12 Cung cấp tài nguyên triển khai hệ thống Master - Workers.rar'>
        # <DirEntry 'LDS9 Bigdata.rar'>
        # <DirEntry 'LDS8.rar'>
        # <DirEntry 'HTDS_272.rar'>
        # <DirEntry 'Biotechnology_HCMUS'>
        # <DirEntry 'Toan_hoc_chan_phuong.pdf'>
        # <DirEntry 'git_practice'>
        # <DirEntry 'Bioinformatics_Linux_R_Python'>
        # <DirEntry 'DataScience_MachineLearning'>
        # <DirEntry 'Programming_Materials'>


# scan then printout each entry's attributes (name, type, size)
with os.scandir('/home/longdpt/Documents/Academic') as entries:
    for entry in entries:
        if entry.is_file():
            print(f"File: {entry.name}, Size: {entry.stat().st_size} bytes")
        elif entry.is_dir():
            print(f"Directory: {entry.name}")
            # Directory: Biotech_books_summary
            # Directory: MachineLearning_ThayLoi
            # Directory: Cancer_NGS_ThayLoi
            # Directory: DataScience_HCMUS
            # File: LDS9 Chapter 12 Cung cấp tài nguyên triển khai hệ thống Master - Workers.rar, Size: 18511520311 bytes
            # File: LDS9 Bigdata.rar, Size: 12382626277 bytes
            # File: LDS8.rar, Size: 11672272532 bytes
            # File: HTDS_272.rar, Size: 3878818433 bytes
            # Directory: Biotechnology_HCMUS
            # File: Toan_hoc_chan_phuong.pdf, Size: 272921745 bytes
            # Directory: git_practice
            # Directory: Bioinformatics_Linux_R_Python
            # Directory: DataScience_MachineLearning
            # Directory: Programming_Materials