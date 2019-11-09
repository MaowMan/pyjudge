import json as json 
from tkinter import *
class JudgeObj(object):
    def __init__(self):
        with open("./Config/MainConfig.json","r") as reader:
            self.MainConfig=json.loads(reader.read())
        self.Container=[]
    def __iter__(self):
        self.Counter=-1
        return self
    def __next__(self):
        if self.Counter==len(self.Container)-1:
            raise StopIteration
        else:
            self.Counter+=1
            return self.Container[self.Counter]

class JudgeError(BaseException):
    pass

class JudgeTk(JudgeObj):
    def __init__(self):
        super(JudgeTk,self).__init__()
        self.Root=Tk()
        with open("./Config/GUIConfig.json","r") as reader:
            self.GUIConfig=json.loads(reader.read())
        self.Font=(self.GUIConfig["Font"],self.GUIConfig["WordSize"])