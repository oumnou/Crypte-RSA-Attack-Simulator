
# Copyright
from functions import *
from tkinter import *
from PIL import ImageTk,Image
from sympy import *
import random



root = Tk()
root.title('RAS(RSAAttackSimulator)')
root.iconbitmap('img/pizza.ico')
root.maxsize(1100,1500)
# root.geometry("1000x2000")

a=Label(root, text="Oumaima",font=("Arial Bold",20))
a.grid(row=0, column=2)

my_img = Image.open("img/oum.png")

resize_image = my_img.resize((150,150), Image.ANTIALIAS)

my_pic = ImageTk.PhotoImage(resize_image)
my_label = Label(image=my_pic )
my_label.grid(row=0, column=0)

#n
b=Label(root, text="n")
b.grid(row=4, column=1)

n1 = Entry(root, width=35)
n1.grid(row=4, column=2)

#public key
b=Label(root, text="public key")
b.grid(row=6, column=1)

pu = Entry(root, width=35)
pu.grid(row=6, column=2)

#private key
p11=Label(root, text="private key")
p11.grid(row=8, column=1)

pr = Entry(root, width=35)
pr.grid(row=8, column=2)


#Button
s = Button(root, text="generate the keys",command = lambda :new())
s.grid(row=10, column=2)

#DISABLED
msg = Entry(root, width=35)
msg.grid(row=12, column=2)

r=Checkbutton(root, text=("Option"),command= lambda: Sign())
r.grid(row=12, column=1)


#Button
s = Button(root, text="Send" ,command = lambda: newmsg())
s.grid(row=12, column=3)

#Buttonkey
h = Button(root, text="keyToAyman" ,command= lambda: stillpublickey1())
h.grid(row=12, column=0)
############################ Alice


my_img3 = Image.open("img/send.png")

resize_image3 = my_img3.resize((150,150), Image.ANTIALIAS)

my_pic3 = ImageTk.PhotoImage(resize_image3)
my_label = Label(image=my_pic3)
my_label.grid(row=0, column=7)


############################ Ayman

a=Label(root, text="Ayman",font=("Arial Bold",20))
a.grid(row=0, column=11)



my_img2 = Image.open("img/mar.png")

resize_image2 = my_img2.resize((150,150), Image.ANTIALIAS)

my_pic2 = ImageTk.PhotoImage(resize_image2)
my_label = Label(image=my_pic2 )
my_label.grid(row=0, column=13)

#n
gg=Label(root, text="n")
gg.grid(row=4, column=10)

n2 = Entry(root, width=35)
n2.grid(row=4, column=11)

#public key
b=Label(root, text="public key")
b.grid(row=6, column=10)

pu2 = Entry(root, width=35)
pu2.grid(row=6, column=11)

#private key
b=Label(root, text="private key")
b.grid(row=8, column=10)

pr2 = Entry(root, width=35)
pr2.grid(row=8, column=11)

#Button
s = Button(root, text="generate the keys",command=lambda:newAyman())
s.grid(row=10, column=11)


#DISABLED
msg2 = Entry(root, width=35)
msg2.grid(row=12, column=11)

r=Checkbutton(root, text=("Option"))
r.grid(row=12, column=10)


#Button
h = Button(root, text="Send",command= lambda: newmsg2())
h.grid(row=12, column=12)

#Buttonkey
h = Button(root, text="keyToOumaima",command= lambda: stillpublickey())
h.grid(row=12, column=13)





############################################################################################################### BOB
#FENETRE 2
def new():
         global e
         global e1
         global eA
         lok = Toplevel()         
         lok.title('Generator')
         lok.iconbitmap('img/pizza.ico')
         
         #P
         b=Label(lok, text="P")
         b.grid(row=0, column=1)

         eA = Entry(lok, width=25)
         eA.grid(row=1, column=1)
         #Q
         bE=Label(lok, text="Q")
         bE.grid(row=0, column=3)

         e1 = Entry(lok, width=25)
         e1.grid(row=1, column=3)

        
         #ButtonExit

         s = Button(lok, text="exit",)
         s.grid(row=2, column=4 )
         #ButtonStart

         s = Button(lok, text="Start",command= lambda : getEntry())
         s.grid(row=2, column=2)

##############################

def stillpublickey1():
  buttan1 = Button(root, text="Key",background="#856ff8",command= lambda:publicKey1())
  buttan1.grid(row=0, column=8)


