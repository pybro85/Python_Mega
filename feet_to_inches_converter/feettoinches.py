import PySimpleGUI as sg
from feettoinches_function import convert

sg.theme("LightBrown")

feet_label = sg.Text("Enter feet: ")
feet_input = sg.InputText(tooltip="Enter feet", key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.InputText(tooltip="Enter inches", key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")

exit_button = sg.Button("Exit")

col1 = sg.Column([[feet_label], [inches_label]])
col2 = sg.Column([[feet_input], [inches_input]])


window = sg.Window(
    "Converter", layout = [
        [col1, col2],  
        [convert_button, exit_button, output_label],
        ]
)

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case "Convert":
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])    
                result = convert(feet, inches)
                window["output"].update(value = f"{result} m", text_color = "Black")
            except ValueError:
                sg.Popup("Please provide feet AND inches")        
window.close()    



# import PySimpleGUI as sg
 
 
# def km_to_miles(km):
#     return km / 1.6
 
 
# label = sg.Text("Kilometers: ")
# input_box = sg.InputText(tooltip="Enter todo", key="kms")
# miles_button = sg.Button("Convert")
 
# output = sg.Text(key="output")
 
 
# window = sg.Window('Km to Miles Converter',
#                    layout=[[label, input_box], [miles_button, output]],
#                    font=('Helvetica', 20))
 
# while True:
#     event, values = window.read()
#     match event:
#         case "Convert":
#             km = float(values["kms"])
#             result = km_to_miles(km)
#             window['output'].update(value=result)
#         case sg.WIN_CLOSED:
#             break
 
# window.close()