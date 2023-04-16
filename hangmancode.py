#kan importiw libraries li ghadi nkhdmou bihoum
import random
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
#creation dyal awal window
windoww=Tk()
windoww.title("HANGMAN GAME BY CHAIMAE BOULTAM & MERIEME BOUDRAA")
windoww.geometry("800x500")
windoww.config(bg='#2D2D2B')
width=windoww.winfo_width()
height=windoww.winfo_height()
x=(width//2)+300
y=(height//2)+90
windoww.geometry(f"+{x}+{y}")
lb=Label(windoww, text="Welcome to",font=('Times',25),bg='#2D2D2B',fg='#E1BC27')
lb.pack()
# create a PhotoImage object from the image file
photo = PhotoImage(file="C:\\Users\\user\\Desktop\\fichhh\\tsiwrat\\HangmanGame\\00HANG00.png")

# create a Tkinter label with the image
label = Label(windoww, image=photo)
label.pack()
btn=Button(windoww,text="LET'S GOO",font=("Times 20 bold"),fg='Black',bg='#E1BC27', width=12,height=2,command=lambda:categorie(windoww))
btn.pack()

#creation de la fonction utilisé pour affifcher les categories
def categorie(windoww):
    windoww.withdraw()
    window1=Toplevel()
    window1.title("HANGMAN GAME BY CHAIMAE BOULTAM & MERIEME BOUDRAA")
    window1.geometry("350x300")
    width=window1.winfo_width()
    height=window1.winfo_height()
    x=(width//2)+500
    y=(height//2)+200
    window1.geometry(f"+{x}+{y}")
 


    
#creating categories lighaykhtar l user
    global categories 
    global selected_category
    categories = {
        "Animals": ["LION", "TIGER", "ELEPHANT", "GIRAFFE", "ZEBRA"],
        "Numbers": ["ONE","THREE"],
        "Mounths": ["JANUARY","FEBRUARY","MARCH","AVRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"],
        "Days": ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"],
        "Fruits": ["APPLE","STRAWBERRY","MANGO","KIWI","GRAPES","ORANGE","WATERMELON","MELON","BANANA","PINEAPPLE","CHERRY","AVOCADO","PAPAYA","PEACH","PEAR"],
        "Vegetables": ["TOMATO","POTATO","CARROT","ONION","BROCCOLI","CORN","CUCUMBER","RADISH","BEANS","PUMPKIN"],
        }
    #creating a frame li katkawan mn label w menu
    category_frame = Frame(window1)
    category_frame.pack(expand=TRUE)  
    choose_category = Label(category_frame, text="  Choose a Category:",font=('Broadway 20'),fg='Black')
    choose_category.grid(row=0,sticky="n",pady = 30)
    selected_category = StringVar()
    category_options = OptionMenu(category_frame,selected_category, *categories.keys())
    category_options.config(bg='#E1BC27')
    category_options.grid(row=0,sticky="n",pady = 73)
    # button to start the game
    start_button = Button(category_frame, text="Start",font=('Times',15),bg='Black',fg='#E1BC27' ,command=lambda:game(window1))
    start_button.grid(row=0,sticky="e")
    windoww.mainloop()


#create a window with a title
def game(window1):
    window1.withdraw()
    window=Toplevel()
    width=window.winfo_width()
    height=window.winfo_height()
    x=(width//2)+300
    y=(height//2)+90
    window.geometry(f"+{x}+{y}")
    window.title("HANGMAN GAME BY CHAIMAE BOULTAM & MERIEME BOUDRAA")
    #importing pictures li ghan7tajou
    photo = [
        PhotoImage(file="C:\\Users\\user\\Desktop\\fichhh\\tsiwrat\\HangmanGame\\hangman0.png"),
        PhotoImage(file="C:\\Users\\user\\Desktop\\fichhh\\tsiwrat\\HangmanGame\\hangman1.png"),
        PhotoImage(file="C:\\Users\\user\\Desktop\\fichhh\\tsiwrat\\HangmanGame\\hangman2.png"),
        PhotoImage(file="C:\\Users\\user\\Desktop\\fichhh\\tsiwrat\\HangmanGame\\hangman3.png"),
        PhotoImage(file="C:\\Users\\user\\Desktop\\fichhh\\tsiwrat\\HangmanGame\\hangman4.png"),
        PhotoImage(file="C:\\Users\\user\\Desktop\\fichhh\\tsiwrat\\HangmanGame\\hangman5.png"),
        PhotoImage(file="C:\\Users\\user\\Desktop\\fichhh\\tsiwrat\\HangmanGame\\hangman6.png")
        ]


    

    #creating a function kat affichi awal image wl word ela chkal '_' 
    def newgame():
        global thewordwithspace
        global numberofguesses
        global word
        numberofguesses = 0
        word = random.choice(categories[selected_category.get()])
        imglabel.config(image=photo[0])
        thewordwithspace = " ".join(word)
        lbword.set(" ".join("_" * len(word)))
    #exit button
    Button(window, text="EXIT", command=exit, font=("Times 13 bold"), bg="Black", fg="#E1BC27").grid(row=0, column=8 ,sticky="ne")
    #position de l'image
    imglabel = Label(window)
    imglabel.grid(row=0, columnspan=5, column=0, padx=60, pady=80)
    imglabel.config(image=photo[0])
    #position du mot
    lbword = StringVar()
    Label(window, textvariable=lbword, bd=8, relief="groove", font=("Times 30 bold")).grid(row=0, column=3, columnspan=6,)
    #creat a keyboard
    n = 0
    for c in ascii_uppercase:
        Button(window, text=c, command=lambda c=c: guess(c), font=("Broadway 20"), width=4, bg="#E1BC27", fg="black").grid(row=1 + n // 9, column=n % 9)
        n += 1
    #creat new game button
    Button(window, text="NEW\nGAME", command=lambda: categorie(window), font=("Times 13 bold"), bg="Black", fg="#E1BC27" ,width=7,height=2,).grid(row=3, column=8)
    #function kadir koulchi
    def guess(letter):
        global thewordwithspace
        global numberofguesses
        global word
        if numberofguesses < 6:
            txt = list(thewordwithspace)
            guesses = list(lbword.get())
            if letter in thewordwithspace:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guesses[c] = letter
                lbword.set("".join(guesses))
                if lbword.get() == thewordwithspace:
                    messagebox.showinfo("Hangman", "Congratulations! You win!")
            else:
                numberofguesses = numberofguesses + 1
                imglabel.config(image=photo[numberofguesses])
                if numberofguesses == 6:
                    messagebox.showerror("Hangman", f"Game over! the word is {word}")
    window.resizable(width=False,height=FALSE)     
    newgame()
    window.mainloop()
windoww.mainloop()