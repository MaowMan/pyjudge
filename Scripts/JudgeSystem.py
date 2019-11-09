import json as json 
import csv as csv
from Scripts.JudgeBase import  JudgeObj,JudgeError
from Scripts.JudgeMain import JudgeMain

class JudgeSystem(JudgeObj):
    def __init__(self):
        super(JudgeSystem,self).__init__()
        self.SetupAsset()
        self.CheckFileExists()
        self.MainProcess()
        self.StoreResult()
    def SetupAsset(self):
        with open(self.MainConfig["Environmentfolder"]+"Info.json","r") as reader:
            self.Info=json.loads(reader.read())
        self.Problems=JudgeProblems(self.Info["Problems"])
        self.Students=JudgeStudents(self.Info["Students"])
    def CheckFileExists(self):
        for Problem in self:
            for Testcase in Problem:
                try:
                    with open("{}{}-{}.in".format(self.MainConfig["Environmentfolder"],Problem.Name,Testcase.Seq),"r") as reader:
                        pass
                except(FileNotFoundError):
                    raise JudgeError("{}{}-{}.in not found".format(self.MainConfig["Environmentfolder"],Problem.Name,Testcase.Seq))
                try:
                    with open("{}{}-{}.out".format(self.MainConfig["Environmentfolder"],Problem.Name,Testcase.Seq),"r") as reader:
                        pass
                except(FileNotFoundError):
                    raise JudgeError("{}{}-{}.out not found".format(self.MainConfig["Environmentfolder"],Problem.Name,Testcase.Seq))
    def MainProcess(self):
        for Student in self.Students:
            for Problem in self.Problems:
                for Testcase in Problem:
                    Student.Load(JudgeMain(Student,Problem,Testcase).Result)
    def StoreResult(self):
        with open("{}{}.csv".format(self.MainConfig["Environmentfolder"],self.Info["Name"]),"w",newline="") as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(self.Problems.Firstrow())
            for Student in self.Students:
                writer.writerow(Student.Flush())
        print("Program Ended")



class JudgeProblems(JudgeObj):
    def __init__(self,Data):
        super(JudgeProblems,self).__init__()
        self.Container=[]
        for Problem in Data:
            self.Container.append(JudgeProblem(Problem))
    def Firstrow(self):
        result=["Id","Name","ResultScore"]
        for Problem in self:
            for Testcase in Problem:
                result+=["{}-{}_Status".format(Problem.Name,Testcase.Seq),"{}-{}_Score".format(Problem.Name,Testcase.Seq)]
        return result

class JudgeProblem(JudgeObj):
    def __init__(self,Data):
        super(JudgeProblem,self).__init__()
        self.Name=Data["Name"]
        for Testcase in Data["Testcases"]:
            self.Container.append(JudgeTestcase(Testcase))

class JudgeTestcase(JudgeObj):
    def __init__(self,Data):
        self.Score=Data["Score"]
        self.Seq=Data["Seq"]
        self.Timelimit=Data["Timelimit"]

class JudgeStudents(JudgeObj):
    def __init__(self,Data):
        super(JudgeStudents,self).__init__()
        Cache=0
        for Student in Data:
            self.Container.append(JudgeStudent(Cache,Student))
class JudgeStudent(JudgeObj):
    def __init__(self,Id,Name):
        self.Id=Id
        self.Name=Name
        self.Score=0
        self.Result=[]
    def Flush(self):
        return ([self.Id,self.Name,self.Score]+self.Result)
    def Load(self,data):
        self.Score+=data[1]
        self.Result+=[data[0].replace("\n",""),data[1]]