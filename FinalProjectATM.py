import tkinter as tk
import time

 
current_balance = 1000   #storing the users balance

class AtmApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

       
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.shared_data = {'Balance':tk.IntVar()} #variable to display balance
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #creating the different pages and the navigation between the pages
        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        #Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

#first screen in the app
class StartPage(tk.Frame):
    #initial function of the class
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg = 'black')
        self.controller = controller
        #setting the title, making sure that when opened the window expands to full size, added image to top left corner.
        self.controller.title('Cash Cow')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='atm.png'))
        #creating heading label for the home page
        headingLabel1 = tk.Label(self,
                                 text = 'CASH COW ATM',
                                 font =('Arial',45,'bold'),
                                 foreground = 'white',
                                 background = 'black')
        #setting the location of the label
        headingLabel1.pack(pady = 30)
        #label to give space between heading label and login label
        space_label = tk.Label(self, height=4, bg= 'black')
        space_label.pack()
        #creating the entry login label
        login_label = tk.Label(self,
                               text='Enter Your User ID',
                               font=('Arial',13),
                               bg ='black',
                               fg ='white')
        #setting position of login label
        login_label.pack(pady = 10)

        my_user_name = tk.StringVar()#variable for what the user will be entering in the entry box
        #creating entry box for the login information
        login_entry_box = tk.Entry(self,
                                        textvariable = my_user_name,
                                        font = ('Arial',12),
                                        width = 22)
        login_entry_box.focus_set()
        login_entry_box.pack(ipady = 7)#setting location of entry box

        #function to hide the password with asterisks when entered
        def handle_focus_in(_):
            login_entry_box.configure(fg='black',show='*')
        login_entry_box.bind('<FocusIn>',handle_focus_in)
        #function to set the user id and check the user input and take them to next page if correct
        def check_id():
         if my_user_name.get()== '1234': #setting the login id to 1234
             my_user_name.set('')
             incorrect_id_label['text']=''
             controller.show_frame('MenuPage')
         #label to let the user know if they entered and invalid id
         else:
             incorrect_id_label['text']= 'The ID is not valid'
        #creating login button for user to click when their id is entered 
        login_button = tk.Button(self,
                                 text = 'Login',
                                 command = check_id,
                                 relief = 'raised',
                                 borderwidth = 3,
                                 width = 40,
                                 height = 3)
        login_button.pack(pady = 10) #setting the button location
        #label to display if user enters incorrect information
        incorrect_id_label = tk.Label(self,
                                      text='',
                                      font=('Arial',13),
                                      fg = 'red',
                                      bg = 'white',
                                      anchor = 'n')
        incorrect_id_label.pack(fill = 'both',expand = True)#setting the label location

        
        #creating a bottom frame to the page
        bottom_frame = tk.Frame(self, relief = 'raised', borderwidth = 3)
        bottom_frame.pack(fill='x', side='bottom')

        #adding image to bottom frame to show what bank cards this atm machine takes
        american_express = tk.PhotoImage(file='american-express.png')
        ae_label = tk.Label(bottom_frame, image=american_express)
        ae_label.pack(side='left')
        ae_label.image = american_express

        discover = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame, image=discover)
        discover_label.pack(side='left')
        discover_label.image = discover

        visa = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa)
        visa_label.pack(side='left')
        visa_label.image = visa
        #function to show the time in the bottom right corner and update every 200 milliseconds
        def clock():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,clock)
        time_label = tk.Label(bottom_frame, font=('Arial',12))
        time_label.pack(side='right')

        clock()      

        

         
                           

        
        
       

