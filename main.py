print('start...')
from tkinter import *
Cout = ''
variable = {}
#window2 - (блоки из shell)
def Window2():
    window2 = Toplevel(window)
    window2.geometry('505x250+250+250')
    window2.title('GUIpy>Blocks>Shell')
    win2Button_Print = Button(window2, text="Print", width=16, height=1, command=BPrint)
    win2Button_Var = Button(window2, text="Variable", width=16, height=1, command=BVar)
    win2Button_VarP = Button(window2, text='Var + Var', width=16, height=1, command=BVarP)
    win2Button_VarM = Button(window2, text='Var - Var', width=16, height=1, command=BVarM)
    win2Button_VarMno = Button(window2, text='Var * Var', width=16, height=1, command=BVarMno)
    win2Button_Vardil = Button(window2, text='Var / Var', width=16, height=1, command=BVardil)
    win2Button_if = Button(window2, text='If', width = 16, height = 1, command=ButtonIf)
    win2B_input = Button(window2, text='Input', width=16, height=1, command=ButtonInput)
    win2Button_Var.place(x=130, y=3)
    win2Button_Print.place(x=3, y=3)
    win2Button_VarP.place(x=255, y=3)
    win2Button_VarM.place(x=380, y=3)
    win2Button_VarMno.place(x=3, y=32)
    win2Button_Vardil.place(x=130, y=32)
    win2Button_if.place(x=255, y=32)
    win2B_input.place(x=380, y=32)
    window2.mainloop()


#input window
def WinInput(textInput):
    win3 = Toplevel(window)
    win3.geometry('350x250+300+300')
    win3.title("Input")
    win3_entr = Entry(win3)
    win3_entr.place(x=10, y=100)
    win3_TEXT = Label(win3, text=textInput)
    win3_TEXT.place(x=10, y=50)
    win3_button = Button(win3, text='OK', width = 16, height = 1, command=InputButton)
    win3_button.place(x=175, y=220)

#RunCode <-----------     <------------

def WinShell():
    global Cout
    global variable
    winshell = Toplevel(window)
    winshell.geometry('653x395+250+250')
    winshell.title('Console')
    winShellCreated = True
    CShell = Text(winshell)
    CShell.place(x=3, y=3)
    #CShell.insert(END, 'govno!')
    #print(Shell)
    Cout = winTextBox.get("1.0", END)
    BlokNum = 0
    VarText = False
    VarInt = False
    VarVar = False
    VarLogic = False
    varnams = []
    SodVarText = ''
    SodVarInt = ''
    SodVarVar = ''
    SodVarLogic = ''
    symb = ''
    ifskobok = 0
    Ifcycle = False
    for i in Cout:
        symb += i
        print(symb)
        #print(VarText)
        if Ifcycle:
            if symb == '{':
                ifskobok += 1
            if symb == '}':
                ifskobok -= 1
            if ifskobok <= 0:
                Ifcycle = False
                print("if skipped!")
            symb = ''
        if VarText:
            if symb != '"':
                SodVarText += symb
                symb = ''
                print(SodVarText)
            else:
                VarText = False
                symb = ''
        if VarInt:
            if symb != '@':
                SodVarInt += symb
                symb = ''
                #print(SodVarInt)
            else:
                VarInt = False
                symb = ''
        if VarVar:
            if Action != '':
                if symb != '*':
                    SodVarVar += symb
                    symb = ''
                    #print(SodVarVar)
                else:
                    VarVar = False
                    varnams.append(SodVarVar)
                    SodVarVar = ''
                    symb = ''
        if VarLogic:
            if symb != "'":
                SodVarLogic += symb
                symb = ''
            else:
                VarLogic = False
                symb = ''

        #начало считывания блоков + аргументы
        if symb == '{':
            print("skip{")
            symb = ''
        if symb == '}':
            print("skip}")
            symb = ''
        if symb == "[":
            symb = ''
            BlokNum += 1
            varnams.clear()
        if symb == ',':
            symb = ''
            print("Next Argument")

            
        #bloks code
        if symb == 'Print::':
            Action = symb
            symb = ''
        if symb == 'Var::':
            Action = symb
            symb = ''
        if symb == 'Var+Var::': 
            Action = symb
            symb = ''
        if symb == 'Var-Var::': 
            Action = symb
            symb = ''
        if symb == 'Var/Var::': 
            Action = symb
            symb = ''
        if symb == 'Var*Var::': 
            Action = symb
            symb = ''
        if symb == 'Var^Var::': 
            Action = symb
            symb = ''
        if symb == "if::":
            Action = symb
            symb = ''
        if symb == 'Input::':
            Action = symb
            symb = ''

        #symbols. Type variable
        if symb == '"':
            VarText = True
            symb = ''
        if symb == '@':
            VarInt = True
            symb = ''
        if symb == '*':
            VarVar = True
            symb = ''
        if symb == "'":
            VarLogic = True
            symb = ""

        #срабатывает после прочтения всего блока кода!!!
        if symb == ']':
            symb = ''
            PrintEnd = '\n'
            PrintSpace = ' '
            PrintTab = '    '
            print(str(Action) + " - Action")
            if Action == 'Print::':
                if not SodVarText:
                    ShellOut = variable[varnams[0]]
                    ShellOut = str(ShellOut) + str(PrintEnd)
                    CShell.insert(END, ShellOut)
                    varnams.clear()
                else:
                    SodVarText = str(SodVarText) + str(PrintEnd)
                    #print(Console)
                    CShell.insert(END, SodVarText)
                    SodVarText = ''
            if Action == 'Var::':
                if not SodVarInt:
                    variable[varnams[0]] = str(SodVarText)
                    print(variable)
                else:
                    variable[varnams[0]] = int(SodVarInt)
                    print(variable)
            if Action == 'Var+Var::':
                print(varnams)
                chis_a = variable[varnams[1]]
                chis_b = variable[varnams[2]]
                variable[varnams[0]] = int(chis_a) + int(chis_b)
                varnams.clear()
            if Action == 'Var-Var::':
                print(varnams)
                chis_a = variable[varnams[1]]
                chis_b = variable[varnams[2]]
                variable[varnams[0]] = int(chis_a) - int(chis_b)
                varnams.clear()
            if Action == 'Var*Var::':
                print(varnams)
                chis_a = variable[varnams[1]]
                chis_b = variable[varnams[2]]
                variable[varnams[0]] = int(chis_a) * int(chis_b)
                varnams.clear()
            if Action == 'Var/Var::':
                print(varnams)
                chis_a = variable[varnams[1]]
                chis_b = variable[varnams[2]]
                variable[varnams[0]] = int(chis_a) / int(chis_b)
                varnams.clear()
            if Action == 'Var^Var::':
                print(varnams)
                chis_a = variable[varnams[1]]
                chis_b = variable[varnams[2]]
                variable[varnams[0]] = int(chis_a) ** int(chis_b)
                varnams.clear()
            if Action == 'if::':
                var1 = varnams[0]
                var2 = varnams[1]
                if SodVarLogic == '=':
                    if variable[var1] == variable[var2]:
                        ifReturn = True
                    else:
                        ifReturn = False
                if SodVarLogic == '<':
                    if variable[var1] < variable[var2]:
                        ifReturn = True
                    else:
                        ifReturn = False
                if SodVarLogic == '>':
                    if variable[var1] > variable[var2]:
                        ifReturn = True
                    else:
                        ifReturn = False
                if SodVarLogic == '!=':
                    if variable[var1] != variable[var2]:
                        ifReturn = True
                    else:
                        ifReturn = False
                if SodVarLogic == '>=':
                    if variable[var1] >= variable[var2]:
                        ifReturn = True
                    else:
                        ifReturn = False
                if SodVarLogic == '<=':
                    if variable[var1] <= variable[var2]:
                        ifReturn = True
                    else:
                        ifReturn = False
                print(str(ifReturn), ' ', str(Ifcycle))
                if ifReturn == False:
                    Ifcycle = True
                print(str(ifReturn), ' ', str(Ifcycle))
            if Action == 'Input::':
                inputOut = ''
                textinp = SodVarText
                varinp = varnams[0]
                variable[varinp] = input(textinp)
                vyvod = str(textinp) + str(variable[varinp]) 
                CShell.insert(END, vyvod)
                #InputCycle = True
                #WinInput(textinp)
                #while InputCycle:
                #    WinInput(textinp)
                #    if InputCycle == False:
                #        break
                #variable[varinp] = inputOut
            Action = ''
            VarText = False
            VarInt = False
            VarVar = False
            VarLogic = False
            SodVarText = ''
            SodVarInt = ''
            SodVarVar = ''
            SodVarLogic = ''
            varnams.clear()


