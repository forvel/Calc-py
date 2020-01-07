from tkinter import *
def addText():
    
    pass
def calc(op):
    num1 = int(entNumber1.get())
    num2 = int(entNumber2.get())
    if op == "+":
        res = num1+num2 
        entResult.insert(0,str(res))
    #elif op = "-":
        
    
root = Tk()

root.title("Калькулятор")
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(4, weight=1)

lblNumber1 = Label(root, text="Число 1", width = 10, anchor = W)
lblNumber1.grid(row = 0, column = 0, columnspan = 2, sticky = W)
entNumber1 = Entry(root, width = 13, justify = RIGHT)
entNumber1.grid(row = 0, column = 2, columnspan = 2, sticky = E, padx=2)

lblNumber2 = Label(root, text="Число 2", width = 10, anchor = W)
lblNumber2.grid(row = 1, column = 0, columnspan = 2, sticky = W)
entNumber2 = Entry(root, width = 13, justify = RIGHT)
entNumber2.grid(row = 1, column = 2, columnspan = 2, sticky = E, padx=2)

lblResult = Label(root, text="Результат", width = 10, anchor = W)
lblResult.grid(row = 2, column = 0, columnspan = 2, sticky = W)
entResult = Entry(root, width = 13, justify = RIGHT)
entResult.grid(row = 2, column = 2, columnspan = 2, sticky = E, padx=2)

#stack = []
#stack.append(something) - положить элемент на вершину
#sign = stack.pop() - вернуть верхний элемент


btnList =   (
            ('7','8','9','/'),
            ('4','5','6','*'),
            ('1','2','3','-'),
            ('0',',','=','+')
            )
for i in range(4):
    for j in range(4):
        
        if j == 3:
            btn = Button (root,text = btnList[i][j],width = 5, command = lambda x=btnList[i][j]: calc(x))
            btn.grid(row = i+3, column = j,padx=2,pady=2)
            #btn.bind(,)
        else:
            btn = Button (root,text = btnList[i][j],width = 5, command = addText)
            btn.grid(row = i+3, column = j,padx=2,pady=2)
root.mainloop()