#second page the user is taken to upon login
class MenuPage(tk.Frame):
    #initial function of the class, refers to self and is the parent window, uses controller to change frames 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = 'black')
        self.controller = controller
        #heading label reused for menu page
        headingLabel1 = tk.Label(self,
                                 text = 'CASH COW ATM',
                                 font =('Arial',45,'bold'),
                                 foreground = 'white',
                                 background = 'black')

        headingLabel1.pack(pady = 30)#set label location
        #creating main menu label for menu page
        menu_label = tk.Label(self,
                              text='Main Menu',
                              font=('Arial',30),
                              fg='white',
                              bg='black')
        menu_label.pack()#setting label location
        #creating label to ask user to select and option
        select_label = tk.Label(self,
                                text='Please make a selection',
                                font=('Arial',20),
                                fg='white',
                                bg='black',
                                anchor='center')
        select_label.pack()#setting label location

        #creating a frame to put the buttons on
        button_frame = tk.Frame(self,bg='white')
        button_frame.pack(fill='both', expand=True)
        #function to allow the user to go to the withdraw page when withdraw button is selected
        def withdraw():
            controller.show_frame('WithdrawPage')
        #creating the withdraw button
        withdraw_button = tk.Button(button_frame,
                                    text='Withdraw',
                                    command=withdraw,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
                                    
        withdraw_button.place(x=840, y= 30)#setting location of the withdraw button

        #function to allow the user to go to the deposit page when deposit button is selected
        def deposit():
            controller.show_frame('DepositPage')
        #creating the deposit button
        deposit_button = tk.Button(button_frame,
                                    text='Deposit',
                                    command=deposit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
                                    
        deposit_button.place(x=840, y= 155)#setting the location of the deposit button

        #function to allow the user to go to the balance page when selected
        def balance():
            controller.show_frame('BalancePage')
        #creating the balance button
        balance_button = tk.Button(button_frame,
                                    text='Balance',
                                    command=balance,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
                                    
        balance_button.place(x=840, y= 280)#setting the location of the balance button

        #function to allow the user to exit back to the home page when selected
        def exit():
            controller.show_frame('StartPage')
        #creating exit button
        exit_button = tk.Button(button_frame,
                                    text='Exit',
                                    command=exit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
                                    
        exit_button.place(x=840, y= 405)#setting the location of the exit button

        
        #adding bottom frame to page
        bottom_frame = tk.Frame(self, relief = 'raised', borderwidth = 3)
        bottom_frame.pack(fill='x', side='bottom')
        #adding image of bank cards the atm takes
        american_express = tk.PhotoImage(file='american-express.png')
        ae_label = tk.Label(bottom_frame, image=american_express)
        ae_label.pack(side='left')
        ae_label.image = american_express

        discover = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame, image=discover)
        discover_label.pack(side='left')
        discover_label.image = discover

        visa = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa)
        visa_label.pack(side='left')
        visa_label.image = visa
        #function to add time to bottom right of page
        def clock():
            current_time = time.strftime('%I:%M %p')#
            time_label.config(text=current_time)
            time_label.after(200,clock)
        time_label = tk.Label(bottom_frame, font=('Arial',12))
        time_label.pack(side='right')

        clock()
        

#class to set up withdrawpage
class WithdrawPage(tk.Frame):
    #initial function of the class, refers to self and is the parent window, uses controller to change frames
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')
        self.controller = controller
        #heading label reused for withdraw page
        headingLabel1 = tk.Label(self,
                                 text = 'CASH COW ATM',
                                 font =('Arial',45,'bold'),
                                 foreground = 'white',
                                 background = 'black')

        headingLabel1.pack(pady = 30)#setting location of label
        #creating label to tell user to select amount for withdraw
        amount_label = tk.Label(self,
                              text='Please select an amount to withdraw',
                              font=('Arial',30),
                              fg='white',
                              bg='black')
        amount_label.pack()#setting label location

        #creating frame for buttons to go on
        button_frame = tk.Frame(self,bg='white')
        button_frame.pack(fill='both', expand=True)
        #function for when user clicks on specific withdraw button
        def withdraw(amount):
          global current_balance#gets user current balance
          current_balance -= amount#subtracts amount withdrawn from balance 
          controller.shared_data['Balance'].set(current_balance)
          controller.show_frame('MenuPage')
        #creating the $20 withdraw button
        twenty_button = tk.Button(button_frame,
                                  text='$20',
                                  command=lambda:withdraw(20),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        twenty_button.place(x=450, y=25)#setting location of $20 button
        #creating the $40 withdraw button
        forty_button = tk.Button(button_frame,
                                  text='$40',
                                  command=lambda:withdraw(40),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        forty_button.place(x=450, y=175)
        #creating the $60 withdraw button
        sixty_button = tk.Button(button_frame,
                                  text='$60',
                                  command=lambda:withdraw(60),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        sixty_button.place(x=450, y=325)
        #creating the $80 withdraw button
        eighty_button = tk.Button(button_frame,
                                  text='$80',
                                  command=lambda:withdraw(80),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        eighty_button.place(x=450, y=475)
        #creating the $100 withdraw button
        hundred_button = tk.Button(button_frame,
                                  text='$100',
                                  command=lambda:withdraw(100),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        hundred_button.place(x=1200, y=25)
        #creating the $140 withdraw button
        hundred_forty_button = tk.Button(button_frame,
                                  text='$140',
                                  command=lambda:withdraw(140),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        hundred_forty_button.place(x=1200, y=175)
        #creating the $200 withdraw button
        two_hundred_button = tk.Button(button_frame,
                                  text='$200',
                                  command=lambda:withdraw(200),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        two_hundred_button.place(x=1200, y=325)
        #creating invisible button with text for user to input an alternate withdraw amount
        other_button = tk.Button(button_frame,
                                 text='Enter the alternate amount you want to withdraw',
                                 fg='black',
                                 bg='white',
                                 border=0)
        other_button.place(x=1200, y=530, width=355, height=85)#setting location 
                                 

       

        
        cash = tk.StringVar()#variable for user entering the cash they want to withdraw
        #creating entry box for user to input alternate amount to withdraw
        other_amount_entry = tk.Entry(button_frame,
                                textvariable=cash,
                                width=50,
                                justify='center')
                                                               
        #setting location of entry box                        
        other_amount_entry.place(x=1200, y=475, width=355, height=85)

        


        
        #function when user selects other amount
        def other_amount(_):
            global current_balance #getting user balance
            current_balance-=int(cash.get())#subtracting amount withdrawn from balance
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')

        other_amount_entry.bind('<Return>',other_amount)

        
    
        #creating bottom frame to page
        bottom_frame = tk.Frame(self, relief = 'raised', borderwidth = 3)
        bottom_frame.pack(fill='x', side='bottom')
        #adding images of bank cards the atm takes
        american_express = tk.PhotoImage(file='american-express.png')
        ae_label = tk.Label(bottom_frame, image=american_express)
        ae_label.pack(side='left')
        ae_label.image = american_express

        discover = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame, image=discover)
        discover_label.pack(side='left')
        discover_label.image = discover

        visa = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa)
        visa_label.pack(side='left')
        visa_label.image = visa
        #adding time to bottom right of page
        def clock():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,clock)

        time_label = tk.Label(bottom_frame, font=('Arial',12))
        time_label.pack(side='right')

        clock()
#class to set up DepositPage
class DepositPage(tk.Frame):
    #initial function of the class, refers to self and is the parent window, uses controller to change frames
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller
        #heading label reused for deposit page
        headingLabel1 = tk.Label(self,
                                 text = 'CASH COW ATM',
                                 font =('Arial',45,'bold'),
                                 foreground = 'white',
                                 background = 'black')
        headingLabel1.pack(pady = 30)#placing heading label

        space_label = tk.Label(self, height=4, bg= 'black')
        space_label.pack()
        #create label for user to enter amount they want to deposit
        enter_amount_label = tk.Label(self,
                               text='Enter amount',
                               font=('Arial',13),
                               bg ='black',
                               fg ='white')
        enter_amount_label.pack(pady = 10)#set location of label 
        #variable for user to input the cash amount in the entry box
        cash = tk.StringVar()
        #creating entry box for user to enter deposit amount
        deposit_entry = tk.Entry(self,
                                 textvariable = cash,
                                 font=('Arial',12),
                                 width=22)
        deposit_entry.pack(ipady=7)#set location of entry box
        #function for user to deposit cash
        def deposit_cash():
            global current_balance #getting current user balance
            current_balance += int(cash.get())#adding the deposit amount to balance
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')
        #creating enter button for user to click when deposit amount was entered
        enter_button=tk.Button(self,
                               text='Enter',
                               command=deposit_cash,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=3)
        enter_button.pack(pady=10)#setting location of button
        #creating label to give the two tone color look of the page
        deposit_label=tk.Label(self, bg='white')
        deposit_label.pack(fill='both',expand=True)
        #adding frame to bottom of page
        bottom_frame = tk.Frame(self, relief = 'raised', borderwidth = 3)
        bottom_frame.pack(fill='x', side='bottom')
        #adding image of bank cards accepted by atm
        american_express = tk.PhotoImage(file='american-express.png')
        ae_label = tk.Label(bottom_frame, image=american_express)
        ae_label.pack(side='left')
        ae_label.image = american_express

        discover = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame, image=discover)
        discover_label.pack(side='left')
        discover_label.image = discover

        visa = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa)
        visa_label.pack(side='left')
        visa_label.image = visa
    #function to add time to bottom right of page
    def clock():
        current_time = time.strftime('%I:%M %p')
        time_label.config(text=current_time)
        time_label.after(200,clock)

        time_label = tk.Label(bottom_frame, font=('Arial',12))
        time_label.pack(side='right')

        clock()


   
class BalancePage(tk.Frame):
    #initial function of the class, refers to self and is the parent window, uses controller to change frames
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')
        self.controller = controller
        #heading label reused for balance page
        headingLabel1 = tk.Label(self,
                                 text = 'CASH COW ATM',
                                 font =('Arial',45,'bold'),
                                 foreground = 'white',
                                 background = 'black')
        headingLabel1.pack(pady = 30)

        global current_balance #getting current user balance
        controller.shared_data['Balance'].set(current_balance)
        #creating label to show balance in top left corner
        balance_label = tk.Label(self,
                                 textvariable=controller.shared_data['Balance'],
                                 font=('Arial',18),
                                 fg='white',
                                 bg='black',
                                 anchor='w')
        balance_label.pack(fill='x')#placing the label and filling the space on the x-axis
        #creating frame for the buttons to be placed
        button_frame = tk.Frame(self,bg='white')
        button_frame.pack(fill='both',expand=True)
        #function for user to go back to menu page from balance page
        def menu():
            controller.show_frame('MenuPage')
        #creating the menu button
        menu_button = tk.Button(button_frame,                                
                                 command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
                                
        menu_button.place(x=850, y=180)#setting button location

        #function for user to exit to start page from balance page
        def exit():
            controller.show_frame('StartPage')
        #creating exit button
        exit_button = tk.Button(button_frame,                                
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)        
                                
        exit_button.place(x= 850, y=290)#setting button location
            
                                 
        #creating bottom frame for balance page
        bottom_frame = tk.Frame(self, relief = 'raised', borderwidth = 3)
        bottom_frame.pack(fill='x', side='bottom')
        #adding image of bank cards the atm accepts
        american_express = tk.PhotoImage(file='american-express.png')
        ae_label = tk.Label(bottom_frame, image=american_express)
        ae_label.pack(side='left')
        ae_label.image = american_express

        discover = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame, image=discover)
        discover_label.pack(side='left')
        discover_label.image = discover

        visa = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa)
        visa_label.pack(side='left')
        visa_label.image = visa
        #function to show the time in the bottom right corner
        def clock():
            current_time = time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,clock)

        time_label = tk.Label(bottom_frame, font=('Arial',12))
        time_label.pack(side='right')

        clock()
        

#condition to run AtmApp when ran as a script
if __name__ == "__main__":
    app = AtmApp()
    app.mainloop()