def BPrint():
    winTextBox.insert(END, '[Print::""]')
def BVar():
    winTextBox.insert(END, '[Var::**,@@]')
def BVarP():
    winTextBox.insert(END, '[Var+Var::**,**,**]')
def BVarM():
    winTextBox.insert(END, '[Var-Var::**,**,**]')
def BVarMno():
    winTextBox.insert(END, '[Var*Var::**,**,**]')
def BVardil():
    winTextBox.insert(END, '[Var/Var::**,**,**]')
def ButtonIf():
    winTextBox.insert(END, "[if::**,'',**]{")
def ButtonInput():
    winTextBox.insert(END, '[Input::**,""]')

def Shell(text):
    CShell.insert(END, text)
def CodeBL_Shell():
    Window2()

#inputButton
def InputButton():
    global InputCycle
    global inputOut
    global varinp
    global variable
    global win3_entr
    inputOut = win3_entr.get()
    variable[varinp] = inputOut
    InputCycle = False
    

window = Tk()
winText = Label(text="version: Alpha 0.0.1")
window.geometry('850x450+100+100')
window.title('GUIpy Alpha 0.0.1')
winText.place(x=1, y=1)
#Place Buttons
winButton_Save = Button(text="Save", width=16, height=1)
winButton_Save.place(x=3, y=20)
winButton_SaveAs = Button(text='Save As', width=16, height=1)
winButton_SaveAs.place(x=3, y=50)
winButton_Load = Button(text='Load', width=16, height=1)
winButton_Load.place(x=3, y=80)
winButton_Run = Button(text='Run Code', width=16, height=1, command=WinShell)
winButton_Run.place(x=3, y=110)
winText2 = Label(text="Code Blocks")
winButton_Shell = Button(text='Shell', width=16, height=1, command=CodeBL_Shell)
winButton_Shell.place(x=3, y=170)
winText2.place(x=30, y=140)
#place Text
winTextBox = Text()
winTextBox.place(x=128, y=21)
window.mainloop()
#-------------------

