import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import filedialog as dlg


root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        self.root.mainloop()
    

    def tela(self):
        self.root.title("Audio Book Convertor")
        self.root.resizable(False, False)
        self.root.geometry("300x300")
    

    def widgets(self):
        # Selected Book
        self.selected_book = Label(self.root, text="No book selected", font=("Roboto", 14))
        self.selected_book.place(relx=0.23, rely=0.1)

        # Select Book
        self.select_book = Button(self.root, text="Select Book", bd=4)
        self.select_book.place(relx=0.1, rely=0.4)

        # Convert in  Audio Book
        self.convert_book = Button(self.root, text="Convert in AudioBook", bd=4)
        self.convert_book.place(relx=0.4, rely=0.4)

        # Status
        self.status = Label(self.root, text="teste", font=("Roboto", 14))
        self.status.place(relx=0.4, rely=0.5)


Application()
