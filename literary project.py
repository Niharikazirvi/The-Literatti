import requests
import webbrowser
from tkinter import *
import requests
from bs4 import BeautifulSoup as bs
import re
import pymysql

root = Tk()
root["bg"] = "#e6ffff"
root.geometry("1670x700")

#menubar
class profile_of_literattis:

    def __init__(self,imgpath,text1s,link):

        self.imgpath=imgpath
        self.text=text1s
        self.link=link


    def BioAndLink(self):
        toplevel = Toplevel()
        imgPath = self.imgpath
        photo = PhotoImage(file=imgPath)
        label2 = Label(toplevel,image=photo)
        label2.image = photo # keep a reference!
        label2.grid(row=0, column=1)
        label1 = Label(toplevel, text=self.text, height=10, width=100)
        label1.grid(row=1,column=1)

        def links():
            webbrowser.open(self.link)

        button = Button(toplevel, text="FOLLOW ME", command=links)
        button.grid(row=3,column=1)

    def cessLinks(self):
        toplevel = Toplevel()

        imgPath = self.imgpath
        photo = PhotoImage(file=imgPath)
        label2 = Label(toplevel, image=photo)
        label2.image = photo  # keep a reference!
        label2.grid(row=0)

        label1 = Label(toplevel, text=self.text, height=20, width=200)
        label1.grid(sticky='n')

        fblink = 'https://www.facebook.com/gnducess/?ref=br_rs'

        def links2():
            webbrowser.open(fblink)

        link1 = Button(toplevel, text='facebook', fg='white', bg='#406cb2', command=links2)
        link1.grid(sticky='n')

        instalink = 'https://www.instagram.com/cess.gndu/?hl=en'
        def links3():
            webbrowser.open(instalink)

        link2 = Button(toplevel, text='instagram', fg='white', bg='#406cb2',command=links3)
        link2.grid(sticky='n')

    def theLiterati(self):
        toplevel = Toplevel()

        imgPath = self.imgpath
        photo = PhotoImage(file=imgPath)
        label2 = Label(toplevel, image=photo)
        label2.image = photo  # keep a reference!
        label2.grid(row=0, column=1)

        label1 = Label(toplevel, text=self.text, height=20, width=100)
        label1.grid(row=1, column=1)

        def links():
             webbrowser.open(self.link)

        link0 = Button(toplevel, text='google', fg='white', bg='#406cb2', command=links)
        link0.grid(sticky='n')

        fblink = 'https://www.facebook.com/theliteratii/'

        def links2():
            webbrowser.open(fblink)

        link1 = Button(toplevel, text='facebook', fg='white', bg='#406cb2', command=links2)
        link1.grid(sticky='n')

        instalink = 'https://www.instagram.com/_theliterati_/'

        def links3():
            webbrowser.open(instalink)

        link2 = Button(toplevel, text='instagram', fg='white', bg='#406cb2', command=links3)
        link2.grid(sticky='n')

        def links(link):
            webbrowser.open(link)

    def about(self):
        toplevel = Toplevel()

        label=Label(toplevel,text='self.text',fg='black')
        label.pack()

##NIHARIKA
def objectCommand():
                                                                                                #     #s1=m
     s1=profile_of_literattis(r"C:\\Users\\niharika\\Desktop\\me and parneet\\New folder\\IMG-20171215-WA0017.gif",'I AM NIHARIKA\nFOLLOW ME ON MY BLOG\nFOLLOW ME','https://avalleroop.wordpress.com/')
                                                                                                 #s1=profile_of_literattis(s)
     s1.BioAndLink()


##NAVEEN
def objectCommand2():
    s1 = profile_of_literattis(r"C:\\Users\\niharika\\Desktop\\me and parneet\\New folder\\IMG-20171006-WA0207.gif",
                           'I AM NAVEEN\nFOLLOW ME ON MY BLOG\nFOLLOW ME', 'https://awistfulwind.wordpress.com/')
    s1.BioAndLink()

