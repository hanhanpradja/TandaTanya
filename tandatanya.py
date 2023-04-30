from tkinter import *
from tkinter import messagebox as mb
import webbrowser


# declared functions to open website url
def urlpy(): 
    webbrowser.open('https://www.w3schools.com/python/default.asp')
def urlc():
    webbrowser.open('https://www.w3schools.com/c/index.php')
def urlcpp():
    webbrowser.open('https://www.w3schools.com/cpp/default.asp')
def urlcs():
    webbrowser.open('https://www.w3schools.com/cs/index.php')
def urljava():
    webbrowser.open('https://www.w3schools.com/java/default.asp')
def urlgo():
    webbrowser.open('https://www.w3schools.com/go/index.php')
def urlr():
    webbrowser.open('https://www.w3schools.com/r/default.asp')
def urlkotlin():
    webbrowser.open('https://www.w3schools.com/kotlin/index.php')

# declared functions to closed toplevel window (connected each other)
def closed1():
    winReg.destroy()
def closed2():
    winLog.destroy()

# declared functions to add userdata (register) and check user data (login)
def regisData():
    username = usernameRegis.get()
    password = passwordRegis.get()
    acc = 0

    file = open('userInfo.txt', 'r+')
    lines = file.readlines()
    if username == '' or password == '':
        acc = 1
    elif lines == []:
        acc = 2
    else:
        for line in lines: 
            line_split = line.split()
            if line_split[0]==username:
                acc = 0
                break
            else:
                acc = 2
    file.close()

    file = open('userInfo.txt', 'a')
    if acc == 0:
        mb.showerror('Error', 'Username Already Taken!')
    elif acc == 1:
        mb.showerror('Error', 'INVALID INFO!!')
    else:
        mb.showinfo('Register', 'Successfully Create your Account!')
        file.write(f'{username} {password} \n')
        closed1()

    file.close()

def loginData():
    username = usernameLogin.get()
    password = passwordLogin.get()
    acc = 0

    file = open('userInfo.txt', 'r+')
    for line in file:
        line_split = line.split()
        if line_split[0]==username and line_split[1]==password:
            acc = 1
            break
        else:
            acc = 0
            continue
        
    file.close()

    if acc == 1:
        mb.showinfo('Login', 'Login Successful!')
        closed2()
        mainMenu()
    else:
        mb.showerror('Error', 'Invalid Username or Password!')
         

# declared function for each toplevel window
def register():
    global entryArea, winReg
    global usernameRegis, passwordRegis
    
    winReg = Toplevel(window)
    winReg.title('Register')
    winReg.geometry('500x450')
    winReg.configure(bg=white)
    winReg.resizable(False, False) 
   
    
    # Text
    Label(winReg, image = icon, bg=white).place(x=250,y=100, anchor=CENTER)
    Label(winReg, text='Create your Account', 
          fg=black, bg=white,
          font=('Microsoft Yahei UI Light', 16, 'bold')).place(x=250,y=150, anchor=CENTER)
    
    # Entry Area
    entryArea = Frame(winReg, bg=white, width=250, height=200)
    entryArea.place(x=250, y=280, anchor=CENTER)
    # ---USERNAME---
    Label(entryArea, text='Username', bg=white, fg=black, font=('Microsoft Yahei UI Light', 10)).place(x=0, y=0, anchor=NW)
    userBorder = Frame(entryArea, bg=white, highlightbackground=black, highlightthickness=2, width=250, height=30)
    userBorder.place(x=0, y=21, anchor=NW)
    usernameRegis = Entry(userBorder, bg=white, fg=black, highlightbackground=blue, relief=FLAT, font=('Microsoft Yahei UI Light', 9))
    usernameRegis.place(x=0, y=0, anchor=NW)
    # ---PASSWORD---
    Label(entryArea, text='Password', bg=white, fg=black, font=('Microsoft Yahei UI Light', 10)).place(x=0, y=51, anchor=NW)
    passBorder = Frame(entryArea, bg=white, highlightbackground=black, highlightthickness=2, width=250, height=30)
    passBorder.place(x=0, y=71, anchor=NW)
    passwordRegis = Entry(passBorder, show='*', bg=white, fg=black, highlightbackground=blue, relief=FLAT, font=('Microsoft Yahei UI Light', 9))
    passwordRegis.place(x=0, y=0, anchor=NW)
    # ---BUTTON----
    newRegisterButton = Button(entryArea, text='Register', 
                         bg = blue, fg = white, bd=0, 
                         relief=FLAT, width=100, 
                         font=('Microsoft Yahei UI Light', 10), cursor='hand2', command=regisData)
    newRegisterButton['activeforeground'] = blue
    newRegisterButton['activebackground'] = white
    newRegisterButton.place(x = 125, y=130, anchor=CENTER)
    # ---DIRECT----
    Label(entryArea, text='Already have an Account?', bg=white, fg=black, font=('Microsoft Yahei UI Light', 9)).place(x=30, y=160, anchor=NW)    
    directLoginButton = Button(entryArea, text='Login', 
                               bg=white, fg=blue, bd=0, 
                               relief=FLAT, font=('Microsoft Yahei UI Light', 9), cursor='hand2', command=lambda:[login(), closed1()])
    directLoginButton['activeforeground'] = black
    directLoginButton['activebackground'] = white
    directLoginButton.place(x=180, y=158.5, anchor=NW)

