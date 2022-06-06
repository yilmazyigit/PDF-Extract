import tkinter as tk
import PyPDF2
from PIL import ImageTk as itk
import Image
from numpy import place
root = tk.Tk()
from tkinter.filedialog import askopenfile
#logo
background= "logo.png"
logo= itk.PhotoImage(file=background)
canvas = tk.Canvas(root,width=600, height = 300)
canvas.grid(columnspan=3, rowspan=3)
canvas.imageList = []
canvas.create_image(150,50,anchor = "nw", image=logo)
canvas.imageList.append(logo)

#instructions
instructions = tk.Label(root,text = "Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0,row=2)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent =root, mode = 'rb', title="Choose a file", filetype=[("Pdf file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page= read_pdf.getPage(0)
        page_content = page.extractText()

        #text box
        text_box = tk.Text(root, height = 10, width =50, padx =15, pady=15)
        text_box.insert(1.0,page_content)
        text_box.tag_configure("center", justify ="center")
        text_box.tag_add("center",1.0,"end")
        text_box.grid(column=1, row=4)

        browse_text.set("Browse")


#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable= browse_text, command=lambda:open_file(), font= "Raleway", bg="#20bebe", fg ="white",height=2,width=15)
browse_text.set("Browse")
browse_btn.grid(column=1,row=3)
labelaa = tk.Label(root, text="Yiğit Yılmaz").place(x = 250, y = 20)
canvas = tk.Canvas(root,width=600, height = 250)
canvas.grid(columnspan=3)
root.mainloop()