def objectCommand3():
    s1 = profile_of_literattis(r"C:\\Users\\niharika\\Desktop\\me and parneet\\New folder\\Screenshot_20180811-184611.gif",
                               'I AM PRATIKSHA\nFOLLOW ME ON MY BLOG\nFOLLOW ME', 'https://randomthoughts814.wordpress.com/')
    s1.BioAndLink()

###OBJECT ARTICLES MENU  ###@@@ PLOLYMORPHISM CAN BE USED HERE

def entertainment():
    URL = 'https://www.magzter.com/articles/Entertainment'
    webbrowser.open(URL)

def politics():
    URL = 'https://www.politico.com/'
    webbrowser.open(URL)

def lifestyle():
    URL = 'https://www.forbes.com/lifestyle/#6e7517222d15'
    webbrowser.open(URL)

def ourCulture():
    URL = 'https://www.incredibleindia.org/content/incredibleindia/en/experiences/art-and-culture.html'
    webbrowser.open(URL)

def sufiPoetry():
    URL = 'http://www.poetry-chaikhana.com/index.html'
    webbrowser.open(URL)

def punjabiPoetry():
    URL = 'http://www.punjabi-kavita.com/PunjabiPoetry.php'
    webbrowser.open(URL)

def englishPoetry():
    URL = 'https://www.poemhunter.com/'
    webbrowser.open(URL)

####CESS AND LITRATI OBJECTS

def objectcess():
    s1 = profile_of_literattis(r"C:\\Users\\niharika\\Desktop\\me and parneet\\New folder\\IMG-20180421-WA0018.gif",
                               "We are the COMPUTER ENGINEERING STUDENTS SOCIETY better known as CESS.\nWith the motive of 'GROWTH FOR ALL',we the students of department of computer engineering and technology,GNDU are trying to put our best efforts to bring the change by being the change.\nFor the growth of students in different in aspects of  life we have different teams.And one of them is literary team.\nTo know more click on the following links'" ,'http://cessgndu.com/#!/')
    s1.cessLinks()

def objectliteratis():
    s1 = profile_of_literattis(r"C:\\Users\\niharika\\Desktop\\me and parneet\\New folder\\IMG-20180421-WA0018.gif",
                                   "hello! welcome to our page.\nWe are the members of CESS' LITERARY TEAM  'The Literatti'.\nwe hope you enjoy reading our posts and many other stuff.\nWe organise various literary nd fun activities and tries to bring out the best of a literatti out of the peers who join us.\n\nFollow us on",
                                   'http://cessgndu.com/#!/team/8')
    s1.theLiterati()

def objectabout():
    s1=profile_of_literattis(r"C:\\Users\\niharika\\Desktop\\me and parneet\\New folder\\IMG-20180421-WA0018.gif",'To get any further information and help.\nContact on the following email ID\n202.niharikazirvi@gmail.com\nAny sugegstion are always welcome.')
    s1.about()


menubar = Menu(root)

root.config(menu=menubar)


our_litrattis = Menu(menubar, tearoff=0)
our_litrattis.add_command(label="NIHARIKA", command=objectCommand)
our_litrattis.add_command(label="NAVEEN", command=objectCommand2)
our_litrattis.add_command(label="PRATIKSHA", command=objectCommand3)
our_litrattis.add_separator()
our_litrattis.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="OUR LITRATTIS", menu=our_litrattis)

object_articles = Menu(menubar, tearoff=0)
object_articles.add_command(label="Entertainment", command=entertainment)#will provide the link the link toA= any particular website or any news blog
object_articles.add_command(label="politics", command=politics)
object_articles.add_command(label="lifestyle", command=lifestyle)
object_articles.add_command(label="our culture", command=ourCulture)
object_articles.add_separator()
object_articles.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="ARTISTIC ARTICLES", menu=object_articles)

