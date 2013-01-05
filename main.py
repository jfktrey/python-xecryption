#########################################
# XECryption Crack Helper v3
# Treyk4 3/26/09

#TODO: make it so you can choose which char in "Quick" method (radiobuttons w/ most common letters, last radiobutton for custom input field)

from tkinter import *
import os

global restoreText, passVal, yesno
restoreText = ""
passVal = 0

class Alert(Toplevel):
    def __init__(self, parent, dtext, title = None):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None
        self.grab_set()

        self.protocol("WM_DELETE_WINDOW", self.kill)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))
        
        
        Label(self, text=dtext).pack()
        b = Button(self, text="OK", command=self.kill)
        b.pack(pady=5)
        
        
        self.focus_set()
        self.wait_window(self)
    
    def kill(self):
        self.parent.focus_set()
        self.destroy()

def thorough_call():
    global passVal, yesno
    tto = three_to_one_func(tbox.get(1.0, END))
    if tto != -1:
        firstchar = int(tto.split("\n")[0])
        for i in range(0,255):
            passVal = firstchar - i
            decoded_text = three_decode_guts(False)
            if decoded_text != -1:
                tbd = YesNoTextDialog(root, decoded_text, title="Does this look correct?")
                if yesno == True:
                    frontappend = "* Password collective value: %s\n* Decrypted message below (excluding *'s)\n*********************************************\n" %passVal
                    tbox.config(state=NORMAL)
                    tbox.delete(1.0, END)
                    tbox.insert(1.0, frontappend+decoded_text)
                    tbox.config(state=DISABLED)
                    break
                elif yesno == None:
                    yesno = True
                    break
                        
    if not yesno:
        al = Alert(root, "You couldn't decrypt the text this way either?\nThen something strange is going on here...")

def quick_call():
    global passVal, yesno
    tto = three_to_one_func(tbox.get(1.0, END))
    onelist_clean = []
    passwds_used = []
    if tto != -1:
        onelist = tto.split("\n")
        for i in onelist:
            if i != "":
                onelist_clean.append(i)
        
        for i in onelist_clean:
            i=int(i)-32
            if i not in passwds_used:
                passwds_used.append(i)
                passVal = i
                decoded_text = three_decode_guts(False)
                if decoded_text != -1:
                    tbd = YesNoTextDialog(root, decoded_text, title="Does this look correct?")
                    if yesno == True:
                        frontappend = "* Password collective value: %s\n* Decrypted message below (excluding *'s)\n*********************************************\n" %passVal
                        tbox.config(state=NORMAL)
                        tbox.delete(1.0, END)
                        tbox.insert(1.0, frontappend+decoded_text)
                        tbox.config(state=DISABLED)
                        break
                    elif yesno == None:
                        yesno = True
                        break
        
        if not yesno:
            al = Alert(root, "No suitable password found. You might\nwhat to try the thorough method...?")

class PassPrompt(Toplevel):
    def __init__(self, parent, title=None):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None
        self.grab_set()

        self.protocol("WM_DELETE_WINDOW", self.kill)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))
        
        
        Label(self, text="Password value?").pack()
        self.e = Entry(self)
        self.e.pack(padx=5)
        b = Button(self, text="OK", command=self.ok)
        b.pack(pady=5)
        
        
        self.e.focus_set()
        self.wait_window(self)
    
    def ok(self, event=None):
        global passVal
        passVal = self.e.get()
        self.parent.focus_set()
        self.destroy()
        three_decode_guts(True)
    def kill(self):
        self.parent.focus_set()
        self.destroy()

class YesNoTextDialog(Toplevel):
    def __init__(self, parent, text, title = None):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None
        self.grab_set()

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))
        
        
        self.topfrm = Frame(self)
        self.topfrm.pack()
        self.sbar = Scrollbar(self.topfrm)
        self.sbar.pack(side=RIGHT, fill=Y)
        self.tbox = Text(self.topfrm, height=10, width=45, background="black", foreground="white", state=NORMAL)
        self.tbox.insert(1.0, text)
        self.tbox.config(state=DISABLED)
        self.tbox.pack()

        self.tbox.config(yscrollcommand=self.sbar.set)
        self.sbar.config(command=self.tbox.yview)
        
        
        self.diagFrame = LabelFrame(self, text="Correct?", padx=10, pady=3)
        self.diagFrame.pack(pady=3)
        self.cpy = Button(self.diagFrame, text="Yes", command=self.yes)
        self.cpy.grid(row=0,column=0, padx=3, pady=0)
        self.ok = Button(self.diagFrame, text="No", command=self.no)
        self.ok.grid(row=0,column=1, padx=3, pady=0)
        self.cancel = Button(self.diagFrame, text="Cancel", command=self.cancel)
        self.cancel.grid(row=0,column=2, padx=3, pady=0)
        
        
        self.focus_set()
        self.wait_window(self)
    
    def kill(self):
        pass
    def yes(self, event=None):
        global yesno
        yesno = True
        self.parent.focus_set()
        self.destroy()
    def no(self, event=None):
        global yesno
        yesno = False
        self.parent.focus_set()
        self.destroy()
    def cancel(self, event=None):
        global yesno
        yesno = None
        self.parent.focus_set()
        self.destroy()


