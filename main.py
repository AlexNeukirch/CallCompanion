#!/usr/bin/env Python3
# coding: utf-8

import PySimpleGUI as sg
import datetime
import os

x = datetime.datetime.now()
callAccepted = 0
callRejected = 0
callSummary = 0
callPolish = 0
callGerman = 0
callEnglish = 0
lastCall = ''
doubleUndoPrevention = 0
onTop = True

sg.ChangeLookAndFeel('Dark')

# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Undo'], ],
            ['Help', 'About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Call Companion alpha alphy', size=(30, 1), justification='center', font=("Helvetica", 25),
             relief=sg.RELIEF_RIDGE)],
    [sg.Text('_' * 80)],
    [sg.Text('Odebrane/Suma'), sg.Text('odrzucone'),
     sg.Text('PL', size=(3, 1), justification='center', font=("Helvetica", 25)),
     sg.Text('DE', size=(3, 1), justification='center', font=("Helvetica", 25)),
     sg.Text('EN', size=(3, 1), justification='center', font=("Helvetica", 25))],
    [sg.Text('0/0', size=(5, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE, key='jeden'),
     sg.Text('0', size=(3, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE, key='dwa'),
     sg.Text('0', size=(3, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE,
             key='callPolishKey'),
     sg.Text('0', size=(3, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE,
             key='callGermanKey'),
     sg.Text('0', size=(3, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE,
             key='callEnglishKey')],
    [sg.ProgressBar(callSummary, orientation='h', size=(25, 20), key='progbar'),
     sg.Text('0%   ', key='trzy'),
     sg.Text('Last Call:     ', key='lastCall')],
    [sg.Text('_' * 80)],
    [sg.Button('Odebrany Call PL'),
     sg.Button('Odebrany Call DE'),
     sg.Button('Odebrany Call EN'), sg.Button('Odrzucony Call'),
     sg.Text('', size=(10, 2), font=('Helvetica', 12), justification='center', key='_OUTPUT_')],
    [sg.Text('_' * 80)],
    [sg.Button('Exit'),
     # sg.Button('Save & Exit'), sg.Button('onTop'), sg.Text(str(onTop) + '  ', key='cztery')
     ]
]

layoutAbout = [[sg.Text('CallCompanion alpha')],
               [sg.Text('Statystyki pracy.')],
               [sg.Button('Powrót')]
               ]

layoutUndo = [[sg.Text('Error')],
              [sg.Text('You can undo only once')],
              [sg.Button('Powrót')]
              ]

window = sg.Window('CallCompanion', layout, default_element_size=(40, 1), grab_anywhere=onTop, keep_on_top=onTop,
                   no_titlebar=onTop)
# event, values = window.read()


if not os.path.exists('logs'):
    os.makedirs('logs')
file = open(x.strftime("logs/%Y-%m-%d.txt"), "w")
file.close()

timer_running, counter = True, 0

while True:
    event, values = window.read(timeout=10)

    if event == None or event == "Exit":
        break

    if event == 'About...':
        windowAbout = sg.Window('About...', layoutAbout, grab_anywhere=True)
        event, values = windowAbout.read()
        if event == 'Powrót':
            windowAbout.close()

    if event == "Odebrany Call PL":
        callAccepted += 1
        callSummary += 1
        callPolish += 1
        lastCall = 'PL'
        doubleUndoPrevention = 1
        procent = int(callAccepted) / int(callSummary)
        window['jeden'](str(callAccepted) + '/' + str(callSummary))
        window['progbar'].update_bar(callAccepted, callSummary)
        window['trzy'](str(int(procent * 100)) + '%')
        window['callPolishKey'](callPolish)
        window['lastCall']('Last Call: ' + lastCall)
        f = open(x.strftime("logs/%Y-%m-%d.txt"), "a+")
        f.write(str(callSummary) + '. ' + '%s ' % datetime.datetime.now())
        f.write('PolishCallAccepted\n')
        f.close()
        timer_running = 1
        timer_running = 0
        counter = 0
        timer_running = 1

    if event == "Odebrany Call DE":
        callAccepted += 1
        callSummary += 1
        callGerman += 1
        lastCall = 'DE'
        doubleUndoPrevention = 1
        procent = int(callAccepted) / int(callSummary)
        window['jeden'](str(callAccepted) + '/' + str(callSummary))
        window['progbar'].update_bar(callAccepted, callSummary)
        window['trzy'](str(int(procent * 100)) + '%')
        window['callGermanKey'](callGerman)
        window['lastCall']('Last Call: ' + lastCall)
        f = open(x.strftime("logs/%Y-%m-%d.txt"), "a+")
        f.write(str(callSummary) + '. ' + '%s ' % datetime.datetime.now())
        f.write('GermanCallAccepted\n')
        f.close()
        timer_running = 1
        timer_running = 0
        counter = 0
        timer_running = 1

    if event == "Odebrany Call EN":
        callAccepted += 1
        callSummary += 1
        callEnglish += 1
        lastCall = 'EN'
        doubleUndoPrevention = 1
        procent = int(callAccepted) / int(callSummary)
        window['jeden'](str(callAccepted) + '/' + str(callSummary))
        window['progbar'].update_bar(callAccepted, callSummary)
        window['trzy'](str(int(procent * 100)) + '%')
        window['callEnglishKey'](callEnglish)
        window['lastCall']('Last Call: ' + lastCall)
        f = open(x.strftime("logs/%Y-%m-%d.txt"), "a+")
        f.write(str(callSummary) + '. ' + '%s ' % datetime.datetime.now())
        f.write('EnglishCallAccepted\n')
        f.close()
        timer_running = 1
        timer_running = 0
        counter = 0
        timer_running = 1

    if event == "Odrzucony Call":
        callSummary += 1
        callRejected += 1
        lastCall = "CR"  # CR - Call Rejected
        doubleUndoPrevention = 1
        procent = callAccepted / callSummary
        window['jeden'](str(callAccepted) + '/' + str(callSummary))
        window['dwa'](callRejected)
        window['progbar'].update_bar(callAccepted, callSummary)
        window['trzy'](str(int(procent * 100)) + '%')
        f = open(x.strftime("logs/%Y-%m-%d.txt"), "a+")
        f.write(str(callSummary) + '. ' + '%s ' % datetime.datetime.now())
        f.write('callRejected\n')
        f.close()
        timer_running = 0
        counter = 0
        timer_running = 1

    if timer_running:
        window['_OUTPUT_'].update(
            '{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
        counter += 1

    if event == "Undo":
        if doubleUndoPrevention == 0:
            windowUndo = sg.Window('About...', layoutUndo, grab_anywhere=True)
            event, values = windowUndo.read()
            if event == 'Powrót':
                windowUndo.close()

        if lastCall == 'PL' and doubleUndoPrevention == 1:
            callPolish -= 1
            callSummary -= 1
            callAccepted -= 1
            doubleUndoPrevention = 0
            procent = int(callAccepted) / int(callSummary)
            window['jeden'](str(callAccepted) + '/' + str(callSummary))
            window['progbar'].update_bar(callAccepted, callSummary)
            window['trzy'](str(int(procent * 100)) + '%')
            window['callPolishKey'](callPolish)
            readFile = open(x.strftime("logs/%Y-%m-%d.txt"))
            lines = readFile.readlines()
            readFile.close()
            f = open(x.strftime("logs/%Y-%m-%d.txt"), 'w')
            f.writelines([item for item in lines[:-1]])
            f.close()

        if lastCall == 'DE' and doubleUndoPrevention == 1:
            callGerman -= 1
            callSummary -= 1
            callAccepted -= 1
            doubleUndoPrevention = 0
            procent = int(callAccepted) / int(callSummary)
            window['jeden'](str(callAccepted) + '/' + str(callSummary))
            window['progbar'].update_bar(callAccepted, callSummary)
            window['trzy'](str(int(procent * 100)) + '%')
            window['callGermanKey'](callGerman)
            readFile = open(x.strftime("logs/%Y-%m-%d.txt"))
            lines = readFile.readlines()
            readFile.close()
            f = open(x.strftime("logs/%Y-%m-%d.txt"), 'w')
            f.writelines([item for item in lines[:-1]])
            f.close()

        if lastCall == 'EN' and doubleUndoPrevention == 1:
            callEnglish -= 1
            callSummary -= 1
            callAccepted -= 1
            doubleUndoPrevention = 0
            procent = int(callAccepted) / int(callSummary)
            window['jeden'](str(callAccepted) + '/' + str(callSummary))
            window['progbar'].update_bar(callAccepted, callSummary)
            window['trzy'](str(int(procent * 100)) + '%')
            window['callEnglishKey'](callEnglish)
            readFile = open(x.strftime("logs/%Y-%m-%d.txt"))
            lines = readFile.readlines()
            readFile.close()
            f = open(x.strftime("logs/%Y-%m-%d.txt"), 'w')
            f.writelines([item for item in lines[:-1]])
            f.close()

        if lastCall == 'CR' and doubleUndoPrevention == 1:
            callRejected -= 1
            callSummary -= 1
            doubleUndoPrevention = 0
            procent = int(callAccepted) / int(callSummary)
            window['jeden'](str(callAccepted) + '/' + str(callSummary))
            window['progbar'].update_bar(callAccepted, callSummary)
            window['trzy'](str(int(procent * 100)) + '%')
            window['dwa'](callRejected)
            readFile = open(x.strftime("logs/%Y-%m-%d.txt"))
            lines = readFile.readlines()
            readFile.close()
            f = open(x.strftime("logs/%Y-%m-%d.txt"), 'w')
            f.writelines([item for item in lines[:-1]])
            f.close()

    # if event == "onTop":
    #     if onTop == False:
    #         onTop = True
    #         window['cztery']('True')
    #     else:
    #         onTop = False
    #         window['cztery']('False')

window.close()
# del window
