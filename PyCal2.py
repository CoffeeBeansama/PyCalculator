from customtkinter import *

app = CTk()
set_appearance_mode("dark")


input_number = []
fullOperation = []


def NumberClicked(number):

    numberLenght = len(input_number)

    if numberLenght < 9:
        input_number.append(number)
        string_number = "".join(input_number)
        mainText.configure(text=string_number)
    else:
        string_number = "".join(input_number)
        mainText.configure(text=string_number)

def OperationClicked(operator):
    fullOperation.append( "".join(input_number))
    input_number.clear()
    fullOperation.append(operator)
    mainText.configure(text=operator)

def GetTotal(operation):
    fullOperation.append("".join(input_number))
    total = eval("".join(fullOperation))
    mainText.configure(text=total)



def ClearAll(space):
    input_number.clear()
    fullOperation.clear()
    return mainText.configure(text=space)

padX = 4
pad_y = 6
app.geometry("320x430")

mainText = CTkLabel(app,text=" ",font=("Arial",50))
mainText.grid(row=0,column=0,padx=4,pady=6)
mainText.grid_configure(columnspan=1000)


Clear = CTkButton(app,text="CE",width=70,height=70,command= lambda : ClearAll(" "))
Clear.grid(row=1,column=0,padx=padX,pady=pad_y)

Erase = CTkButton(app,text="C",width=70,height=70)
Erase.grid(row=1, column=1, padx=padX, pady=pad_y)

Divide = CTkButton(app,text="/",width=70,height=70,command= lambda:OperationClicked("/"))
Divide.grid(row=1, column=2, padx=padX, pady=pad_y)

Equals = CTkButton(app,text="=",width=70,height=70,command= lambda : GetTotal(fullOperation))
Equals.grid(row=1, column=3, padx=padX, pady=pad_y)

seven = CTkButton(app,text="7",width=70,height=70,command= lambda:NumberClicked("7"))
seven.grid(row=2, column=0, padx=padX, pady=pad_y)

eight = CTkButton(app,text="8",width=70,height=70,command= lambda:NumberClicked("8"))
eight.grid(row=2, column=1, padx=padX, pady=pad_y)

nine = CTkButton(app,text="9",width=70,height=70,command= lambda:NumberClicked("9"))
nine.grid(row=2, column=2, padx=padX, pady=pad_y)

multiply = CTkButton(app,text="*",width=70,height=70,command= lambda:OperationClicked("*"))
multiply.grid(row=2, column=3, padx=padX, pady=pad_y)

four = CTkButton(app,text="4",width=70,height=70,command= lambda:NumberClicked("4"))
four.grid(row=3, column=0, padx=5, pady=pad_y)

five = CTkButton(app,text="5",width=70,height=70,command= lambda:NumberClicked("5"))
five.grid(row=3, column=1, padx=padX, pady=pad_y)

six = CTkButton(app,text="6",width=70,height=70,command= lambda:NumberClicked("6"))
six.grid(row=3, column=2, padx=padX, pady=pad_y)

minus = CTkButton(app,text="-",width=70,height=70,command= lambda:OperationClicked("-"))
minus.grid(row=3, column=3, padx=padX, pady=pad_y)

zero = CTkButton(app,text="0",width=70,height=70,command= lambda:NumberClicked("0"))
zero.grid(row=4, column=0, padx=padX, pady=pad_y)

one = CTkButton(app,text="1",width=70,height=70,command= lambda:NumberClicked("1"))
one.grid(row=4, column=1, padx=padX, pady=pad_y)

two = CTkButton(app,text="2",width=70,height=70,command= lambda:NumberClicked("2"))
two.grid(row=4, column=2, padx=padX, pady=pad_y)

plus = CTkButton(app,text="+",width=70,height=70,command= lambda:OperationClicked("+"))
plus.grid(row=4, column=3, padx=padX, pady=pad_y)


app.mainloop()