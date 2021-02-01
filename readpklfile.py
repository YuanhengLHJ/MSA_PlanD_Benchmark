
# -*- coding: UTF8 -*-
'''
# cPickle是python2系列用的，3系列已经不用了，直接用pickle就好了
import pickle

# 重点是rb和r的区别，rb是打开2进制文件，文本文件用r
f = open('mosi_data.pkl','rb')
data = pickle.load(f)
print(data)
'''
import os
import sys
import pickle
import numpy as np
info = pickle.load(open('mosi_data.pkl',"rb"))

print(info["train"]["id"]) 
print(info["train"]["labels"]) 


print(info["train"]["vision"].shape) 
print(info["train"]["vision"].shape) 
print(info["train"]["text"].shape) 

print(info["train"]["audio"].shape) 
print(info["train"]["labels"].shape) 
print(info["train"]["labels"][372]) 
