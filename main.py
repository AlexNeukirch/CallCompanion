#!/usr/bin/env Python3
import PySimpleGUI as sg
import datetime

x = datetime.datetime.now()
callAccepted = 0
callRejected = 0
callSummary = 0
onTop = True


sg.ChangeLookAndFeel('Dark')

# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Call Companion alpha aplhy', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('_'  * 80)],
    [sg.Text('0', size=(3, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE, key='jeden'), sg.Text('0', size=(3, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE, key='dwa')],
    [sg.ProgressBar(callSummary, orientation='h', size=(20, 20), key='progbar'), sg.Text('0%   ', key='trzy')],
    [sg.Text('_'  * 80)],
    [sg.Text('Nazwa Hotkey')],
    [sg.Button('Odebrany Call', tooltip='przyciśnij, jeśli odebrałeś calla'), sg.Button('Odrzucony Call')],
    [sg.Text('_'  * 80)],
    [sg.Button('Exit'), sg.Button('Save & Exit'), sg.Button('onTop'), sg.Text(str(onTop) + '  ', key='cztery')]
]

layoutAbout = [[sg.Text('CallCompanion alpha')],
                 [sg.Text('Statystyki pracy.')],
                 [sg.Button('Powrót')]
]


window = sg.Window('CallCompanion', layout, default_element_size=(40, 1), grab_anywhere=True, keep_on_top = onTop, no_titlebar=True)
#event, values = window.read()

file = open(x.strftime("%Y-%m-%d.txt"),"w")
file.close()

while True:
    event, values = window.read()

    if event == None or event == "Exit":
        break

    if event == 'About...':
        windowAbout = sg.Window('About...', layoutAbout, grab_anywhere=True)
        event, values = windowAbout.read()
        if event == 'Powrót':
            windowAbout.close()

    if event == "Odebrany Call":
        callAccepted += 1
        callSummary += 1
        procent = int(callAccepted) / int(callSummary)
        window['jeden'](callAccepted)
        window['progbar'].update_bar(callAccepted, callSummary)
        window['trzy'](str(int(procent * 100)) + '%')
        f=open(x.strftime("%Y-%m-%d.txt"), "a+")
        f.write(str(callSummary) + '. ' + '%s ' %datetime.datetime.now())
        f.write('callAccepted\n')
        f.close()
                
    if event == "Odrzucony Call":
        callSummary += 1
        callRejected += 1
        procent = callAccepted / callSummary
        window['dwa'](callRejected)
        window['progbar'].update_bar(callAccepted, callSummary)
        window['trzy'](str(int(procent * 100)) + '%')
        f=open(x.strftime("%Y-%m-%d.txt"), "a+")
        f.write(str(callSummary) + '. '  + '%s ' %datetime.datetime.now())
        f.write('callRejected\n')
        f.close()

    if event == "onTop":
        if onTop == False:
            onTop = True
            window['cztery']('True')
        else:
            onTop = False
            window['cztery']('False')


window.close()
#del window
