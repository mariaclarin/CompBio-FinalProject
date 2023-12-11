from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
from paternity_test import *
import pandas as pd
from tabulate import tabulate

def cleanPage(root):
    """
    Method to clean the window
    """
    for widget in root.winfo_children():  # To know the widgets used in that page
        widget.destroy()  # To delete all the widgets with iteration
        
def landingPage(root):
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background, backgroundpic
    backgroundpic = Image.open("images/background.png")
    background = ImageTk.PhotoImage(backgroundpic)

    # Show image using label
    backgroundlabel = Label(root, image=background, background="#292F5C")
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)

    title = Label(
        root,
        font=(myFont, 40),
        text="Paternity Test",
        bg="#494E73",
        foreground="white"
    )
    title.place(relx=0.135, rely=0.25)
    title1 = Label(
         root,
        font=(myFont, 40),
        text="Simulator",
        bg="#494E73",
        foreground="white"
    )
    title1.place(relx=0.135, rely=0.32)

    title2 = Label(
        root,
        font=(myFont, 14),
        text="Developed by Arish, Ferdinand, and Maria",
        bg="#494E73",
        foreground="white"
    )
    title2.place(relx=0.135, rely=0.4)
    title2 = Label(
         root,
        font=(myFont, 20),
        text="___________",
        bg="#494E73",
        foreground="#EF6B48"
    )
    title2.place(relx=0.135, rely=0.43)
    
    disclaimer = Label(
        root,
        font=(myFont, 9),
        text="This program is for educational purposes to simulate a simple",
        foreground="white",
        bg="#494E73",
    )
    disclaimer.place(relx=0.135, rely=0.51)
    disclaimer1 = Label(
        root,
        font=(myFont, 9),
        text="paternity probability algorithm. It should not be used for true",
        foreground="white",
        bg="#494E73",
    )
    disclaimer1.place(relx=0.135, rely=0.532)
    disclaimer2 = Label(
        root,
        font=(myFont, 9),
        text="biological assessments of paternity or biological affinity. Data used",
        foreground="white",
        bg="#494E73",
    )
    disclaimer2.place(relx=0.135, rely=0.554)
    disclaimer3 = Label(
        root,
        font=(myFont, 9),
        text="for testing publically available DNA sequences or synthetically",
        foreground="white",
        bg="#494E73",
    )
    disclaimer3.place(relx=0.135, rely=0.576)
    disclaimer4 = Label(
        root,
        font=(myFont, 9),
        text="mutated DNA sequences.",
        foreground="white",
        bg="#494E73",
    )
    disclaimer4.place(relx=0.135, rely=0.598)

    
    userButton = Button(
        root,
        font=(myFont, 15),
        command=lambda: dnaInput(root),
        text="  Start  ",
        background="#494E73",
        foreground="black",
    )
    userButton.place(relx=0.135, rely=0.65)



def validator():
    fatherdna = fatherinput.get("1.0", tk.END)
    childdna = childinput.get("1.0", tk.END)
    try:
        results(root, fatherdna, childdna)
    except Exception as e:
        messagebox.showerror("Error", "Your DNA inputs are invalid or of invalid length. Please try again.")