object_poetry = Menu(menubar, tearoff=0)
object_poetry.add_command(label="Sufi", command=sufiPoetry)#will provide either the websites related to the genre
object_poetry.add_command(label="Punjabi poetry", command=punjabiPoetry)
object_poetry.add_command(label="English poetry", command=englishPoetry)
object_poetry.add_separator()
object_poetry.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="POISE POETRY", menu=object_poetry)

object_about = Menu(menubar, tearoff=0)
object_about.add_command(label="The litterati", command=objectliteratis)#will enherit the same class profile_of_litrattis
object_about.add_command(label="CESS", command=objectcess)#same classs with all the socila media links and use the same class s used above
object_about.add_command(label="HELP", command=objectabout)#contact of mine and my gmail id or any issue ralated to app
object_about.add_separator()
object_about.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="ABOUT", menu=object_about)

#left

#word od the day

URL='http://www.wordthink.com/?qt1m4dc=1'
URL2='http://www.eduro.com/?qt1m4dc=1'

r=requests.get(URL)
words=bs(r.text,'html.parser')

r2=requests.get(URL2)
words2=bs(r2.text,'html.parser')

word=words.find('div',class_='singlemeta')
#print(word.text)
meaning=word.text

word2=words2.find('div',class_='singlemeta')

for quotee in word2.find_all('div',class_='article'):
        quotes=quotee.text.strip()
all_word=meaning+quotes


S = Scrollbar(root,orient='vertical')
T= Text(root,width=30,wrap = "word",height=20,fg='#660000',bg='#ffe6e6')
T.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
T.tag_configure('big', font=('Verdana', 20, 'bold'))

S.pack(side=RIGHT, fill=Y)
T.place(x=100, y=30, width=200, height=300)
S.config(command=T.yview)
T.config(xscrollcommand=S.set)
T.insert(END, all_word)

#suggestion box


suggestion=Label(root,text='EVERY SUGGESTION BY YOUR SIDE IS WELCOME!',fg='#330026')
suggestion.place(x=100, y=400)

def retrieve_input():
    toplevel=Toplevel()
    def information():
        toplevel2=Toplevel()
        label1 = Label(toplevel2, text='Name')
        label1.grid(row=0, column=0)
        entry1 = Entry(toplevel2)
        entry1.grid(row=0, column=1)

        label3 = Label(toplevel2, text='email id')
        label3.grid(row=2, column=0)
        entry3 = Entry(toplevel2)
        entry3.grid(row=2, column=1)

        def inserting1():
            textinput = textBox.get('1.0', 'end-1c')
            name = entry1.get()
            email = entry3.get()

            db = pymysql.connect("localhost", "root", "N!harika25", "literary_project")
            cursor = db.cursor()
            sql1 = """INSERT INTO suggestions_section(SUGGESTIONS,NAME,EMAIL_ID)
                            VALUES('%s','%s','%s');""" % (textinput, name, email)

            try:
                cursor.execute(sql1)
                db.commit()
            except:
                db.rollback()
            db.close()

            toplevel2.destroy()
            toplevel.destroy()

        button = Button(toplevel2, text='submit', command=inserting1)
        button.grid(row=3, column=1)

    def inserting2():
        textinput = textBox.get('1.0', 'end-1c')

        db = pymysql.connect("localhost", "root", "N!harika25", "literary_project")
        cursor = db.cursor()
        sql1 = """INSERT INTO suggestions_section(SUGGESTIONS,NAME,EMAIL_ID)  VALUES('%s','%s','%s');""" % ( textinput,'anoymous','null')
        try:
            cursor.execute(sql1)
            db.commit()
        except:
            db.rollback()
        db.close()
        toplevel.destroy()

    var = IntVar()
    R1 = Radiobutton(toplevel, text="GO Anonyous", variable=var, value=1,
                     command=inserting2)
    R1.grid(row=0, column=1)

    R2 = Radiobutton(toplevel, text="Name", variable=var, value=2,
                     command=information)
    R2.grid(row=1, column=1)

