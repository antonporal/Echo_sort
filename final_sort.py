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
print("IMPORTED EVERYTHING")

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return join(sys._MEIPASS, relative)
    return join(relative)

print("CREATED RESOURCE_PATH FUNCITON")
#GUI for selecting DICOM folder
window = tk.Tk()
root = tk.Tk()
root.withdraw()
print("OPEN TK INSTANCES")
data_dir = filedialog.askdirectory()
print("ASK FOR FOLDER")
#Get all the files in the top level of the DICOM folder
files = [f for f in listdir(data_dir) if isfile(resource_path(join(data_dir, f)))]
print("GET FILES")
#Change directory to DICOM folder
os.chdir(data_dir)
print("CHANGE DIRECTORIES")
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
print("DONE WITH FOR LOOP")
window.title(data_dir)
window.after(1000, window.quit)
window.after(1000, window.destroy)
print("DONE WITH PROGRAM")
window.mainloop()