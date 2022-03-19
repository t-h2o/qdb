
# Import libraries
import lldb
import sys
import os
#import time


VERSION = "1.0"

def __lldb_init_module(debugger, internal_dict):
    
    res = lldb.SBCommandReturnObject()
    output = debugger.GetCommandInterpreter()

    output.HandleCommand("settings set prompt \"(qdb) \"", res) 
    return

#-----------------------------------
# main
#-----------------------------------
    

print("===============")
print("QDB vesrion", VERSION)
print("===============")