textBox = Text(root,height=10,width=15,bg='#ecffb3',fg='#446600')
textBox.place(x=130, y=440, width=150, height=150)

buttonCommit=Button(root,height=2,width=5,text='commit',fg='#993366',bg='#e6b800',command=retrieve_input)
buttonCommit.place(x=180,y=600)


#middle

#photo of cess


imgPath = r"C:\Users\niharika\Desktop\me and parneet\New folder\literaryteampic.gif"
photo = PhotoImage(file=imgPath)
label2 = Label(root,image=photo,width=200,height=100,bg='#ffeb99')
label2.image = photo # keep a reference!
label2.place(x=450,y=25,width=500,height=300)
#books

def books():

    labela = Label(root, text='FOR BOOKishers', fg='#cc0000',font='BrookeShappell8')
    labela.place(x=650, y=335)

    def post_review():
        toplevel = Toplevel()
        labelb = Label(toplevel, text='Book name')
        labelb.grid(row=0, column=1)
        bookname = Entry(toplevel)
        bookname.grid(row=0, column=2)

        labeld = Label(toplevel, text='writer name')
        labeld.grid(row=1, column=1)
        writername = Entry(toplevel)
        writername.grid(row=1, column=2)

        labelc = Label(toplevel, text='Review')
        labelc.grid(row=2, column=1)
        reviewa = Text(toplevel, height=20, width=30)
        reviewa.grid(row=2, column=2, rowspan=4)

        def letsRockAndRoll():
            books = bookname.get()
            writers = writername.get()
            reviews = reviewa.get('1.0', END)
            if kind_lender==1:
                mail = giversEmail.get()

                db = pymysql.connect("localhost", "root", "N!harika25", "literary_project")
                cursor = db.cursor()

                sql1 = """INSERT INTO review_section1(BOOK,WRITER,REVIEW,kIND_LENDER,EMAIL) VALUES('%s','%s','%s','%s','%s');""" % (
                    books, writers, reviews, 1, mail)
            else:
                db = pymysql.connect("localhost", "root", "N!harika25", "literary_project")
                cursor = db.cursor()

                sql1 = """INSERT INTO review_section1(BOOK,WRITER,REVIEW,KIND_LENDER) VALUES('%s','%s','%s','%s','%s');""" % (
                    books, writers, reviews, 0, 'null')

            try:
                cursor.execute(sql1)
                db.commit()
            except:
                db.rollback()

            db.close()
            if kind_lender==1:
                toplevelv.destroy()
                toplevel.destroy()
            else:
                toplevel.destroy()

        def info_about_giver():
            global toplevelv
            toplevelv = Toplevel()

            global kind_lender
            kind_lender = 1

            labelf = Label(toplevelv,
                           text="You can give your email_id here so that if any borrower will be interested in borrowing your book.\nwe will send you notification with the borrower's email id so that you can contact the former according to your own convenience.")
            labelf.grid(row=0, column=0)

            labele = Label(toplevelv, text='EMAIL_ID')
            labele.grid(row=1, column=0)

            global giversEmail
            giversEmail = Entry(toplevelv)
            giversEmail.grid(row=2, column=0)

            submitButton = Button(toplevelv, text='Submit', command=letsRockAndRoll)
            submitButton.grid(row=3, column=0)



        ####option for sharing
        var = IntVar()
        radiobuttona = Radiobutton(toplevel, text='willing to lend your book', variable=var, value=1,
                                   command=info_about_giver)  # ,command=sharin_details)
        radiobuttona.grid(row=6, column=1)

        radiobuttonb = Radiobutton(toplevel, text='not willing to share', variable=var, value=2,
                                   command=letsRockAndRoll)
        radiobuttonb.grid(row=7, column=1)

    buttona = Button(root, text='POST REVIEW', command=post_review,fg='#993333',bg='#ff8566')
    buttona.place(x=650, y=365)

    labeld = Label(root, text='REVIEWS',fg='#4d3900')
    labeld.place(x=670,y=395)

    labelbooks = Label(root,fg='#cc3300',
                       text='Click on the BOOK from the list below to read the  reviews posted by readers abouth that book.\nYou can also see for the TO BORROW option if u want to borrow any particular book\n by providing ur contact information so as it let the lender know about you.')
    labelbooks.place(x=430, y=415)

    def list_of_books():
        #books_in_database = []

        db = pymysql.connect("localhost", "root", "N!harika25", "literary_project")
        cursor = db.cursor()
        sql = '''SELECT BOOK FROM review_section1 '''
        listbox = Listbox(root, bg='#ffffcc', fg='#999966', selectmode=EXTENDED)
        listbox.place(x=650, y=500)

        #bookList = cursor.execute(sql)
        #
        # for book in bookList:
        #     books_in_database.append(book)
        global books_in_database
        final_result=[]
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            final_result.append(i)
        print(final_result)                                    #######how can we insert the column data directly into listbox ...coz otherwise the data in listbox is being insert as a tuples
                                                    ###and thats why when the book in the list box is clicked is it not being rcognized as a single object aand nothing is selcted...and it shos error
                                                ### tuple object is empty ssomething...
        # final_result=[]
        # final_result = [list(i) for i in result]
        # books_in_database = list(cursor.fetchall())
        # print(books_in_database)

        for item in final_result:
            listbox.insert(END, item)

        # try:
        #     bookList = cursor.execute(sql)
        #     #
        #     # for book in bookList:
        #     #     books_in_database.append(book)
        #     global books_in_database
        #     books_in_database=list(bookList)
        #     print(books_in_database)
        #
        #     for item in books_in_database:
        #         listbox.insert(END, item)
        # except:
        #     listbox.insert(END,'nuli')
        #     # if not books_in_database:
        #     #     label = Label(root,text="No books are available as the listbox is empty this time")
        #     #     label.place(x=550, y=470)
        #     # else:
        #     #     label = Label(root, text="error")
        #     #     label.place(x=550, y=470)
        #     # msg = Message(root, text="error")
        #     # msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        #     # msg.pack()


        db.close()


        def availability():
            if kindLender == 1:
                toplevel = Toplevel()
                available = "THIS BOOK IS AVAILABLE FOR BORROWING.THE OWNER OF THIS BOOK  WILL CONTACT YOU ON HIS/HER OWN CONVENIENCE AND AVAILABILITY OF BOOK.\n MAY CONTACT YOU ON THE EMAIL ID YOU PROVIDE BELOW.\n"
                front = Label(toplevel, text=available)
                front.grid(row=0)
                title = Label(toplevel, text="availability")
                title.grid(row=1)
                entry1 = Label(toplevel, text="email ID")
                entry1.grid(row=2, column=1)
                entry = Entry(toplevel)
                entry.grid(row=2, column=2)

            else:
                toplevel = Toplevel()
                available = "THIS BOOK IS NOT AVAILABLE FOR BORROWING.SORRY!"
                front = Label(toplevel, text=available)
                front.grid(row=0)
                msg = Message(toplevel, text="availabity")
                msg.config(bg='lightgreen', font=('times', 24, 'italic'))
                msg.grid()

            toplevel.destroy()

        def book_review(event):

            # value = event.widget.get(event.widget.curselection()[0])
            # print(value)
            value=listbox.curselection()[0]
            index = listbox.get(value)
            print(index)

            toplevel = Toplevel()
            db = pymysql.connect("localhost", "root", "N!harika25", "literary_project")
            cursor = db.cursor()
            sql = '''SELECT REVIEW,KIND_LENDER FROM review_section1 WHERE BOOK=%s'''%(index )
            try:

                global kindlender
                cursor.execute(sql)
                result1,kindlender=cursor.fetchall()
                labelb = Label(toplevel, text=result1)
                labelb.pack()
            except:
                labelb = Label(toplevel, text="No review available")
                labelb.pack()
            db.close()

            buttonb = Button(toplevel, text='Availabity for borrowing', command=availability)
            buttonb.pack()

            toplevel.destroy()
        listbox.bind('<Button-1>', book_review)
        listbox.place(x=650, y=500)



    list_of_books()


