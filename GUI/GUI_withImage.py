
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
import tkinter as tk

LARGE_FONT = ("Verdana", 12)
root = Tk()
class Food(tk.Tk):
    def  __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self,"Portfoodlio")
        container = tk.Frame(self)
        container.pack(side="top", fill="both",expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):
            frame = self.frames[cont]
            frame.tkraise()
            
photo = PhotoImage(file="./img.jpg")
label = Label(root,image=photo)
label.pack()
label = ttk.Label(root, text = "Welcome to Portfoodlio!")
label.pack()
#button = ttk.Button(root,text = "Let's get started")
#button.pack()

class StartPage(tk.Frame):
    def  __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(root,text = "Welcome to Portfoodlio", font = LARGE_FONT)
        #label.pack(pady = 100, padx = 100)
        button1 = ttk.Button(root, text = "Let's get started!",command = lambda: controller.show_frame(PageOne))
        button1.pack()


class PageOne(tk.Frame):
    def  __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text = "Enter the ingredients separated by commas", font = LARGE_FONT)
        label.pack(pady = 100, padx = 100)
        button2 = ttk.Button(self, text = "Choose categories", command = lambda: controller.show_frame(StartPage))
        button2.pack()

app= Food()
app.mainloop()
                    
                    
                    
#class WelcomePage(tk.Frame):
#    def  __init__(self,parent,controller):
#        tk.Frame.__init__(self,parent)
#        photo= PhotoImage(file="INFO 206 - Portfoodlio.png")
#        label = Label(root,image=photo)
#        label.pack()
#        label = ttk.Label(root, text = "Welcome to Portfoodlio!")
#        label.pack()
#        button = ttk.Button(root,text = "Let's get started", command = lambda: controller.show_frame(PageOne))
#        button.pack()                    

