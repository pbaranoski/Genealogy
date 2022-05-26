import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import *
from tkinter.tix import *

import renameFiles

def getDirPath (lblLabel):
    dirPath = tk.filedialog.askdirectory()
    print("##Directory: "+dirPath)

    #entry2.insert(0,str(dirPath))
    lblLabel.config(text=dirPath)


def renameFilesAction():
    
    # load variables with window values
    sParish = tkParishChoiceVar.get()   
    print(sParish)
    curDir = lblSearchDirText.cget("text")

    # Verify that input values have been entered/selected
    if curDir == "":
        messagebox.showerror("Error", "No input directory has been selected!")
        return

    if sParish == "":
        messagebox.showerror("Error", "No Parish Selected!")
        return

    #print(f"curDir: {curDir}")
    #print(sParish)
    renameFiles.processDir(curDir, sParish)

    ###########################################
    # Comparison has completed
    ###########################################
    messagebox.showinfo("Complete", "Parish Files have been renamed!")


def main():

    ####################################################
    # define variables
    ####################################################
    global MDIWnd
    global lblSearchDirText
    global tkParishChoiceVar

    ####################################################
    # Build window
    ####################################################
    MDIWnd= tk.Tk()
    MDIWnd.title("Rename Parish Files")
    MDIWnd.geometry("1000x300")

    lblHdr = tk.Label(MDIWnd, text='Rename Parish Files')
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
    lstParishChoices = ["Nur", "Boguty", "Kuczyn", "Czyżew", "Zuzela", "Filipów", "Jeleniewo", "Suwałki"]

    lblParish = tk.Label(MDIWnd, text='Select Parish:')
    lblParish.config(font=('helvetica', 10))
    lblParish.grid(row=4, column=2, sticky='e', pady=3)
   
    # Create a Tkinter variable
    tkParishChoiceVar = tk.StringVar(MDIWnd)

    # Dictionary with options
    tkParishChoiceVar.set(lstParishChoices[0]) # set the default option

    dropdown = tk.OptionMenu(MDIWnd, tkParishChoiceVar, *lstParishChoices)
    dropdown.grid(row=4, column=3, sticky='w', pady=5)

    ###############################
    # Buttons
    ###############################
    bthSearchFiles = tk.Button(text='Rename Files', command=lambda:renameFilesAction(), bg='blue', fg='white', font=('helvetica',10, 'bold'))
    bthSearchFiles.grid(row=6, column=3, sticky='w', pady=10)

    ####################################
    # Process Window messages
    ####################################
    MDIWnd.mainloop()


if __name__ == "__main__":
    
    main()