#class tboxDialog:
#    def __init__(self, parent, text):
#        top = self.top = Toplevel(parent)
#        top.title("Most Occurring #'s")
#        top.geometry('+20+20')
#        
#        diagTbox = self.diagTbox = Text(top, height=30, width=60, background="black", foreground="white", state=DISABLED)
#        diagTbox.config(state=NORMAL)
#        diagTbox.insert(1.0, text)
#        diagTbox.config(state=DISABLED)
#        self.diagTbox.pack()
#        diagFrame = self.diagFrame = LabelFrame(top, text="Correct?")
#        self.diagFrame.pack(pady=3)
#        cpy = self.cpy = Button(diagFrame, text="Yes", command=self.yes)
#        self.cpy.grid(row=0,column=0, padx=3, pady=0)
#        ok = self.ok = Button(diagFrame, text="No", command=self.no)
#        self.ok.grid(row=0,column=1, padx=3, pady=0)
#        
#        self.top.focus_set()
#        
#        self.wait_window(root)
#
#    def yes(self):
#        global yesno
#        yesno = True
#        self.top.destroy()
#    
#    def no(self):
#        global yesno
#        yesno = False
#        self.top.destroy()

def delete_call():
    tbox.config(state=NORMAL)
    tbox.delete(1.0, END)
    tbox.config(state=DISABLED)

def paste_call():
    global restoreText
    tbox.config(state=NORMAL)
    tbox.delete(1.0, END)
    root.tk.call('tk_textPaste', tbox._w)
    tbox.config(state=DISABLED)
    restoreText = tbox.get(0.0,END)

def copy_call():
    tbox.config(state=NORMAL)
    tbox.tag_add(SEL, "1.0", END)
    tbox.focus_set()
    root.tk.call('tk_textCopy', tbox._w)
    bottom.focus_set()
    tbox.config(state=DISABLED)

#def three_to_one_call():
#    text = tbox.get(1.0, END)
#    out = three_to_one_func(text)
#    if out != -1:
#        tbox.config(state=NORMAL)
#        tbox.delete(1.0, END)
#        tbox.insert(1.0, out)
#        tbox.config(state=DISABLED)
#    else:
#        al = Alert(root, "You have improperly formatted text, the\n number of values must be a multiple of three.")

#def mode_of_one_call():
##    text = tbox.get(1.0, END)
##    tbd = tboxDialog(root, mode_of_one_func(text))
#    text = tbox.get(1.0, END)
#    out = mode_of_one_func(text)
#    tbox.config(state=NORMAL)
#    tbox.delete(1.0, END)
#    tbox.insert(1.0, out)
#    tbox.config(state=DISABLED)

def restore_call():
    global restoreText
    tbox.config(state=NORMAL)
    tbox.delete(1.0, END)
    tbox.insert(1.0, restoreText)
    tbox.config(state=DISABLED)

def decode_call():
    global passVal
    pp = PassPrompt(root, title="Password?")
    
def three_decode_guts(setMainText):
    global passVal
    single = three_to_one_func(tbox.get(1.0, END))
    if single != -1:
        single_list = single.split("\n")
        single_list_clean = []
        ascii_vals = []
        
        for i in single_list:
            if i != "":
                single_list_clean.append(i)
        
        for i in single_list_clean:
            i = int(i)
            ascii_vals.append(i-int(passVal))
        try:
            ascii_string = ''.join(chr(i) for i in ascii_vals)
        except:
            ascii_string = -1
        
        print("\n%s\n" %ascii_string)
        
        if (setMainText):
            if ascii_string != -1:
                frontappend = "* Password collective value: %s\n* Decrypted message below (excluding *'s)\n*********************************************\n" %passVal
                ascii_string = frontappend + ascii_string
                tbox.config(state=NORMAL)
                tbox.delete(1.0, END)
                tbox.insert(1.0, ascii_string)
                tbox.config(state=DISABLED)
            else:
                tbox.config(state=NORMAL)
                tbox.delete(1.0, END)
                tbox.insert(1.0, "It is not possible to decode the encrypted text using  this password.")
                tbox.config(state=DISABLED)
        else:
            return ascii_string
    else:
        return -1

