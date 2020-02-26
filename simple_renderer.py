import subprocess
import PySimpleGUI as sg
import os

sg.theme('Dark Blue 3')

try:
    f= open("render.bat","r")
    first_line = f.readline()
    directory_blender = first_line[3:]
    
except IOError:
    directory_blender = "C:\Program Files\Blender Foundation\Blender 2.82"
    print("New User")


layout = [  [sg.Text('Simple Renderer v0.1-alpha ')],
            [sg.Text('Path to folder with blender.exe: '),sg.InputText(directory_blender)],
            [sg.Text('1.'), sg.InputText(),sg.Radio('Frame [1]', "RADIO1", default=True, size=(10,1)), sg.Radio('Anim [Full]', "RADIO1"),sg.Text('',key='0')],
            [sg.Text('2.'), sg.InputText(),sg.Radio('Frame [1]', "RADIO2", default=True, size=(10,1)), sg.Radio('Anim [Full]', "RADIO2"),sg.Text('',key='1')],
            [sg.Text('3.'), sg.InputText(),sg.Radio('Frame [1]', "RADIO3", default=True, size=(10,1)), sg.Radio('Anim [Full]', "RADIO3"),sg.Text('',key='2')],
            [sg.Text('4.'), sg.InputText(),sg.Radio('Frame [1]', "RADIO4", default=True, size=(10,1)), sg.Radio('Anim [Full]', "RADIO4"),sg.Text('',key='3')],
            [sg.Text('5.'), sg.InputText(),sg.Radio('Frame [1]', "RADIO5", default=True, size=(10,1)), sg.Radio('Anim [Full]', "RADIO5"),sg.Text('',key='4')],
            [sg.Text('6.'), sg.InputText(),sg.Radio('Frame [1]', "RADIO6", default=True, size=(10,1)), sg.Radio('Anim [Full]', "RADIO6"),sg.Text('',key='5')],
            [sg.Button('Render'), sg.Button('Exit')]]


window = sg.Window('Simple Renderer', layout, no_titlebar=True, grab_anywhere=True,keep_on_top=True)
while True:
    event, values = window.read()

    if event in ('Render'):
        for x in range(6):
            f= open("render.bat","w+")
            f.write("cd ")
        
        
            f.write(values[0])
            f.write("\n")
            f.write("blender -b ")

            if not values[1+3*x]:
                print("Empty"+str(x))
            else:
                
                f.write('"')
                f.write(str(values[1+3*x]))
                f.write('"')
                f.write(' -o "//')
                f.write(os.path.splitext(os.path.basename(values[1+3*x]))[0])
                f.write('_"')
                if values[2+3*x] == True:
                    f.write(" -f 1 ")
                if values[3+3*x] == True:
                    f.write(" -a ")
        
                f.close()
                subprocess.call([r'render.bat'])
                window[str(x)].update('✓')
                print("Finished: " + str(x))

        
    if event in (None, 'Exit'):
        break

window.close()
