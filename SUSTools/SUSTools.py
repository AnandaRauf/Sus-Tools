from neurolib.utils.loadData import Dataset
from neurolib.models.aln import ALNModel
import matplotlib.pyplot as plotmodel
print("------------------------------------------------------------------------------------------\n")
toolsname = "Sus Tools"
version = "Beta version 1.0"
devby = "Ananda Rauf Maududi"
devdate = "1 April 2021"
print("------------------------------------------------------------------------------------------\n")

class MenuTools():
    def menutools():
        print("Menu Sus Tools:")
        print
        print("1.Brain Analytics")
        print("2.Blood Analytics")
        print("3.Bone Analytics")
        print("4.Human Identation")
        print("5.Auto Detect Human Activity")

class BrainAnal():
    def brainanal(self):
        print("You're choose Brain Analytics \n")
        #Frekuensi Brain
        modelf = ALNModel()
        modelf.params['sigma_ou'] = 0.5 #Add some noise from brain
        modelf.run()
        plotmodel.plot(modelf.t,model.output.T)
        print("Frekuensi Brain accept some noise \n")

        #Data activity Brain

        datasetmodel = DataSet("gw")
        modelactivity = ALNModel(Cmat = datasetmodel.Cmat,Dmat = datasetmodel.Dmat)
        modelactivity.params['duration'] = 1*60*1000 #Time simulation brain activity #One minutes simulation
        modelactivity.run(bold=True)
        print("Simulation activity sel on Brain \n")

class BloodAnal():
    def bloodanal(self):
        print("You're choose Blood Analytics \n")

class BoneAnal():
    def boneanal(self):
        print("You're choose Bone Analytics \n")

class HumanIdent():
    def humanident(self):
        print("You're choose Human Identation\n")

class AutoDetectHuman():
    def autodetecthuman(self):
        print("You're choose Auto Detect Human Activity\n")

MenuTools.menutools()

ch = int(input("Please,choose menu Sus Tools :"))
Brain = BrainAnal()
Blood = BloodAnal()
Bone = BoneAnal()
HumanIden = HumanIdent()
AutoDetect = AutoDetectHuman()

if ch == 1:
    Brain.brainanal()
elif ch ==2:
    Blood.bloodanal
elif ch==3:
    Bone.boneanal()
elif ch==4:
    HumanIden.humanident()
elif ch==5:
    AutoDetect.autodetecthuman()
else:
    exit