def login():
    global winLog, usernameLogin, passwordLogin
    winLog = Toplevel(window)
    winLog.title('Login')
    winLog.geometry('500x450')
    winLog.configure(bg=white)
    winLog.resizable(False, False) 
    
    # Text
    Label(winLog, image = icon, bg=white).place(x=250,y=100, anchor=CENTER)
    Label(winLog, text='Log in to your Account', 
          fg=black, bg=white,
          font=('Microsoft Yahei UI Light', 16, 'bold')).place(x=250,y=150, anchor=CENTER)
    
    # Entry Area
    entryArea = Frame(winLog, bg=white, width=250, height=200)
    entryArea.place(x=250, y=280, anchor=CENTER)
    # ---USERNAME---
    Label(entryArea, text='Username', bg=white, fg=black, font=('Microsoft Yahei UI Light', 10)).place(x=0, y=0, anchor=NW)
    userBorder = Frame(entryArea, bg=white, highlightbackground=black, highlightthickness=2, width=250, height=30)
    userBorder.place(x=0, y=21, anchor=NW)
    usernameLogin = Entry(userBorder, bg=white, fg=black, highlightbackground=blue, relief=FLAT, font=('Microsoft Yahei UI Light', 9))
    usernameLogin.place(x=0, y=0, anchor=NW)
    # ---PASSWORD---
    Label(entryArea, text='Password', bg=white, fg=black, font=('Microsoft Yahei UI Light', 10)).place(x=0, y=51, anchor=NW)
    passBorder = Frame(entryArea, bg=white, highlightbackground=black, highlightthickness=2, width=250, height=30)
    passBorder.place(x=0, y=71, anchor=NW)
    passwordLogin = Entry(passBorder, show='*', bg=white, fg=black, highlightbackground=blue, relief=FLAT, font=('Microsoft Yahei UI Light', 9))
    passwordLogin.place(x=0, y=0, anchor=NW)
    # ---BUTTON----
    newLoginButton = Button(entryArea, text='Log in', 
                         bg = blue, fg = white, bd=0, 
                         relief=FLAT, width=100, 
                         font=('Microsoft Yahei UI Light', 10), cursor='hand2', command=loginData)
    newLoginButton['activeforeground'] = blue
    newLoginButton['activebackground'] = white
    newLoginButton.place(x = 125, y=130, anchor=CENTER)
    # ---DIRECT----
    Label(entryArea, text='Do not have an Account?', bg=white, fg=black, font=('Microsoft Yahei UI Light', 9)).place(x=30, y=160, anchor=NW)    
    directLoginButton = Button(entryArea, text='Register', 
                               bg=white, fg=blue, bd=0, 
                               relief=FLAT, font=('Microsoft Yahei UI Light', 9), cursor='hand2', command=lambda: [register(), closed2()])
    directLoginButton['activeforeground'] = black
    directLoginButton['activebackground'] = white
    directLoginButton.place(x=180, y=158.5, anchor=NW)

