import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import *
from tkinter.tix import *

import string
import os

import backupChangedFilesInDir


def getDirPath (lblLabel):
    dirPath = tk.filedialog.askdirectory()
    print("##Directory: "+dirPath)

    #entry2.insert(0,str(dirPath))
    lblLabel.config(text=dirPath)


def backupChangedFilesAction():
    
    # load variables with window values
    sDriveLetter = tkDriveChoiceVar.get() [0:1]   
    print(sDriveLetter)
    curDir = lblSearchDirText.cget("text")

    # Verify that input values have been entered/selected
    if curDir == "":
        messagebox.showerror("Error", "No input directory has been selected!")
        return

    if sDriveLetter == "":
        messagebox.showerror("Error", "No Drive Selected!")
        return

    #print(f"curDir: {curDir}")
    #print(sDriveLetter)
    backupChangedFilesInDir.backupDriveLetter = sDriveLetter
    backupChangedFilesInDir.processDir(curDir)

    ###########################################
    # Comparison has completed
    ###########################################
    messagebox.showinfo("Complete", "Changed Files have been backed-up!")


def main():

    ####################################################
    # define variables
    ####################################################
    global MDIWnd
    global lblSearchDirText
    global tkDriveChoiceVar

    ####################################################
    # Build window
    ####################################################
    MDIWnd= tk.Tk()
    MDIWnd.title("Backup Changed Files")
    MDIWnd.geometry("1000x300")

    lblHdr = tk.Label(MDIWnd, text='Backup Changed Files')
    lblHdr.config(font=('helvetica', 14))
    lblHdr.grid(row=0, column=3, columnspan=3, padx=5, pady=10)

    lblSpacer = tk.Label(MDIWnd, text="          ")
    lblSpacer.grid(row=0, column=0)

    ##############################
    # Select InFile1
    ##############################
    btnInFile1 = tk.Button(text='Select File', command=lambda:getDirPath(lblSearchDirText), bg='blue', fg='white', font=('helvetica', 8, 'bold'))
    btnInFile1.grid(row=1, column=1, padx=5, pady=3)

    #lblSearchDirLabel = tk.Label(MDIWnd, text='Input File 1:', bd=1, relief="sunken")
    lblSearchDirLabel = tk.Label(MDIWnd, text='Folder Path to Process:')
    lblSearchDirLabel.config(font=('helvetica', 10))
    lblSearchDirLabel.grid(row=1, column=2, sticky='e', pady=1)

    # Selected InFile1
    lblSearchDirText = tk.Label(MDIWnd, text="")
    lblSearchDirText.config(font=('helvetica', 10))
    lblSearchDirText.grid(row=1, column=3, sticky='w')

    ###############################
    # Columns to Omit
    ###############################
    #lstDrives = ["C:"]
    lstDrives = [f"{d}:" for d in string.ascii_uppercase if os.path.exists(f"{d}:")]
    lstDrives.remove("C:")

    lblDrives = tk.Label(MDIWnd, text='Select Drive:')
    lblDrives.config(font=('helvetica', 10))
    lblDrives.grid(row=4, column=2, sticky='e', pady=3)
   
    # Create a Tkinter variable
    tkDriveChoiceVar = tk.StringVar(MDIWnd)

    # Dictionary with options
    if len(lstDrives) > 0:
        tkDriveChoiceVar.set(lstDrives[0]) # set the default option
    else:
        lstDrives.append("")    

    dropdown = tk.OptionMenu(MDIWnd, tkDriveChoiceVar, *lstDrives)
    dropdown.grid(row=4, column=3, sticky='w', pady=5)

    ###############################
    # Buttons
    ###############################
    bthSearchFiles = tk.Button(text='Backup Files', command=lambda:backupChangedFilesAction(), bg='blue', fg='white', font=('helvetica',10, 'bold'))
    bthSearchFiles.grid(row=6, column=3, sticky='w', pady=10)

    ####################################
    # Process Window messages
    ####################################
    MDIWnd.mainloop()


if __name__ == "__main__":
    
    main()




