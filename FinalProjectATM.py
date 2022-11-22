import tkinter as tk
#from PIL import ImageTk,Image
 


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

       
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg = 'black')# bg = tk.PhotoImage(file='C:/Users/Aaron Roberson/Desktop/ATM Project/CashCow.jpg'))
        self.controller = controller

        self.controller.title('Cash Cow')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='C:/Users/Aaron Roberson/Desktop/ATM Project/atm.png'))

        headingLabel1 = tk.Label(self,
                                 text = 'CASH COW ATM',
                                 font =('Arial',45,'bold'),
                                 foreground = 'white',
                                 background = 'black')

        headingLabel1.pack(pady = 30)

        space_label = tk.Label(self, height=4, bg= 'black')
        space_label.pack()

        login_label = tk.Label(self,
                               text='Enter Your User ID',
                               font=('Arial',13),
                               bg ='black',
                               fg ='white')
        login_label.pack(pady = 10)

        my_user_name = tk.StringVar()
        login_entry_box = tk.Entry(self,
                                        textvariable = my_user_name,
                                        font = ('Arial',12),
                                        width = 22)
        login_entry_box.focus_set()
        login_entry_box.pack(ipady = 7)
        def handle_focus_in(_):
            login_entry_box.configure(fg='black',show='*')
        login_entry_box.bind('<FocusIn>',handle_focus_in)
        
        def check_id():
         if my_user_name.get()== '1234':
             controller.show_frame('MenuPage')
         else:
             incorrect_id_label['text']= 'The ID is not valid'
         
        login_button = tk.Button(self,
                                 text = 'Login',
                                 command = check_id,
                                 relief = 'raised',
                                 borderwidth = 3,
                                 width = 40,
                                 height = 3)
        login_button.pack(pady = 10)

        incorrect_id_label = tk.Label(self,
                                      text='',
                                      font=('Arial',13),
                                      fg = 'red',
                                      bg = 'white',
                                      anchor = 'n')
        incorrect_id_label.pack(fill = 'both',expand = True)
        
                                        

        
        
       


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()