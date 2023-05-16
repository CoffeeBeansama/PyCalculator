import PySimpleGUI as sg


_buttonSize = (5,2)

_windowSize = (250,350)
sg.theme("black")
show_hidden = False


def CreateButton(content,key):
    return sg.Button(content,size=_buttonSize,key=key)

layout = [
    [sg.Push(),sg.Text("Enter a value",text_color="white",pad=(1,30),key="output")],
    [CreateButton("CE","Clear all"),CreateButton("C","Erase"),CreateButton("%","percent"),CreateButton("/","/")],
    [CreateButton("7","7"),CreateButton("8","8"),CreateButton("9","9"),CreateButton("*","*")],
    [CreateButton("4","4"),CreateButton("5","5"),CreateButton("6","6"),CreateButton("-","-")],
    [CreateButton("1","1"),CreateButton("2","2"),CreateButton("3","3"),CreateButton("+","+")],
    [CreateButton("0","0"),CreateButton(".","."),CreateButton("=","equals")]
]


window = sg.Window("test",layout,size=_windowSize)

inputed_numbers = []
full_operation = []
result = 0

while True:

    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event in ["1","2","3","4","5","6","7","8","9"]:
        inputed_numbers.append(event)
        stringnumber = "".join(inputed_numbers)
        window["output"].Update(stringnumber)
    if event in["/","*","-","+"]:
        full_operation.append("".join(inputed_numbers))
        inputed_numbers = []
        full_operation.append(event)
        window["output"].update("")
    if event in "equals":
        full_operation.append("".join(inputed_numbers))
        result = eval("".join(full_operation))

        window["output"].update(result)

    if event in "Clear all":
        inputed_numbers.clear()
        full_operation.clear()
        window["output"].update("")

   




