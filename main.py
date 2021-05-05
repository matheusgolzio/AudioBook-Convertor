import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import filedialog as dlg
from tkinter import messagebox


root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        self.root.mainloop()
    

    def tela(self):
        self.root.title("Audio Book Convertor - Convert your pdf in audiobook")
        self.root.resizable(False, False)
        self.root.geometry("300x300")
    

    def widgets(self):
        # Selected Book
        self.selected_book = Label(self.root, text="No PDF selected", font=("Roboto", 14))
        self.selected_book.place(relx=0.23, rely=0.1)

        # Select Book
        self.select_book = Button(self.root, text="Select PDF", bd=4, command=self.select_file)
        self.select_book.place(relx=0.1, rely=0.4)

        # Convert in  Audio Book
        self.convert_book = Button(self.root, text="Convert in AudioBook", bd=4, command=self.convert)
        self.convert_book.place(relx=0.4, rely=0.4)
    

    def select_file(self):
        self.filename = dlg.askopenfilename()
        self.selected_book["text"] = "PDF selected"
    

    def convert(self):
        with open(f'{self.filename}', "rb") as book:
            self.reader = PyPDF2.PdfFileReader(book)

            self.full_text = ""

            self.audio_reader = pyttsx3.init()
            self.audio_reader.setProperty("rate", 100)

            for self.page in range(self.reader.numPages):
                self.next_page = self.reader.getPage(self.page)
                self.content = self.next_page.extractText()
                self.full_text += self.content

            self.audio_reader.save_to_file(self.full_text, "myaudiobook.mp3")
            self.audio_reader.runAndWait()

            messagebox.showinfo("Saved", "The audiobook version of your pdf was saved sucessfully.")


Application()
