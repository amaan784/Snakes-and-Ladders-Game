# using necessary features from Tkinter
from tkinter import Tk, Label, Button, Frame

# function for changing frames
def raise_frame(switch_frame):
    switch_frame.tkraise()


# Function for closing window or app
def close():
    App.destroy()


App = Tk()

App.title("Snakes and Ladders")

# App.geometry("300x300")

InfoFrame = Frame(App)
MainFrame = Frame(App)
Frame1 = Frame(App)
Frame2 = Frame(App)
Frame3 = Frame(App)

for frame in (InfoFrame, MainFrame, Frame1, Frame2, Frame3):
    frame.grid(row=0, column=0, sticky='news')

########################## INFO FRAME ##########################
s2a = "2. User Selected ROI Processing-\n Provide an Image.\n Select a Region of Interest (ROI) using the mouse.\n"
s2b = "Press Enter twice after selecting the ROI.\n The texts in the ROI will be exported in a .txt file."
s2 = s2a + s2b

Label(InfoFrame, text='Snakes and Ladders Information-\n', font=('Arial', 12, 'bold')).pack()
Label(InfoFrame, text=s2, fg="#0d68a4").pack()
Label(InfoFrame, text='').pack()
Button(InfoFrame, text='PROCEED', command=lambda: raise_frame(MainFrame),
       bg="#3ac73a", anchor="center", justify="center", width=30, height=2).pack()

########################## MAIN FRAME ##########################
Label(MainFrame, text='IR Tool', width=5, height=3, font=('Arial', 18, 'bold')).pack()
Label(MainFrame, text='').pack()
Button(MainFrame, text='Word Search in an Image', command=lambda: raise_frame(Frame1),
       bg="#ffb800", anchor="center", justify="center", width=30, height=2, font=('Arial', 15, 'bold')).pack()
# for space
Label(MainFrame, text='').pack()
Button(MainFrame, text='User Selected ROI Processing', command=lambda: raise_frame(Frame2),
       bg="#ffb800", anchor="center", justify="center", width=30, height=2, font=('Arial', 15, 'bold')).pack()
Label(MainFrame, text='').pack()
Button(MainFrame, text='Receipt Features Extraction', command=lambda: raise_frame(Frame3),
       bg="#ffb800", anchor="center", justify="center", width=30, height=2, font=('Arial', 15, 'bold')).pack()
Label(MainFrame, text='').pack()
Button(MainFrame, text="Exit UI", command=close,
       bg="#f25e5e", justify="center", width=15, height=2, font=('Arial', 12, 'bold')).pack()

########################## FRAME 1 / BUTTON 1 ##########################
Label(Frame1, text='Word Search in an Image-', font=('Arial', 18, 'bold')).pack()
Label(Frame1, text='').pack()


Label(Frame1, text='').pack()
Label(Frame1, text='').pack()
Button(Frame1, text='Back to Main Page', command=lambda: raise_frame(MainFrame), bg="#f25e5e",
       width=30, height=2, font=('Arial', 10, 'bold')).pack()

########################## FRAME 2 / BUTTON 2 ##########################
Label(Frame2, text='User Selected ROI Processing-', font=('Arial', 18, 'bold')).pack()
Label(Frame2, text='').pack()
Label(Frame2, text='').pack()


Label(Frame2, text='').pack()
Label(Frame2, text='').pack()
Button(Frame2, text='Back to Main Page', command=lambda: raise_frame(MainFrame), bg="#f25e5e",
       width=30, height=2, font=('Arial', 10, 'bold')).pack()

########################## FRAME 3 / BUTTON 3 ##########################
Label(Frame3, text='Receipt(s) Features Detection and Recognition-', font=('Arial', 18, 'bold')).pack()
Label(Frame3, text='').pack()
Label(Frame3, text='').pack()


Label(Frame3, text='').pack()
Label(Frame3, text='').pack()
Button(Frame3, text='Back to Main Page', command=lambda: raise_frame(MainFrame), bg="#f25e5e",
       width=30, height=2, font=('Arial', 10, 'bold')).pack()

raise_frame(InfoFrame)
App.mainloop()