from tkinter import *
from tkinter import filedialog
from Scripts.JudgeBase import JudgeObj,JudgeError,JudgeTk
import json as json

class JudgeSetup(JudgeTk):
    def __init__(self):
        super(JudgeSetup,self).__init__()
        self.Root.title(self.GUIConfig["Title"])
        self.SetupLayout()
        self.Mainloop()
    def SetupLayout(self):
        self.SelectFolderLabel=Label(self.Root,text="選擇目標測驗資料夾:",font=self.Font)
        self.SelectFolderLabel.grid(row=0,column=0)
        self.FolderVar=StringVar()
        self.FolderVar.set(self.MainConfig["Environmentfolder"])
        self.FolderPathLabel=Label(self.Root,bg="gray",textvariable=self.FolderVar,font=self.Font)
        self.FolderPathLabel.grid(row=0,column=1)
        self.SelectFolderButton=Button(self.Root,text="選擇",font=self.Font,command=self.select_environment_folder)
        self.SelectFolderButton.grid(row=0,column=2)

    def Mainloop(self):
        self.Root.mainloop()




    def select_environment_folder(self):
        EnvFolder=filedialog.askdirectory(title="選擇測驗環境資料夾")
        if len(EnvFolder) != 0:
            self.FolderVar.set(EnvFolder)


class JudgeTextEditor(JudgeTk):
    def __init__(self,Dir):
        super(JudgeTextEditor,self).__init__()
        self.Savelocation=Dir
        self.TopbarMenu=Menu(self.Root)
        self.Root.config(menu=self.TopbarMenu)
        self.Root.config(title=Dir)
        self.TopbarMenu.add_command(text="儲存",command=self.Store())
        self.Text=Text(self.Root,undo=True)
        self.Text.grid(row=0,column=0)
        self.Scroll=Scrollbar(self.Root,command=self.Text.yview)
        self.Scroll.grid(row=0,column=1,sticky=N+S)
        self.Text.config(yscrollcommand=self.Scroll.set)
    def Store(self):
        content=self.Text.get("1.0","end-1c")
        with open(self.Savelocation,"w") as writer:
            writer.write(content)
        self.Root.destroy()