"""Start of script
File name: Sys_Module.py
Author: Rutuja Jain
Tool: pycharm

"""

import sys, os

print(os.getcwd())
#print("You have entered: ", sys.argv[1], sys.argv[2], sys.argv[3])
#print(sys.exit())

number = 100
print(sys.maxsize)

print(sys.path)

print(sys.api_version)

print(sys.platform)

print(sys.version)

print(sys.exec_prefix)



'''os_module'''
print(os.name)

print(os.path)

print(os.getcwd())

print(os.listdir())

print(dir(os))
print(os.chdir('C:\\Users\\pc\\PycharmProjects\\Assignment'))

print(os.getcwd())

print(os.environ.get('Path'))
