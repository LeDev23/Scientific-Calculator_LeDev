
from tkinter import *
import tkinter.messagebox
from math import *


class Calculator(Frame): #This creates the frame for the calculator side of the application

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)


        # Variable
        self.current_value = ''                                # variable for the equation
        self.updated_value = ''                                # variable for the answer
        self.current_ans = None
        self.equated = False

        # labels and entry

        # Number and Operator Buttons Are Displayed In The Labels
        self.display = Entry(self, width=50, borderwidth=10, justify=RIGHT, font=('arial', 12), relief=SUNKEN, bg='#0ED145')
        self.display.grid(row=0, column=0, columnspan=5)

        # History Frame
        history_label = Label(self, text='Calculations History', width=20, justify=CENTER, font=('arial', 12, 'italic'),
                              relief=SUNKEN)
        history_label.grid(row=0, column=5, padx=(5, 5))

        self.history_frame = LabelFrame(self, relief=SUNKEN, height=500, width=295, bg='#C3C3C3')
        self.history_frame.grid(row=1, column=5, rowspan=9, pady=(0, 5), columnspan=2)
        self.history_frame.propagate(0)

        # sub frame for history to destroy the frame widget faster
        self.history_frame2 = LabelFrame(self.history_frame, relief=FLAT, height=50, width=250, bg='#C3C3C3')
        self.history_frame2.pack(anchor=NE)

        # ALL THE BUTTONS GROUPED BY ROWS
        btn_clear_history = Button(self, text='Clear', font=('arial', 12), command=self.clear_history).grid(
            row=0, column=6, sticky='we')

        btn_natural_log = Button(self, text='ln', font=('arial', 12), padx=10, pady=10,
                                 command=lambda: self.calcfunction('log')).grid(row=9, column=0, sticky='wens')
        btn_log2 = Button(self, text='log2', font=('arial', 12), padx=10, pady=10,
                          command=lambda: self.calcfunction('log2')).grid(row=9, column=1, sticky='wens')
        btn_log10 = Button(self, text='log10', font=('arial', 12), padx=5, pady=10,
                           command=lambda: self.calcfunction('log10')).grid(row=9, column=2, sticky='wens')
        btn_e = Button(self, text='e', font=('arial', 12), padx=10, pady=10,
                       command=lambda: self.button_press('e')).grid(row=9, column=3, sticky='wens')
        btn_rad = Button(self, text='rad', font=('arial', 12), padx=10, pady=10,
                         command=lambda: self.calcfunction('rad')).grid(row=9, column=4, sticky='wens')

        btn_sinh = Button(self, text='sinh', font=('arial', 12), padx=10, pady=10,
                          command=lambda: self.calcfunction('sinh')).grid(row=8, column=0, sticky='wens')
        btn_cosh = Button(self, text='cosh', font=('arial', 12), padx=10, pady=10,
                          command=lambda: self.calcfunction('cosh')).grid(row=8, column=1, sticky='wens')
        btn_tanh = Button(self, text='tanh', font=('arial', 12), padx=10, pady=10,
                          command=lambda: self.calcfunction('tanh')).grid(row=8, column=2, sticky='wens')
        btn_abs = Button(self, text='|x|', font=('arial', 12), padx=10, pady=10,
                         command=lambda: self.calcfunction('abs')).grid(row=8, column=3, sticky='wens')
        btn_deg = Button(self, text='deg', font=('arial', 12), padx=10, pady=10,
                         command=lambda: self.calcfunction('deg')).grid(row=8, column=4, sticky='wens')

        btn_sin = Button(self, text='sin', font=('arial', 12), padx=10, pady=10,
                         command=lambda: self.calcfunction('sin')).grid(row=7, column=0, sticky='wens')
        btn_cos = Button(self, text='cos', font=('arial', 12), padx=10, pady=10,
                         command=lambda: self.calcfunction('cos')).grid(row=7, column=1, sticky='wens')
        btn_tan = Button(self, text='tan', font=('arial', 12), padx=10, pady=10,
                         command=lambda: self.calcfunction('tan')).grid(row=7, column=2, sticky='wens')
        btn_exponential = Button(self, text='exp', font=('arial', 12), padx=10, pady=10,
                                 command=lambda: self.calcfunction('exp')).grid(row=7, column=3, sticky='wens')
        btn_fact = Button(self, text='n!', font=('arial', 12), padx=10, pady=10,
                          command=lambda: self.calcfunction('fact')).grid(row=7, column=4, sticky='wens')

        btn_open_prnth = Button(self, text='(', font=('arial', 12,), padx=10, pady=10,
                                command=lambda: self.button_press('(')).grid(row=6, column=0, sticky='wens')
        btn_close_prnth = Button(self, text=')', font=('arial', 12), padx=10, pady=10,
                                 command=lambda: self.button_press(')')).grid(row=6, column=1, sticky='wens')
        btn_eql = Button(self, text='=', font=('arial', 12, 'bold'), width=1, height=1, bg='#2FFF97', padx=10,
                         pady=10, command=self.equate).grid(row=6, column=3, columnspan=2, sticky='nswe')
        btn_mod = Button(self, text='Mod', font=('arial', 12), padx=10, pady=10,
                         command=lambda: self.button_press('Mod')).grid(row=6, column=2, sticky='wens')

        btn_pi = Button(self, text='π', font=('arial', 15), padx=10, pady=5,
                        command=lambda: self.button_press('π')).grid(row=5, column=0, sticky='wens')
        btn_0 = Button(self, text='0', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('0')).grid(row=5, column=1, sticky='wens')
        btn_dot = Button(self, text='.', font=('arial', 15), padx=10, pady=5,
                         command=lambda: self.button_press('.')).grid(row=5, column=2, sticky='wens')
        btn_add = Button(self, text='+', font=('arial', 15), padx=10, pady=5,
                         command=lambda: self.button_press(' + ')).grid(row=5, column=3, sticky='wens')
        btn_ans = Button(self, text='Ans', font=('arial', 12), padx=10, pady=10,
                         command=self.showcurrentans).grid(row=5, column=4, sticky='wens')

        btn_1 = Button(self, text='1', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('1')).grid(row=4, column=0, sticky='wens')
        btn_2 = Button(self, text='2', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('2')).grid(row=4, column=1, sticky='wens')
        btn_3 = Button(self, text='3', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('3')).grid(row=4, column=2, sticky='wens')
        btn_sub = Button(self, text='-', font=('arial', 15), padx=10, pady=5,
                         command=lambda: self.button_press(' - ')).grid(row=4, column=3, sticky='wens')

        btn_4 = Button(self, text='4', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('4')).grid(row=3, column=0, sticky='wens')
        btn_5 = Button(self, text='5', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('5')).grid(row=3, column=1, sticky='wens')
        btn_6 = Button(self, text='6', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('6')).grid(row=3, column=2, sticky='wens')
        btn_mul = Button(self, text='×', font=('arial', 15), padx=10, pady=5,
                         command=lambda: self.button_press(' × ')).grid(row=3, column=3, sticky='wens')
        btn_clear = Button(self, text='C', font=('arial', 12), bg='#FF6361', padx=10, pady=10,
                           command=self.clear).grid(row=3, column=4, rowspan=2, sticky='nswe')

        btn_7 = Button(self, text='7', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('7')).grid(row=2, column=0, sticky='wens')
        btn_8 = Button(self, text='8', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('8')).grid(row=2, column=1, sticky='wens')
        btn_9 = Button(self, text='9', font=('arial', 12, 'bold'), bg='#B7CDCF', padx=10, pady=10,
                       command=lambda: self.button_press('9')).grid(row=2, column=2, sticky='wens')
        btn_div = Button(self, text='÷', font=('arial', 15), padx=10, pady=5,
                         command=lambda: self.button_press(' / ')).grid(row=2, column=3, sticky='wens')

        btn_pwr = Button(self, text='x^y', font=('arial', 12), padx=10, pady=10,
                         command=lambda: self.button_press('^')).grid(row=1, column=0, sticky='wens')
        btn_sqrt = Button(self, text='√', font=('arial', 12), padx=10, pady=10,
                          command=lambda: self.calcfunction('sqrt')).grid(row=1, column=1, sticky='wens')
        btn_left = Button(self, text='←', font=('arial', 12), padx=10, pady=10, bg='#FFA443',
                          command=lambda: self.movebutton('left')).grid(row=1, column=2, sticky='wens')
        btn_right = Button(self, text='→', font=('arial', 12), padx=10, pady=10, bg='#FFA443',
                           command=lambda: self.movebutton('right')).grid(row=1, column=3, sticky='wens')
        btn_clear_all = Button(self, text='CE', font=('arial', 12), bg='#FF6361', padx=10, pady=10,
                               command=self.clear_all).grid(row=1, column=4, rowspan=2, sticky='nswe')

    # this method inserts the values or symbols corresponding to the buttons into the entry
    def button_press(self, button):
        self.display.insert(self.display.index(INSERT), button)
        self.current_value = self.display.get()
        self.equated = False
        self.display.focus()

    # evaluates the equation
    def equate(self):
        try:
            self.current_value = self.display.get()
            self.updated_value = self.current_value
            self.updated_value = self.updated_value.replace('^', '**')  # replacing symbols with their python equivalent
            self.updated_value = self.updated_value.replace('×', '*')
            self.updated_value = self.updated_value.replace('√', 'sqrt')
            self.updated_value = self.updated_value.replace('π', f'{pi}')
            self.updated_value = eval(self.updated_value)

        except ZeroDivisionError:
            tkinter.messagebox.showinfo('Error', 'Cannot divide by zero!')
            self.display.delete(0, END)
            self.updated_value = ''

        except (SyntaxError, TypeError, NameError):
            if self.updated_value == '':  # this line prevents error from popping up when equal button is pressed and the entry is blank
                return

            else:
                tkinter.messagebox.showinfo('Error', 'Incorrect format!\n''Check for missing/unwanted characters.')
                self.display.delete(0, END)
                self.updated_value = ''

        except (ValueError):
            tkinter.messagebox.showinfo('Error', 'Invalid input!\n''Check for missing/unwanted characters.')
            self.display.delete(0, END)
            self.updated_value = ''

        else:
            self.paste_history()
            self.display.delete(0, END)
            self.display.insert(0, self.updated_value)
            self.current_ans = self.display.get()
            self.equated = True

    # deletes entire entry
    def clear_all(self):
        self.display.delete(0, END)

    # clears entry one by one
    def clear(self):
        self.display.delete(self.display.index("insert") - 1)

    # method to move the cursor
    def movebutton(self, direction):
        self.equated = False
        if direction == 'left':
            self.display.icursor(self.display.index('insert') - 1)

        else:
            self.display.icursor(self.display.index('insert') + 1)

    # method in pasting history
    def paste_history(self):
        self.history = Label(self.history_frame2, text=f'{self.current_value} = {self.updated_value}', wraplength=280,
                             justify=RIGHT, font=10, bg='#C3C3C3')
        self.history.pack(side=BOTTOM, anchor=E)

    # method to clear the history
    def clear_history(self):
        self.history_frame2.destroy()
        self.history_frame2 = LabelFrame(self.history_frame, relief=FLAT, height=50, width=250, bg='#C3C3C3')
        self.history_frame2.pack(anchor=NE)

    # method to show current answer
    def showcurrentans(self):
        if self.current_ans != None:
            self.button_press(self.current_ans)
            self.equated = False

        else:
            pass

    # method for other operations
    def calcfunction(self, function):
        self.display.focus()
        temp = self.display.get()
        self.display.delete(0, END)
        self.display.insert(0, f'{function}(' + temp + ')')
        temp = self.display.get()
        self.display.icursor(temp.index(')'))



class Calculator_Window(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('VCalculator: Scientific Calculator  by Velasco_CCC102')
        self.resizable(width=False, height=False)

        icon = PhotoImage(file='CalcuLogo2.png')
        self.iconphoto(True, icon)
        self.config(background="#3f3f3f")

        #
        Calculator(self).grid(sticky=NSEW)


calculator_app = Calculator_Window()
calculator_app.mainloop()