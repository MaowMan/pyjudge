from Scripts.JudgeBase import JudgeObj,JudgeError
from subprocess import run,PIPE,TimeoutExpired
class JudgeMain(JudgeObj):
    def __init__(self,Student,Problem,Testcase):
        super(JudgeMain,self).__init__()
        with open("{}{}-{}.in".format(self.MainConfig["Environmentfolder"],Problem.Name,Testcase.Seq),"r") as reader:
            inputfile=reader.read()
        with open("{}{}-{}.out".format(self.MainConfig["Environmentfolder"],Problem.Name,Testcase.Seq),"r") as reader:
            outputfile=reader.read()
        try:
            process=run(["python","{}{}-{}.{}".format(self.MainConfig["Environmentfolder"],Student.Name,Problem.Name,self.MainConfig["Filetype"])],input=inputfile,stdout=PIPE,stderr=PIPE,timeout=1,encoding="ascii")
        except (TimeoutExpired):
            self.Result=("TLE",0)
        if len(process.stderr)==0:
            if outputfile==process.stdout:
                self.Result=("AC",Testcase.Score)
            else:
                self.Result=("WA:{}->{}".format(outputfile,process.stdout),0)
        else:
            self.Result=("NA:{}".format(process.stderr),0)
    
