import PySimpleGUI as pg
import converter

message1 = pg.Text("Enter Feet")
input1 = pg.Input(key="feet_input")
input2 = pg.Input(key="inches_input")
message2 = pg.Text("Enter inches")
c_button = pg.Button("Convert")
output_text = pg.Text(key='output')

window = pg.Window('Converter',
                   layout=[[message1, input1],
                           [message2, input2],
                           [c_button, output_text]],
                   font=('Helvetica', 20))


while True:
    events, values = window.read()
    feet = float(values["feet_input"])
    inches = float(values["inches_input"])
    c_value = str(round(converter.convert(feet, inches),3))

    window['output'].update(c_value + ' m')

window.close()
