
# Import module  
from tkinter import *
  
# Create object  
root = Tk() 
  
# Adjust size  
root.geometry("400x400") 
  
# Add image file 
bg = PhotoImage(file = "images/background1.png") 

# Set the window dimensions based on the background image
window_width = bg.width()
window_height = bg.height()
# Adjust size  
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)
  
# Show image using label 
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 
  
# Create Frame 
frame1 = Frame(root) 
frame1.grid(row=2, column=0)
  
button2 = Button(frame1, text="Start")
button2.grid(row=500, column=5)
  

# Execute tkinter 
root.mainloop()