books()

#right

#membership

class new_member():                          ###@@@could have directlt msde it function...
    def __init__(self):

        self.toplevel=Toplevel(root)
        self.label1 = Label(self.toplevel, text='first_name')
        self.label1.grid(row=0, column=0)
        self.entry1 = Entry(self.toplevel)
        self.entry1.grid(row=0, column=1)

        self.label2 = Label(self.toplevel, text='last_name')
        self.label2.grid(row=1, column=0)
        self.entry2 = Entry(self.toplevel)
        self.entry2.grid(row=1, column=1)

        self.label3 = Label(self.toplevel, text='email id')
        self.label3.grid(row=2, column=0)
        self.entry3 = Entry(self.toplevel)
        self.entry3.grid(row=2, column=1)

        self.label4 = Label(self.toplevel, text='City')
        self.label4.grid(row=3, column=0)
        self.entry4 = Entry(self.toplevel)
        self.entry4.grid(row=3, column=1)

        self.label5 = Label(self.toplevel, text='profession')
        self.label5.grid(row=4, column=0)
        self.entry5 = Entry(self.toplevel)
        self.entry5.grid(row=4, column=1)

        self.button = Button(self.toplevel, text='ok',command=self.inserting)
        self.button.grid(row=5, column=1)

    def inserting(self):
        firstname = self.entry1.get()
        lastname = self.entry2.get()
        emailidname = self.entry3.get()
        cityname = self.entry4.get()
        professionname = self.entry5.get()

        self.db = pymysql.connect("localhost", "root", "N!harika25", "literary_project")
        self.cursor = self.db.cursor()

        self.sql1 = """INSERT INTO membership_form(FIRST_NAME,
                 LAST_NAME,EMAIL_ID,CITY,PROFESSION)
                 VALUES('%s','%s','%s','%s','%s');"""%(firstname,lastname,emailidname,cityname,professionname)
        try:
            self.cursor.execute(self.sql1)
            self.db.commit()
            w = Message(root, text="Welcome to the team!",fg='#330a00',bg='#ff3300')
            w.pack()

        except:
            self.db.rollback()
        self.db.close()
        self.toplevel.destroy()

def call():
    e1=new_member()

labelm=Label(root,text='Want to be Member of THE LITERATI!\nJust click below',fg='#cc6600')
labelm.place(x=1100,y=100)
buttonm=Button(root,text='FILL ME',bg='#eaf4b2',fg='#5d9152',width=20,command=call)
buttonm.place(x=1120,y=140)
###hukumnama


URL='http://hukamnamasahib.com/2018/12/sandhia-vele-da-hukamnama-sri-darbar-sahib-amritsar-date-30-december-2018-ang-683/'
r=requests.get(URL)
words=bs(r.text,'html.parser')
word=words.find('div',class_='entry-content')
hukumnama=word.text

S1 = Scrollbar(root,orient='vertical')
T1= Text(root,width=30,wrap = "word",height=20,fg='#009999',bg='#cce6ff')
T1.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
T1.tag_configure('big', font=('Verdana', 20, 'bold'))

S1.pack(side=RIGHT, fill=Y)
T1.place(x=1050,y=250,height=300)
S1.config(command=T1.yview)
T1.config(xscrollcommand=S1.set)
T1.insert(END,hukumnama)



mainloop()

##good hukumnama app fo web scrapping that must show everyday hukumnama
##change the photoas of cess and literatti in menubar