def mainMenu():
    global winMenu

    winMenu = Toplevel(window)
    winMenu.title('Tanda Tanya')
    winMenu.geometry('500x450')
    winMenu.configure(bg=white)
    winMenu.resizable(False, False)

    Label(winMenu, image = icon, bg=white).place(x=250,y=70, anchor=CENTER)
    Label(winMenu, text='Tanda Tanya', fg=black, bg=white,font=('Microsoft Yahei UI Light', 12, 'bold')).place(x=250,y=110, anchor=CENTER)
    Label(winMenu, text='Explore programming tutorial here', fg=black, bg=white,font=('Microsoft Yahei UI Light', 10)).place(x=250,y=135, anchor=CENTER)
    Label(winMenu, text='Copyright © 2023 Hanafi Pradja', fg=black, bg=white,font=('Microsoft Yahei UI Light', 9)).place(x=250,y=400, anchor=CENTER)

    mainFrame = Frame(winMenu, bg=white, width=400, height=250)
    mainFrame.place(x=250, y=280, anchor=CENTER)

    pyButton = Button(mainFrame, text='Python', width=20, 
                      bg=blue, fg=white, activebackground=white, 
                      activeforeground=blue, bd=0, 
                      relief=FLAT, font=('Microsoft Yahei UI Light', 9), 
                      cursor='hand2', command=urlpy)
    cbutton = Button(mainFrame, text='C', width=20, 
                      bg=blue, fg=white, activebackground=white, 
                      activeforeground=blue, bd=0, 
                      relief=FLAT, font=('Microsoft Yahei UI Light', 9), 
                      cursor='hand2', command=urlc)
    cppButton = Button(mainFrame, text='C++', width=20, 
                      bg=blue, fg=white, activebackground=white, 
                      activeforeground=blue, bd=0, 
                      relief=FLAT, font=('Microsoft Yahei UI Light', 9), 
                      cursor='hand2', command=urlcpp)
    csButton = Button(mainFrame, text='C#', width=20, 
                      bg=blue, fg=white, activebackground=white, 
                      activeforeground=blue, bd=0, 
                      relief=FLAT, font=('Microsoft Yahei UI Light', 9), 
                      cursor='hand2', command=urlcs)
    javaButton = Button(mainFrame, text='Java', width=20, 
                      bg=blue, fg=white, activebackground=white, 
                      activeforeground=blue, bd=0, 
                      relief=FLAT, font=('Microsoft Yahei UI Light', 9), 
                      cursor='hand2', command=urljava)
    goButton = Button(mainFrame, text='Go', width=20, 
                      bg=blue, fg=white, activebackground=white, 
                      activeforeground=blue, bd=0, 
                      relief=FLAT, font=('Microsoft Yahei UI Light', 9), 
                      cursor='hand2', command=urlgo)
    rButton = Button(mainFrame, text='R', width=20, 
                      bg=blue, fg=white, activebackground=white, 
                      activeforeground=blue, bd=0, 
                      relief=FLAT, font=('Microsoft Yahei UI Light', 9), 
                      cursor='hand2', command=urlr)
    kotlinButton = Button(mainFrame, text='Kotlin', width=20, 
                      bg=blue, fg=white, activebackground=white, 
                      activeforeground=blue, bd=0, 
                      relief=FLAT, font=('Microsoft Yahei UI Light', 9), 
                      cursor='hand2', command=urlkotlin)
    
    #grid
    pyButton.grid(row = 0, column=0, padx=8, pady=5)
    cbutton.grid(row = 1, column=0, padx=8, pady=5)
    cppButton.grid(row = 2, column=0, padx=8, pady=5)
    csButton.grid(row = 3, column=0, padx=8, pady=5)
    javaButton.grid(row = 0, column=1, padx=8, pady=5)
    goButton.grid(row = 1, column=1, padx=8, pady=5)
    rButton.grid(row = 2, column=1, padx=8, pady=5)
    kotlinButton.grid(row = 3, column=1, padx=8, pady=5)

# Main window
def mainWindow():
    global window, frame1 # Root and Frame
    global black, white, blue, grey # Color
    global icon # Image
    
    # Color
    black = '#1c1c1c'
    grey = '#f1f1f1'
    white = '#fff'
    blue = '#3466aa'

    # Root
    window = Tk()
    window.title('Tanda Tanya')
    window.geometry('500x450')
    window.configure(bg=white)
    window.resizable(False, False) 

    # Heading (Icon and Text)
    icon = PhotoImage(file = 'logotiny.png')
    window.iconphoto(True, icon)
    Label(image = icon, bg=white).place(x=250,y=130, anchor=CENTER)
    Label(text='Hi!, Welcome to Tanda Tanya', fg=black, bg=white,font=('Microsoft Yahei UI Light', 10)).place(x=250,y=180, anchor=CENTER)
    Label(text='Log in to continue', fg=black, bg=white,font=('Microsoft Yahei UI Light', 10)).place(x=250,y=200, anchor=CENTER)
    
    # Button Area
    frame1 = Frame(window, width=500, height=40, bg=white)
    frame1.place(x=250, y=250, anchor=CENTER)
    
    loginButton = Button(frame1, text='Log in', 
                         bg = blue, fg = white, bd=0, 
                         relief=FLAT, width=10, 
                         font=('Microsoft Yahei UI Light', 10), cursor='hand2', command=login)
    loginButton.place(x = 201, y=20, anchor=CENTER)
    loginButton['activeforeground'] = blue
    loginButton['activebackground'] = white

    regisButton = Button(frame1, text='Register',
                          bg = blue, fg = white, bd=0, 
                          relief=FLAT, width=10, 
                          font=('Microsoft Yahei UI Light', 10), cursor='hand2', command=register)
    regisButton['activeforeground'] = blue
    regisButton['activebackground'] = white
    regisButton.place(x = 300, y=20, anchor=CENTER)

    window.mainloop()


mainWindow()