def publicKey1():
  AYA1=Toplevel()
  AYA1.title('Key to Ayman')

  #public key e
  Pk11=Label(AYA1, text="public key e :")
  Pk11.grid(row=0, column=0)
  Pkey11 = Entry(AYA1, width=35)
  Pkey11.grid(row=0, column=1)
  Pkey11.insert(0,public1[0])

 #public key n
  Pk11=Label(AYA1, text="public key n :")
  Pk11.grid(row=1, column=0)
  Pkey11 = Entry(AYA1, width=35)
  Pkey11.grid(row=1, column=1)
  Pkey11.insert(0,public1[1])

 #DONE
  Bkey1 = Button(AYA1,text="Done...",command= lambda:Done1())
  Bkey1.grid(row=2, column=0)

def Done1():
  n2.insert(0,public1[1])
  pu2.insert(0,public1[0])


##################################### HackerZone
frame = LabelFrame(root, text="Hacker zone", padx=50, pady=50)
frame.grid(row=20 , column=0,columnspan=40)

#Oumaima
b=Label(frame, text="Oumaima",font=("Arial Bold",20))
b.grid(row=21, column=4)
#n
b=Label(frame, text="n")
b.grid(row=22, column=0)

hack1 = Entry(frame, width=35)
hack1.grid(row=22, column=4)

#public key
b=Label(frame, text="public key")
b.grid(row=24, column=0)

key1 = Entry(frame, width=35)
key1.grid(row=24, column=4)

#private key
b=Label(frame, text="private key")
b.grid(row=26, column=0)

e = Entry(frame, width=35)
e.grid(row=26, column=4)


#Buttons
s = Button(frame, text="attacks",command=lambda:pirat())
s.grid(row=28, column=4)

#DISABLED
e = Entry(frame, width=35)
e.grid(row=30, column=4)

p13=Checkbutton(frame, text=("Sign"))
p13.grid(row=30, column=3)


#Button
s = Button(frame, text="Send")
s.grid(row=30, column=0)

############################ Alice





a=Label(frame, text="Ayman",font=("Arial Bold",20))
a.grid(row=21, column=20)

my_img4 = Image.open("img/hacker.png")

resize_image4 = my_img4.resize((150,150), Image.ANTIALIAS)

my_pic4 = ImageTk.PhotoImage(resize_image4)
my_label = Label(frame,image=my_pic4 )
my_label.grid(row=21, column=7)

#n
hack=Label(frame, text="n")
hack.grid(row=22, column=40)

hack2 = Entry(frame, width=35)
hack2.grid(row=22, column=20)

#public key
b=Label(frame, text="public key")
b.grid(row=24, column=40)

ep1 = Entry(frame, width=35)
ep1.grid(row=24, column=20)

#private key
b=Label(frame, text="private key")
b.grid(row=26, column=40)

e = Entry(frame, width=35)
e.grid(row=26, column=20)

#Button
s = Button(frame, text="attacks",command=lambda:pirat1())
s.grid(row=28, column=20)

#DISABLED
e = Entry(frame, width=35)
e.grid(row=30, column=20)

r=Checkbutton(frame, text=("Sign"))
r.grid(row=30, column=30)


#Button
s = Button(frame, text="Send")
s.grid(row=30, column=40)

def pirat():
  L,k=main(n)
  zoo=Toplevel()
  zoo.title('Attack')
  zoo.iconbitmap('img/pizza.ico')

#p
  p2=Label(zoo, text="p : ")
  p2.grid(row=2, column=0)

  p11 = Entry(zoo, width=25)
  p11.grid(row=2, column=1)
  p11.insert(0,L)

  #q
  q1=Label(zoo, text="n :")
  q1.grid(row=3, column=0)

  n11 = Entry(zoo, width=25)
  n11.grid(row=3, column=1)
  n11.insert(0,k)
  key1.insert(0,my_e)






















def newAyman():
         global e
         global pe
         global be
         global e2
         bok = Toplevel()         
         bok.title('Generator')
         bok.iconbitmap('img/pizza.ico')
         
         #P
         Pa=Label(bok, text="P")
         Pa.grid(row=0, column=1)

         pe= Entry(bok, width=25)
         pe.grid(row=1, column=1)
         #Q
         ba=Label(bok, text="Q")
         ba.grid(row=0, column=3)

         be = Entry(bok, width=25)
         be.grid(row=1, column=3)

        
         #ButtonExit

         s = Button(bok, text="exit",)
         s.grid(row=2, column=4 )
         #ButtonStart

         s = Button(bok, text="Start",command=lambda:getEntryA())
         s.grid(row=2, column=2)



def getEntryA():
         global phi
         global public2
         global my_e
         global private
         
         pe.insert(0,p)
         be.insert(0,q)
         n2.insert(0,n)
         my_e = exposant()
         d=inverse_modulaire(my_e,phi)
         public2 = (my_e,n)
         private = d
         pu2.insert(0,my_e)
         pr2.insert(0,d)
         print("la cle public est:",public2)
         print("la cle privée est:", private)

