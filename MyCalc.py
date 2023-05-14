#!/bin/python3

import PySimpleGUI as sg

Ans = 0
Ans_ok = ''
calnum1 = 0
calc_list = []
calc_way = []
Ans_storage = []
ispoint = False

layout = [
    [sg.MenuBar([['&File',['New','---','&Quit']],['&Edit',['menu1','menu2']]], key='-menubar-')],
    [sg.Text(Ans_ok, size=(20, 2), justification='center', key='-input-')],
    [sg.Submit(button_text='1', size=(4, 2), key='1'), sg.Submit(button_text='2', size=(4, 2), key='2'), sg.Submit(button_text='3', size=(4, 2), key='3'), sg.Submit(button_text='DEL', size=(4, 2), key='-del-'), sg.Submit(button_text='AC', size=(4, 2), key='-allclear-')],
    [sg.Submit(button_text='4', size=(4, 2), key='4'), sg.Submit(button_text='5', size=(4, 2), key='5'), sg.Submit(button_text='6', size=(4, 2), key='6'), sg.Submit(button_text='+', size=(4, 2), key='-plus-'), sg.Submit(button_text='-', size=(4, 2), key='-minus-')],
    [sg.Submit(button_text='7', size=(4, 2), key='7'), sg.Submit(button_text='8', size=(4, 2), key='8'), sg.Submit(button_text='9', size=(4, 2), key='9'), sg.Submit(button_text='×', size=(4, 2), key='-multi-'), sg.Submit(button_text='÷', size=(4, 2), key='-div-')],
    [sg.Submit(button_text='0', size=(4, 2), key='0'), sg.Submit(button_text='.', size=(4, 2), key='.'), sg.Submit(button_text='×10^x', size=(4, 2), key='-exp10-'), sg.Submit(button_text='Ans', size=(4, 2), key='-saveans-'), sg.Submit(button_text='=', size=(4, 2), key='equal')],
    [sg.Text(Ans, size=(20, 2), justification='center')],
    [sg.Text('This calc was made by MBTomo.', size=(20, 2), justification='center')]
]

window = sg.Window('Test Program1', layout, resizable=True)

def num_pushed(): #ボタンが押されたときに画面表示を更新

    window['-input-'].update(Ans_ok)

def restart1(restart1=0, restart2=[], restart3=[]):
    restart1 = 0
    restart2 = []
    restart3 = []
    return restart1, restart2, restart3

def calc_symbol(): #四則演算の記号を識別
    calc_symbol_num = 0
    if event == '-plus-':
        calc_symbol_num = 1
        print("plus")
    if event == '-minus-':
        calc_symbol_num = 2
        print("minus")
    if event == '-multi-':
        calc_symbol_num = 3
        print("multiple")
    if event == '-div-':
        calc_symbol_num = 4
        print("divide")
    
    return calc_symbol_num #四則演算に割り与えられた数値をreturn

def calc_exe(cl, cw): #計算実行
    j = 0 #初期化
    if len(cl) == 0: #何も入力されていないとき
        num_result = None
    else: #入力されているとき
        num_result = cl[j] #num_resultに最初の値を入れる
    for i in cw:
        if len(cl) == 0: #何も入力されていないとき、終了
            break
        if cw[j] == 1:
            num_result = num_result + cl[j+1]
        elif cw[j] == 2:
            num_result = num_result - cl[j+1]
        elif cw[j] == 3:
            num_result = num_result * cl[j+1]
        elif cw[j] == 4:
            num_result = num_result / cl[j+1]
        j = j+1

    return num_result #値を返却

is_num_input = False
while True: #メインループ
    event, values = window.read()

    if calc_symbol() != 0:
        calnum1 = calc_symbol()
    
    if event is None or values['-menubar-'] == 'Quit':
        print('exit')
        if Ans_ok != '':
            calc_list.append(float(Ans_ok))
        break

    if event == '-allclear-':
        calnum1, calc_list, calc_way = restart1(calnum1, calc_list, calc_way)
        Ans_ok = ''
        window['-input-'].update(Ans_ok)
        is_num_input = False

    if event.isdigit() == True:
        if calnum1 != 0 and is_num_input == True:
            calc_way.append(calnum1)
            calc_list.append(float(Ans_ok))
            ispoint = False
            Ans_ok = ''
            calnum1 = 0
        elif is_num_input == False:
            calnum1 = 0
            is_num_input = True
        Ans_ok = Ans_ok + event
        num_pushed()
    elif event == '.' and ispoint == False and is_num_input == True:
        Ans_ok = Ans_ok + event
        num_pushed()
        ispoint = True #小数点が入力された

    if event == 'equal':
        if len(calc_list) == 0:
            continue
        calc_list.append(float(Ans_ok))
        anstemp1 = calc_exe(calc_list, calc_way)
        Ans_ok = str(anstemp1) #表示用の数値をstrに変換して代入
        Ans_storage.append(anstemp1) #答えの配列に格納
        window['-input-'].update(Ans_ok) #アップデートして表示
        #terminal
        print(calc_way)
        print(calc_list)
        print(calc_exe(calc_list, calc_way))
        #初期化
        calnum1, calc_list, calc_way = restart1(calnum1, calc_list, calc_way)
        '''
        calnum1 = 0
        calc_list = []
        calc_way = []
        '''
        #break
print(calc_way)
print(calc_list)
print(calc_exe(calc_list, calc_way))
print(Ans_storage)
window.close()