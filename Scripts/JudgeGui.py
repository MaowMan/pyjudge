from tkinter import *
from tkinter import filedialog
from Scripts.JudgeBase import JudgeObj,JudgeError,JudgeTk
import json as json
from shutil import copyfile
class JudgeSetup(JudgeTk):
    def __init__(self):
        super(JudgeSetup,self).__init__()
        self.Root.title(self.GUIConfig["Title"])
        self.SetupLayout()
        self.Mainloop()
    def SetupLayout(self):
        self.SelectFolderLabel=Label(self.Root,text="選擇目標測驗資料夾:",font=self.Font)
        self.SelectFolderLabel.grid(row=0,column=0,sticky=W)
        self.FolderVar=StringVar()
        self.FolderVar.set(self.MainConfig["Environmentfolder"][:-1])
        self.FolderPathLabel=Label(self.Root,bg="gray",textvariable=self.FolderVar,font=self.Font)
        self.FolderPathLabel.grid(row=0,column=1,sticky=W)
        self.SelectFolderButton=Button(self.Root,text="選擇",font=self.Font,command=self.select_environment_folder)
        self.SelectFolderButton.grid(row=0,column=2,sticky=W+E)

        self.StudentsLabel=Label(self.Root,text="輸入學生名單",font=self.Font)
        self.StudentsLabel.grid(row=1,column=0,columnspan=1,sticky=W)
        self.StudentsInfoLabel=Label(self.Root,bg="gray",text="格式:學生姓名以換行分隔",font=self.Font)
        self.StudentsInfoLabel.grid(row=1,column=1,sticky=W)
        self.StudentsButton=Button(self.Root,text="編輯",font=self.Font,command=lambda :JudgeTextEditor(self.FolderVar.get()+"/Students.data"))
        self.StudentsButton.grid(row=1,column=2,sticky=W+E)

        self.ProblemLabel=Label(self.Root,text="輸入題目資訊",font=self.Font)
        self.ProblemLabel.grid(row=2,column=0,sticky=W)
        self.ProblemNoteLabel=Label(self.Root,text="格式:題號-測資數量，以換行分隔",font=self.Font,bg="gray")
        self.ProblemNoteLabel.grid(row=2,column=1,sticky=W)
        self.ProblemButton=Button(self.Root,text="編輯",font=self.Font,command=lambda :JudgeTextEditor(self.FolderVar.get()+"/Problems.data"))
        self.ProblemButton.grid(row=2,column=2,sticky=W+E)

        self.IndexLabel=Label(self.Root,text="測資詳細訊息",font=self.Font)
        self.IndexLabel.grid(row=3,column=0,columnspan=1,sticky=W)
        self.IndexInfoLabel=Label(self.Root,bg="gray",text="格式:分數-限制秒數",font=self.Font)
        self.IndexInfoLabel.grid(row=3,column=1,sticky=W)
        self.IndexEditButton=Button(self.Root,text="編輯",font=self.Font,command=lambda: self.edit_problem_index(".data"))
        self.IndexEditButton.grid(row=3,column=2)
        self.UpperBlankLabel=Label(self.Root,text="測資輸入檔案",font=self.Font)
        self.UpperBlankLabel.grid(row=4,column=0,columnspan=2,sticky=W)
        self.InputEditButton=Button(self.Root,text="編輯",font=self.Font,command=lambda: self.edit_problem_index(".in"))
        self.InputEditButton.grid(row=4,column=2)
        self.LowerBlankLabel=Label(self.Root,text="測資輸出檔案",font=self.Font)
        self.LowerBlankLabel.grid(row=5,column=0,columnspan=2,sticky=W)
        self.OutputEditButton=Button(self.Root,text="編輯",font=self.Font,command=lambda: self.edit_problem_index(".out"))
        self.OutputEditButton.grid(row=5,column=2)

        self.SelectScriptsLabel=Label(self.Root,text="選擇學生程式碼",font=self.Font)
        self.SelectScriptsLabel.grid(row=6,column=0,columnspan=2,sticky=W)
        self.SelectScriptsButton=Button(self.Root,text="選擇",font=self.Font,command=self.select_scripts)
        self.SelectScriptsButton.grid(row=6,column=2)

        self.SaveConfigButton=Button(self.Root,text="儲存",font=self.Font,fg="red",command=self.save_config)
        self.SaveConfigButton.grid(row=7,column=2)
    def Mainloop(self):
        self.Root.mainloop()
    

    def edit_problem_index(self,filetype):
        with open(self.FolderVar.get()+"/Problems.data","r") as reader:
            lines=reader.readlines()
        print(lines)
        for line in lines:
            for i in range(int(line.split("-")[1])):
                print("{}-{}{}".format(line.split("-")[0],str(i),filetype))
                JudgeTextEditor(self.FolderVar.get()+("/{}-{}{}".format(line.split("-")[0],str(i),filetype)))


    def select_environment_folder(self):
        EnvFolder=filedialog.askdirectory(title="選擇測驗環境資料夾")
        if len(EnvFolder) != 0:
            self.FolderVar.set(EnvFolder)
    
    def select_scripts(self):
        files=filedialog.askopenfilenames(title="選擇學生程式檔案(複數)")
        for file_ in files:
            filename=file_.split("/")[-1]
            copyfile(file_,self.FolderVar.get()+"/"+filename)

    def save_config(self):
        pass

            

class JudgeTextEditor(JudgeTk):
    def __init__(self,location):
        super(JudgeTextEditor,self).__init__()
        self.Location=location
        self.Root.title(self.Location)
        self.TopbarMenu=Menu(self.Root)
        self.Root.config(menu=self.TopbarMenu)
        self.TopbarMenu.add_command(label="儲存",command=self.Store)
        self.Text=Text(self.Root,undo=True)
        self.Text.grid(row=0,column=0)
        self.Scroll=Scrollbar(self.Root,command=self.Text.yview)
        self.Scroll.grid(row=0,column=1,sticky=N+S)
        self.Text.config(yscrollcommand=self.Scroll.set)
        self.Text.bind("<Control-s>",self.Store)
        try:
            self.Open()
        except(FileNotFoundError):
            pass
    def Open(self):
        with open(self.Location,"r") as reader:
            content=reader.read()
        self.Text.delete("1.0",END)
        self.Text.insert(END,content)
    def Store(self,nothing=0):
        content=self.Text.get("1.0","end-1c")
        with open(self.Location,"w") as writer:
            writer.write(content)
        self.Root.destroy()