import os
import sys
sys.path.insert(0,os.getcwd()"/src")
import useful_functions

def str_to_dic(string):
    obj = {}
    for kv in string.split("&"):
        kv = kv.split('=')
        obj[kv[0]] = obj[1]
    return obj
def profile_for(string):
    string.replace('&','').replace('=','')
    str_to_dic("email="+string+"&udi=10&role=user")
    