def results(root, fatherdna, childdna):
    matching_percentage, childmarkerlen, fathermarkerlen, childfathermarkerlen, child_markers, father_markers = paternity_test(childdna, fatherdna, 13) 
    
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background, backgroundpic
    backgroundpic = Image.open("images/background1.png")
    background = ImageTk.PhotoImage(backgroundpic)

    # Show image using label
    backgroundlabel = Label(root, image=background, background="#182052")
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)

    title = Label(
        root,
        font=(myFont, 40),
        text="Paternity Test Results",
        bg="#182052",
        foreground="#EF6B48"
    )
    title.place(relx=0.12, rely=0.09)
    instruction = Label(
        root,
        font=(myFont, 16),
        text="Here are the genetic markers found in the alleged father and child DNA to indicate paternity probability",
        bg="#182052",
        foreground="white"
    )
    instruction.place(relx=0.12, rely=0.17)

    resultTable = ttk.Treeview(root, columns=('Genetic Markers', 'Child', 'Alleged Father'), show='headings')
    resultTable.heading('Genetic Markers', text='Genetic Markers')
    resultTable.heading('Child', text='Child')
    resultTable.heading('Alleged Father', text='Alleged Father')
    resultTable.column('Genetic Markers',  width=250, anchor='center')
    resultTable.column('Child', width=250, anchor='center')
    resultTable.column('Alleged Father', width=250, anchor='center')
    resultTable['height'] = 15

    all_markers = set(child_markers + father_markers)
    for marker in all_markers:
        child_count = childdna.count(marker)
        father_count = fatherdna.count(marker)
        resultTable.insert('', 'end', values=(marker,child_count,father_count))

    if matching_percentage >= 99.9:
        resultdescription = f"The supposed father is very likely to be the biological father with {matching_percentage}% probability of paternity."
        resultstitle = "High likelihood of biological paternity."
        resultcolor = 1
    else:
        resultdescription = f"The supposed father is unlikely to be the biological father with {matching_percentage}% probability of paternity."
        resultstitle = "Unlikely of biological paternity."
        resultcolor= 0
    if resultcolor==1:
        resultstitles = Label(
            root,
            font=(myFont, 20),
            text=resultstitle,
            bg="#182052",
            foreground="#09B800"
        )
        resultstitles.place(relx=0.12, rely=0.21)
    else:
        resultstitles = Label(
            root,
            font=(myFont, 20),
            text=resultstitle,
            bg="#182052",
            foreground="#FF0000"
        )
        resultstitles.place(relx=0.12, rely=0.21)

    resultstitles1 = Label(
        root,
        font=(myFont, 10),
        text='No. of Child Markers: ',
        bg="#182052",
        foreground="#737BB6"
    )
    resultstitles1.place(relx=0.72, rely=0.21)
    resultstitles2 = Label(
        root,
        font=(myFont, 10),
        text=childmarkerlen,
        bg="#182052",
        foreground="#737BB6"
    )
    resultstitles2.place(relx=0.835, rely=0.21)
    resultstitles3 = Label(
        root,
        font=(myFont, 10),
        text='No. of Father Markers: ',
        bg="#182052",
        foreground="#737BB6"
    )
    resultstitles3.place(relx=0.72, rely=0.235)
    resultstitles4 = Label(
        root,
        font=(myFont, 10),
        text=fathermarkerlen,
        bg="#182052",
        foreground="#737BB6"
    )
    resultstitles4.place(relx=0.835, rely=0.235)

    resultTable.place(relx=0.12, rely=0.27)
    results_label = tk.Label(root, text= resultdescription, font=('Helvetica', 14), bg="#182052", foreground="white")
    results_label.place(relx=0.12, rely=0.705)

    disclaimer_label = tk.Label(root, text="This program is for educational purposes to simulate a simple paternity probability algorithm. It should not be used for true biological assessments of  ", font=('Helvetica', 12), bg="#182052", foreground="#737BB6")
    disclaimer_label.place(relx=0.12, rely=0.74)   
    disclaimer1_label = tk.Label(root, text="paternity or biological affinity. Data used for testing publically available DNA sequences available DNA sequences or synthetically mutated DNA ", font=('Helvetica', 12), bg="#182052", foreground="#737BB6")
    disclaimer1_label.place(relx=0.12, rely=0.77)   
    disclaimer2_label = tk.Label(root, text="sequences. ", font=('Helvetica', 12), bg="#182052", foreground="#737BB6")
    disclaimer2_label.place(relx=0.12, rely=0.80)   

    def export_to_txt(table, filename):
        data = []

        # Extract data from the table
        for row_id in table.get_children():
            data.append(table.item(row_id)['values'])

        # Convert data to a DataFrame
        df = pd.DataFrame(data, columns=['Genetic Markers', 'Child', 'Alleged Father'])

        # Export DataFrame to a .txt file using tabulate
        with open(filename, 'w') as file:
            file.write('Paternity Test Simulator Results\n')
            file.write('===================================================\n')
            file.write(resultstitle)
            file.write('\n')
            file.write('===================================================\n')
            file.write(resultdescription)
            file.write('\n\n')
            file.write('Total Child Markers: ')
            file.write((str(len(child_markers))))
            file.write('\n')
            file.write('Total Father Markers: ')
            file.write(str(len(father_markers)))
            file.write('\n')
            file.write('Total Combined Markers: ')
            file.write(str(len(set(child_markers) & set(father_markers))))
            file.write('\n\n')

            file.write(tabulate(df, headers='keys', tablefmt='pretty'))
            file.write('\n\n')
            file.write('This program is for educational purposes to simulate a simple paternity probability algorithm. It should not be used for true biological assessments of paternity or biological affinity. Data used for testing publically available DNA sequences or synthetically mutated DNA sequences.')
    
    def export_button_click(table):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if file_path:
            export_to_txt(table, file_path)

    exportButton = tk.Button(root, text="Export Results", command=lambda: export_button_click(resultTable), font=(myFont, 12))
    exportButton.place(relx=0.27, rely=0.85)
    returnButton = Button(
        root,
        font=(myFont, 12),
        command=lambda: landingPage(root),
        text="Take Another Test",
        background="#494E73",

        foreground="black"
    )
    returnButton.place(relx=0.12, rely=0.85)