def newmsg2():
         butta = Button(root, text="New msg",background="#856ff8", command= lambda:getmsg1())
         butta.grid(row=0, column=3)
         hack2.insert(0,n)





def getEntry():
         global phi
         global my_e
         global private
         global public1
         eA.insert(0,p)
         e1.insert(0,q)
         n1.insert(0,n)
         my_e = exposant()
         d= inverse_modulaire(my_e,phi)
         public1 = (my_e,n)
         private = d
         pu.insert(0,my_e)
         pr.insert(0,d)
         print("la cle public est:",public1)
         print("la cle privée est:", private)


def newmsg():
         butt = Button(root, text="New msg",background="#856ff8", command= lambda:getmsg())
         butt.grid(row=0, column=10)
         hack1.insert(0,n)

     
        
def exposant():
         e=random.randrange(0, 10000)
         while pgcd(e,phi) !=1:
          e=random.randrange(0, 10000)
         print("L'exposant e = ",e)
         return e


def  getmsg():
         global top
         global chifreee
         global dechiffree
         msg1 = msg.get()
         print(msg1)
         a=chiffre(f[0], f[1], msg1)


         top = Toplevel()         
         top.title('Message')
         top.iconbitmap('img/pizza.ico')
        
         chifreee=chiffre(f[0], f[1], msg.get())
         print(chifreee)
         dechiffree=dechiffre(f[0], f[2], *chifreee)
         print("dechiffree : ",dechiffree)
         
         #M chifree
         b=Label(top,text="encrypted message :")
         b.grid(row=0, column=0)
         e = Entry(top, width=25)
         e.grid(row=0, column=1)
         e.insert(0,chifreee)
    
         
         botona = Button(top,text="show :",command=lambda: msg11())
         botona.grid(row=9, column=0)

         return chifreee

def msg11():
           #message dechiffre
         mm=Label(top, text="decrypted message : ")
         mm.grid(row=10, column=0)
        

         lo = Entry(top, width=25)
         lo.grid(row=10, column=1)
         lo.insert(0,dechiffree)

def Sign():
         s = [str(integer) for integer in getmsg()]
         a_string = "".join(s)

         res = int(a_string)

         print(res)
         print(type(res))
         S = (res**private) % n
         
         #Signature
         Sm=Label(top, text="Signature : ")
         Sm.grid(row=8, column=3)
         print("aicha")

         lo = Entry(top, width=25)
         lo.grid(row=9, column=3)
         lo.insert(0,S)


         pm=Label(top, text="Signature 2 : ")
         pm.grid(row=10, column=3)
         M1 = ((S**exposant()) % n)


         mo = Entry(top, width=25)
         mo.grid(row=9, column=3)
         mo.insert(0,M1)
         if M1 != S:
                  pm=Label(top, text="Message modifier")
                  pm.grid(row=11, column=3)
         return S

def stillpublickey():
  buttan = Button(root, text="Key",background="#856ff8",command= lambda:publicKey())
  buttan.grid(row=0, column=1)


def publicKey():
 
  AYA=Toplevel()
  AYA.title('Key to Oumaima')
 
  #public key e
  Pk1=Label(AYA, text="public key e :")
  Pk1.grid(row=0, column=0)
  Pkey1 = Entry(AYA, width=35)
  Pkey1.grid(row=0, column=1)
  Pkey1.insert(0,public2[0])

 #public key n
  Pk1=Label(AYA, text="public key n :")
  Pk1.grid(row=1, column=0)
  Pkey1 = Entry(AYA, width=35)
  Pkey1.grid(row=1, column=1)
  Pkey1.insert(0,public2[1])

 #DONE

  Bkey1 = Button(AYA,text="Done...",command= lambda:Done())
  Bkey1.grid(row=2, column=1)

def Done():
  n1.insert(0,public2[1])
  pu.insert(0,public2[0])


def  getmsg1():
         global pol
         global chifreee
         global dechiffree
         msg1 = msg.get()
         print(msg1)
         a=chiffre(f[0], f[1], msg1)


         pol = Toplevel()         
         pol.title('Message')
         pol.iconbitmap('img/pizza.ico')
        
         chifreee=chiffre(f[0], f[1], msg2.get())
         print(chifreee)
         dechiffree=dechiffre(f[0], f[2], *chifreee)
         print("dechiffree : ",dechiffree)
         
         #M chifree
         bq=Label(pol,text="encrypted message :")
         bq.grid(row=0, column=0)
         eq = Entry(pol, width=25)
         eq.grid(row=0, column=1)
         eq.insert(0,chifreee)
    
         
         botona0 = Button(pol,text="show :",command=lambda: msg111())
         botona0.grid(row=9, column=0)

         return chifreee