def three_to_one_func(text):
    numberList_o = []
    numberList = []
    singleVals = []
    currentVal = 0
    thirdsDone = 0
    textOutput = ""
    
    numberList_o = text.split(".")
    numberList_o.pop(0)
    
    for i in numberList_o:
        try:
            numberList.append(int(i))
        except:
            return -1
    
    if (float(len(numberList))/3.0) == float(len(numberList)/3):
        for i in numberList:
            if thirdsDone < 3:
                currentVal += int(i)
                thirdsDone += 1
            else:
                singleVals.append(currentVal)
                currentVal = int(i)
                thirdsDone = 1
        
        for i in singleVals:
            textOutput += str(i)+"\n"
        
        return textOutput
    
    else:
        return -1
        

#def numInList(num, nestList):
#    if nestList != []:
#        for i in range(0, len(nestList)):
#            if str(nestList[i][0]) == str(num):
#                return -1
#        return i
#
#def getTopSix(list):
#    newListOrder=[]
#    
#    for i in list:
#        if newListOrder != []:
#            lastPosition = 0
#            inserted = False
#            for i2 in range(0,len(newListOrder)):
#                if i[1] > newListOrder[i2][1]:
#                    newListOrder.insert(lastPosition, i)
#                    inserted = True
#                    break
#                else:
#                    lastPosition += 1
#            if not inserted:
#                newListOrder.append(i)
#        else:
#            newListOrder = [i]
#
#    toReturn = []
#    n = 0
#    while n < 6:
#        toReturn.append(newListOrder[n])
#        n+=1
#    
#    return toReturn

def mode_of_one_func(text):
    textArray = text.split("\n")
    textArrayNew = []
    modeArray = []
    
    for i in range(0,len(textArray)):
        if (textArray[i] != ""):
            textArrayNew.append(textArray[i])
    
    for i in textArrayNew:
        i = str(i)
        nil = numInList(i, modeArray)
        if (nil != -1):
            modeArray.append([i, 1])
        else:
            modeArray[nil][1] += 1
    
    top6 = getTopSix(modeArray)
    toReturn = "The space character most likely to be one of these:\n\n"
    for i in top6:
        toReturn += "%s: %s\n" %(i[0], i[1])
    
    return toReturn
    

#------------------------------


root = Tk()
root.resizable(0,0)
#root.iconbitmap(default="./icon.ico")
root.title("XECryption Crack Helper v4.1")

topfrm = Frame(root)
topfrm.pack()

scrollbar = Scrollbar(topfrm)
scrollbar.pack(side=RIGHT, fill=Y)

tbox = Text(topfrm, height=25, width=55, background="black", foreground="white", state=DISABLED)
tbox.pack()

tbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tbox.yview)

bottom = Frame(root)
bottom.pack()

group2 = LabelFrame(bottom, text="Function", padx=5, pady=5)
group2.grid(row=0, column=0, padx=10, pady=10)

button2_1 = Button(group2, text="Paste", command=paste_call)
button2_1.grid(row=0,column=0, padx=3, pady=0)
button2_2 = Button(group2, text="Copy all", command=copy_call)
button2_2.grid(row=0,column=1, padx=3, pady=0)
button2_3 = Button(group2, text="Clear", command=delete_call)
button2_3.grid(row=0,column=2, padx=3, pady=0)
button2_4 = Button(group2, text="Restore", command=restore_call)
button2_4.grid(row=0,column=3, padx=3, pady=0)

group1 = LabelFrame(bottom, text="Crack Methods", padx=5, pady=5)
group1.grid(row=0, column=1, padx=10, pady=10)

button1_1 = Button(group1, text="Quick", command=quick_call)
button1_1.grid(row=0,column=0, padx=3, pady=0)
button1_2 = Button(group1, text="Thorough", command=thorough_call)
button1_2.grid(row=0,column=1, padx=3, pady=0)
button1_3 = Button(group1, text="Decode w/ pass", command=decode_call)
button1_3.grid(row=0,column=2, padx=3, pady=0)

root.mainloop()
