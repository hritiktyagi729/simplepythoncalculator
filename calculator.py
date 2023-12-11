from tkinter import *
from subprocess import call
import math
root = Tk()
#button_9 = Button(label_key,text='9',height=3,width=5,font=('Helvetica','12'))
#button_9.grid(row=0,column=0)
class Calculator:
    def click_button(self,numbers):
        global operator
        global var
        self.operator = self.operator + str(numbers)
        self.var.set(self.operator)

    def clear(self):
        self.entry.delete(0,END)
        self.operator =""
        #self.extra=""

    ''' def delete(self):
        self.operator = str(self.entry.delete(len(self.entry.get())-1))
    '''

    def evaluate_expression(expression):
        # Define a regex pattern to match functions like sin(90)
        pattern = r'([a-z]+)\((\d+)\)'

        # Define a function to replace the matched expressions with their evaluated values
        def repl(match):
            func, arg = match.groups()
            if func in ('sin', 'cos', 'tan'):
                # Convert the angle to radians for trigonometric functions
                return str(math.radians(float(arg)))
            elif func == 'sqrt':
                return str(math.sqrt(float(arg)))
            else:
                return match.group()

    def evaluate(self):
        try:
            # Get the expression from the entry
            expression = self.entry.get()

            # Replace trigonometric functions with radians conversion
            expression = expression.replace("sin(", "math.sin(math.radians(")
            expression = expression.replace("cos(", "math.cos(math.radians(")
            expression = expression.replace("tan(", "math.tan(math.radians(")

            # Attempt to evaluate the expression using eval
            result = eval(expression, {"__builtins__": None}, {"math": math})

            # If the evaluation is successful, update the display
            self.var.set(result)
            self.operator = str(result)
        except Exception as e:
            # If there's an error in the evaluation, handle it
            self.var.set("Error")
            self.operator = ""
    