def msg111():
        #message dechiffre
         mm1=Label(pol, text="decrypted message : ")
         mm1.grid(row=10, column=0)
        

         lo1 = Entry(pol, width=25)
         lo1.grid(row=10, column=1)
         lo1.insert(0,dechiffree)



def getEntry():
         global phi
         global my_e
         global private
         global public1
         eA.insert(0,p)
         e1.insert(0,q)
         n1.insert(0,n)
         my_e = exposant()
         d= inverse_modulaire(my_e,phi)
         public1 = (my_e,n)
         private = d
         pu.insert(0,my_e)
         pr.insert(0,d)
         print("la cle public est:",public1)
         print("la cle privée est:", private)


def newmsg():
         butt = Button(root, text="New msg",background="#856ff8", command= lambda:getmsg())
         butt.grid(row=0, column=10)
         hack1.insert(0,n)

     
        
def exposant():
         e=random.randrange(0, 10000)
         while pgcd(e,phi) !=1:
          e=random.randrange(0, 10000)
         print("L'exposant e = ",e)
         return e


def  getmsg():
         global top
         global chifreee
         global dechiffree
         msg1 = msg.get()
         print(msg1)
         a=chiffre(f[0], f[1], msg1)


         top = Toplevel()         
         top.title('Message')
         top.iconbitmap('img/pizza.ico')
        
         chifreee=chiffre(f[0], f[1], msg.get())
         print(chifreee)
         dechiffree=dechiffre(f[0], f[2], *chifreee)
         print("dechiffree : ",dechiffree)
         
         #M chifree
         b=Label(top,text="encrypted message :")
         b.grid(row=0, column=0)
         e = Entry(top, width=25)
         e.grid(row=0, column=1)
         e.insert(0,chifreee)
    
         
         botona = Button(top,text="show :",command=lambda: msg11())
         botona.grid(row=9, column=0)

         return chifreee

def msg11():
           #message dechiffre
         mm=Label(top, text="decrypted message : ")
         mm.grid(row=10, column=0)
        

         lo = Entry(top, width=25)
         lo.grid(row=10, column=1)
         lo.insert(0,dechiffree)

def Sign():
         s = [str(integer) for integer in getmsg()]
         a_string = "".join(s)

         res = int(a_string)

         print(res)
         print(type(res))
         S = (res**private) % n
         
         #Signature
         Sm=Label(top, text="Signature : ")
         Sm.grid(row=8, column=3)
         print("aicha")

         lo = Entry(top, width=25)
         lo.grid(row=9, column=3)
         lo.insert(0,S)


         pm=Label(top, text="Signature 2 : ")
         pm.grid(row=10, column=3)
         M1 = ((S**exposant()) % n)


         mo = Entry(top, width=25)
         mo.grid(row=9, column=3)
         mo.insert(0,M1)
         if M1 != S:
                  pm=Label(top, text="Message modifier")
                  pm.grid(row=11, column=3)
         return S

def stillpublickey():
  buttan = Button(root, text="Key",background="#856ff8",command= lambda:publicKey())
  buttan.grid(row=0, column=1)


def publicKey():
 
  AYA=Toplevel()
  AYA.title('Key to Oumaima')
 
  #public key e
  Pk1=Label(AYA, text="public key e :")
  Pk1.grid(row=0, column=0)
  Pkey1 = Entry(AYA, width=35)
  Pkey1.grid(row=0, column=1)
  Pkey1.insert(0,public2[0])

 #public key n
  Pk1=Label(AYA, text="public key n :")
  Pk1.grid(row=1, column=0)
  Pkey1 = Entry(AYA, width=35)
  Pkey1.grid(row=1, column=1)
  Pkey1.insert(0,public2[1])

 #DONE

  Bkey1 = Button(AYA,text="Done...",command= lambda:Done())
  Bkey1.grid(row=2, column=1)

def Done():
  n1.insert(0,public2[1])
  pu.insert(0,public2[0])


  
def exposant():
         e=random.randrange(0, 10000)
         while pgcd(e,phi) !=1:
          e=random.randrange(0, 10000)
         print("L'exposant e = ",e)
         return e

def pirat1():
  L,k=main(n)
  zoo=Toplevel()
  zoo.title('Attack')
  zoo.iconbitmap('img/pizza.ico')

  
#p
  p2=Label(zoo, text="p : ")
  p2.grid(row=2, column=0)

  p11 = Entry(zoo, width=25)
  p11.grid(row=2, column=1)
  p11.insert(0,L)

  #q
  q1=Label(zoo, text="n :")
  q1.grid(row=3, column=0)

  n11 = Entry(zoo, width=25)
  n11.grid(row=3, column=1)
  n11.insert(0,k)
  ep1.insert(0,my_e)


frame.mainloop()