def dnaInput(root):
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background, backgroundpic
    backgroundpic = Image.open("images/background1.png")
    background = ImageTk.PhotoImage(backgroundpic)

    # Show image using label
    backgroundlabel = Label(root, image=background, background="#182052")
    backgroundlabel.image = background
    backgroundlabel.place(x=0, y=0)

    title = Label(
        root,
        font=(myFont, 40),
        text="DNA Input",
        bg="#182052",
        foreground="#EF6B48"
    )
    title.place(relx=0.137, rely=0.105)
    instruction = Label(
        root,
        font=(myFont, 15),
        text="Type the alleged father's DNA sequence or load a file (.txt)",
        bg="#182052",
        foreground="white"
    )
    instruction.place(relx=0.137, rely=0.175)

    global fatherinput
    fatherinput = tk.Text(root, wrap='word', width=100, height=10)
    fatherinput.place(relx=0.137,rely=0.215 )


    # Function to change the input field to the loaded file content
    def loadfatherfile():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                fatherinput.delete("1.0", "end")
                fatherinput.insert("1.0", content)

    loadfatherbutton = Button(
        root,
        font=(myFont, 10),
        command=loadfatherfile,
        text="Load Father DNA File",
        background="#494E73",
        foreground="black",
    )
    loadfatherbutton.place(relx=0.137, rely=0.425)

    title2 = Label(
         root,
        font=(myFont, 12),
        text="_________",
        bg="#182052",
        foreground="#EF6B48"
    )
    title2.place(relx=0.137, rely=0.4765)

    instruction1 = Label(
        root,
        font=(myFont, 15),
        text="Type the child's DNA sequence or load a file (.txt)",
        bg="#182052",
        foreground="white"
    )
    instruction1.place(relx=0.137, rely=0.505)

    global childinput
    childinput = tk.Text(root, wrap='word', width=100, height=10)
    childinput.place(relx=0.137,rely=0.545 )

    def loadchildfile():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                childinput.delete("1.0", "end")
                childinput.insert("1.0", content)

    loadchildbutton = Button(
        root,
        font=(myFont, 10),
        command=loadchildfile,
        text="Load Child DNA File",
        background="#494E73",
        foreground="black",
    )
    loadchildbutton.place(relx=0.137, rely=0.755)

    testButton = Button(
        root,
        font=(myFont, 15),
        command=validator,
        text="Start Paternity Test",
        background="#494E73",
        width=20,
        foreground="black"
    )
    testButton.place(relx=0.24, rely=0.83)

    returnButton = Button(
        root,
        font=(myFont, 15),
        command=lambda: landingPage(root),
        text="  Return  ",
        background="#494E73",

        foreground="black"
    )
    returnButton.place(relx=0.137, rely=0.83)


def main():
    width = 1000
    height = 700

    # Create tkinter root
    global root
    root = Tk()
    root.config(bg="#2C602E")
    root.title("Paternity Test Simulator")
    global myFont
    myFont = font.Font(family="Helvetica")

    # Assign value of device screen size
    setW = root.winfo_screenwidth()
    setH = root.winfo_screenheight()

    # Set the padding so it will position window center
    padW = (setW//2)-(width//2)
    padH = (setH//2)-(height//2)

    # Set the window size and position
    root.geometry(f"{width}x{height}+{padW}+{padH}")
    root.resizable(False, False)

    landingPage(root)
    root.mainloop()

main()