#    def evaluate(self):
#            
#        self.answer =eval(self.entry.get())
#        self.var.set(self.answer)
#        self.operator = str(self.answer)


    def __init__(self,master):

        self.operator = ""        
        self.var = StringVar()
        frame_s = Frame(master, height=400, width=90 )
        frame_s.pack(side=TOP, fill=BOTH, expand=True)
        self.entry = Entry(frame_s,textvariable=self.var,bg='grey',width=45,bd=20,insertwidth=4,justify='right',font=('arial',10,'bold'))
        self.entry.pack()
        self.t = Text(self.entry,height=40)
        self.extra = ""



        label_key = Label(root, height=30, width=45,bd=10,bg='white')
        label_key.pack(side=RIGHT, fill=BOTH, expand=True)

        label_fkey = Label(root, height=15, width=15, bg='white')
        label_fkey.pack(fill=BOTH, expand=True)

        label_7 = Label(label_key, bg='black')
        label_7.grid(row=0, column=0)
        button_7 = Button(label_7, text='1', font=('Helvetica', '16'),command= lambda : self.click_button(1),bg='cornsilk2',fg='black')
        button_7.pack()

        label_8 = Label(label_key, bg='black')
        label_8.grid(row=0, column=1, padx=20)
        button_8 = Button(label_8, text='2', font=('Helvetica', '16'),command= lambda: self.click_button(2),bg='cornsilk2',fg='black')
        button_8.pack()

        label_9 = Label(label_key, bg='black')
        label_9.grid(row=0, column=2, padx=10)
        button_9 = Button(label_9, text='3', font=('Helvetica', '16'),command= lambda: self.click_button(3),bg='cornsilk2',fg='black')
        button_9.pack()

        label_4 = Label(label_key, bg='black')
        label_4.grid(row=1, column=0, padx=10, pady=10)
        button_4 = Button(label_4, text='4', font=('Helvetica', '16'),command= lambda: self.click_button(4),bg='cornsilk2',fg='black')
        button_4.pack()

        label_5 = Label(label_key, bg='black')
        label_5.grid(row=1, column=1, padx=10, pady=10)
        button_5 = Button(label_5, text='5', font=('Helvetica', '16'),command= lambda: self.click_button(5),bg='cornsilk2',fg='black')
        button_5.pack()

        label_6 = Label(label_key, bg='black')
        label_6.grid(row=1, column=2, padx=10, pady=10)
        button_6 = Button(label_6, text='6', font=('Helvetica', '16'),command= lambda: self.click_button(6),bg='cornsilk2',fg='black')
        button_6.pack()

        label_1 = Label(label_key, bg='black')
        label_1.grid(row=2, column=0, padx=10)
        button_1 = Button(label_1, text='7', font=('Helvetica', '16'),command= lambda: self.click_button(7),bg='cornsilk2',fg='black')
        button_1.pack()

        label_2 = Label(label_key, bg='black')
        label_2.grid(row=2, column=1, padx=10)
        button_2 = Button(label_2, text='8', font=('Helvetica', '16'),command= lambda: self.click_button(8),bg='cornsilk2',fg='black')
        button_2.pack()

        label_3 = Label(label_key, bg='black')
        label_3.grid(row=2, column=2, padx=10)
        button_3 = Button(label_3, text='9', font=('Helvetica', '16'),command= lambda: self.click_button(9),bg='cornsilk2',fg='black')
        button_3.pack()

        label_0 = Label(label_key, bg='black')
        label_0.grid(row=3, column=0, padx=10, pady=10)
        button_0 = Button(label_0, text='0', font=('Helvetica', '16'),command= lambda: self.click_button(0),bg='cornsilk2',fg='black')
        button_0.pack()

        label_deci = Label(label_key, bg='black')
        label_deci.grid(row=3, column=1, padx=10, pady=10)
        button_deci = Button(label_deci, text='.', font=('Helvetica', '16'),command= lambda: self.click_button('.'),bg='cornsilk2',fg='black')
        button_deci.pack()

        label_equal = Label(label_key, bg='black')
        label_equal.grid(row=3, column=2, padx=10, pady=10)
        button_equal = Button(label_equal, text='=', font=('Helvetica', '16'),command= self.evaluate,bg='cornsilk2',fg='black')
        button_equal.pack()

        label_C = Label(label_fkey, bg='black')
        label_C.grid(row=0, column=0,columnspan=2)
        button_C = Button(label_C, text='C', font=('Helvetica', '16'), height=1, width=10,command=  self.clear,bg='cornsilk2',fg='black')
        button_C.pack(side=LEFT)

        '''label_del = Label(label_fkey, bg ='cornsilk2')
        label_del.grid(row=0,column=1,sticky=E)
        button_del = Button(label_del, text='del', font=('Helvetica', '16'),bd=3, height=1, width=3,command=  self.delete)
        button_del.pack()'''
       
        call(["python3", "PyGUI.py"])
        label_sub = Label(label_fkey, bg='black')
        label_sub.grid(row=1, column=0, sticky=W, pady=10)
        button_sub = Button(label_sub, text='-', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('-'),bg='cornsilk2',fg='black')
        button_sub.pack(side=LEFT)

        label_mul = Label(label_fkey, bg='black')
        label_mul.grid(row=1, column=1, sticky=E)
        button_mul = Button(label_mul, text='x', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('*'),bg='cornsilk2',fg='black')
        button_mul.pack()

        label_div = Label(label_fkey, bg='black')
        label_div.grid(row=2, column=0, sticky=W)
        button_div = Button(label_div, text='/', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('/'),bg='cornsilk2',fg='black')
        button_div.pack()

        label_add = Label(label_fkey, bg='black')
        label_add.grid(row=2, column=1, sticky=E)
        button_add = Button(label_add, text='+', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('+'),bg='cornsilk2',fg='black')
        button_add.pack()

        label_lbrace = Label(label_fkey, bg='black')
        label_lbrace.grid(row=3,column=0,sticky=W,pady=10)
        button_lbrace = Button(label_lbrace,text='(', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('('),bg='cornsilk2',fg='black')
        button_lbrace.pack()

        label_rbrace = Label(label_fkey, bg='black')
        label_rbrace.grid(row=3, column=1, sticky=E, pady=10)
        button_rbrace = Button(label_rbrace, text=')', font=('Helvetica', '16'), height=1, width=3, command=lambda: self.click_button(')'),bg='cornsilk2',fg='black')
        button_rbrace.pack()

        label_pow = Label(label_fkey, bg='black')
        label_pow.grid(row=0, column=3, sticky=W, padx=10, pady=10)
        button_pow = Button(label_pow, text='pow', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('**'),bg='cornsilk2',fg='black')
        button_pow.pack()
 
        label_exp = Label(label_fkey, bg='black')
        label_exp.grid(row=1, column=3, sticky=W, padx=10, pady=10)
        button_exp = Button(label_exp, text='exp', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('^'),bg='cornsilk2',fg='black')
        button_exp.pack()

        label_sin = Label(label_fkey, bg='black')
        label_sin.grid(row=2, column=3, sticky=W, padx=10)
        button_sin = Button(label_sin, text='sin', font=('Helvetica', '16'), height=1, width=3,
        command=lambda: self.click_button('sin'), bg='cornsilk2',fg='black')
        button_sin.pack()
        label_cos = Label(label_fkey, bg='black')
        label_cos.grid(row=3, column=3, sticky=W,padx=10, pady=10)
        button_add = Button(label_cos, text='cos', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('cos'),bg='cornsilk2',fg='black')
        button_add.pack()
        label_tan = Label(label_fkey, bg='black')
        label_tan.grid(row=4, column=3, sticky=W, padx=10)
        button_add = Button(label_tan, text='tan', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('tan'),bg='cornsilk2',fg='black')
        button_add.pack()

#        label_add = Label(label_fkey, bg='black')
#        label_add.grid(row=4, column=2, sticky=E, pady=10)
#        button_add = Button(label_add, text='exp', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('e'),bg='cornsilk2',fg='gray40')
#        button_add.pack()                

#        label_sub = Label(label_fkey, bg='black')
#        label_sub.grid(row=5, column=0, sticky=W, pady=10)
#
#        button_sub = Button(label_sub, text='pow', font=('Helvetica', '16'), height=1, width=3,
#                    command=lambda: self.click_button('pow'), bg='cornsilk2', fg='gray40')
#        button_sub.grid(row=0, column=0)  # Use grid for button_sub as well
#        button_rbrace.pack()

c = Calculator(root)
root.title("Python Calculator Challenge")
root.mainloop()
