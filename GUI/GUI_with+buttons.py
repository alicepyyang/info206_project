
# coding: utf-8

# In[3]:



# coding: utf-8

# In[ ]:

LARGE_FONT = ("Verdana", 12)

import tkinter as tk
class Food(tk.Tk):
    def  __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
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
class StartPage(tk.Frame):
    def  __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = "PortFoodlio", font = LARGE_FONT)
        label.pack(pady = 100, padx = 100)
        button1 = tk.Button(self, text = "Let's get started!",
                            command = lambda: controller.show_frame(PageOne))
        button1.pack()

class PageOne(tk.Frame):
    def  __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = "Enter the ingredients separated by commas", font = LARGE_FONT)
        label.pack(pady = 100, padx = 100)
        button2 = tk.Button(self, text = "Back to Home",
                            command = lambda: controller.show_frame(StartPage))
        button2.pack()

                            
app = Food()
app.mainloop()

# In[ ]:



