# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:44:39 2022

@author: aporal
"""
import sys
from os import listdir
from os.path import isfile, join
import os
import pydicom
import tkinter as tk 
from tkinter import filedialog

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return join(sys._MEIPASS, relative)
    return join(relative)

#GUI for selecting DICOM folder
window = tk.Tk()
root = tk.Tk()
root.withdraw()

data_dir = filedialog.askdirectory()

#Get all the files in the top level of the DICOM folder
files = [f for f in listdir(data_dir) if isfile(resource_path(join(data_dir, f)))]

#Change directory to DICOM folder
os.chdir(data_dir)
for f in files:
    if f.startswith("IM"):
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
window.title(data_dir)
window.after(1000, window.quit)
window.after(1000, window.destroy)
window.mainloop()