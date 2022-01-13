# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:44:39 2022

@author: aporal
"""

from os import listdir
from os.path import isfile, join
import os
import pydicom
import tkinter as tk 
from tkinter.filedialog import askdirectory

#GUI for selecting DICOM folder

root = tk.Tk()
root.withdraw()
root.mainloop()
filepath = askdirectory()

#Get all the files in the top level of the DICOM folder
files = [f for f in listdir(filepath) if isfile(join(filepath, f))]

#Change directory to DICOM folder
os.chdir(filepath)
n=1
for f in files:
    #read DICOM
    ds = pydicom.filereader.dcmread(f)
    #check if folder exists for Echo Time
    folder = str(ds.EchoTime)
    isExist = os.path.exists(folder)
    if not isExist:
        os.makedirs(folder)
        newPath = folder+"\\"+f
        ds.save_as(newPath)
    else:
        newPath = folder+"\\"+f
        ds.save_as(newPath)
    print(str(n)+"/"+str(len(files)))
    n+=1