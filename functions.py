from tkinter import *
from PIL import Image
from sympy import *
from test import *
import random
import math 


def newAyman():
         global e
         global e1
         global e2
         bok = Toplevel()         
         bok.title('Generator')
         bok.iconbitmap('pizza.ico')
         
         #P
         b=Label(bok, text="P")
         b.grid(row=0, column=1)

         e = Entry(bok, width=25)
         e.grid(row=1, column=1)
         m = e.get()
         print(m)
         #Q
         b=Label(bok, text="Q")
         b.grid(row=0, column=3)

         e1 = Entry(bok, width=25)
         e1.grid(row=1, column=3)

        
         #ButtonExit

         s = Button(bok, text="exit",)
         s.grid(row=2, column=4 )
         #ButtonStart

         s = Button(bok, text="Start",command= lambda : getEntryA())
         s.grid(row=2, column=2)

def getEntryA():
         global phi
         global my_e
         global private
         p1 = e.insert(0,p)
         q1 = e1.insert(0,q)
         n2.insert(0,n)
         my_e = exposant()
         d=inverse_modulaire(my_e,phi)
         public = (my_e,n)
         private = d
         pu2.insert(0,my_e)
         pr2.insert(0,d)
         print("la cle public est:",public)
         print("la cle privée est:", private)

def newmsg():
         butt = Button(root, text="New msg",background="#856ff8", command= lambda:getmsg())
         butt.grid(row=0, column=10)
         hack2.insert(0,n)

def  getmsg():
         global pol
         global chifreee
         global dechiffree
         msg1 = msg.get()
         print(msg1)
         a=chiffre(f[0], f[1], msg1)


         pol = Toplevel()         
         pol.title('Message')
         pol.iconbitmap('pizza.ico')
        
         chifreee=chiffre(f[0], f[1], msg2.get())
         print(chifreee)
         dechiffree=dechiffre(f[0], f[2], *chifreee)
         print("dechiffree : ",dechiffree)
         
         #M chifree
         b=Label(pol,text="encrypted message :")
         b.grid(row=0, column=0)
         e = Entry(pol, width=25)
         e.grid(row=0, column=1)
         e.insert(0,chifreee)
    
         #e
         b=Label(pol, text="e : ")
         b.grid(row=2, column=0)

         e1 = Entry(pol, width=25)
         e1.grid(row=2, column=1)
         e1.insert(0,d)

         #n
         ol=Label(pol, text="n :")
         ol.grid(row=3, column=0)

         n1 = Entry(pol, width=25)
         n1.grid(row=3, column=1)
         n1.insert(0, f[0])
         
         m = e.get()
         botona = Button(pol,text="show :",command=lambda: msg11())
         botona.grid(row=9, column=0)

         print(m)
         return chifreee
       
def exposant():
         e=random.randrange(0, 10000)
         while pgcd(e,phi) !=1:
          e=random.randrange(0, 10000)
         print("L'exposant e = ",e)
         return e

def pgcd(e,phi):
    while (phi!=0):
        e,phi = phi,e%phi
    return e

def eugcd(e,phi):
    for i in range (1,phi):
        while(e!=0):
            a,b=phi//e,phi%e
            if(b!=0):
                print("%d=%d*(%d)+%d"%(phi,a,e,b))
            phi=e
            e=b

def eea (a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        math.gcd,s,t = eea(b,a%b)
        s = s-((a//b)*t)
        print("%d = %d*(%d)+(%d)*(%d)"%(math.gcd,a,t,s,b))
        return(math.gcd,t,s)

def inverse_modulaire(e,phi):
    math.gcd,s,_ = eea(e,phi)
    if(math.gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Puisque %d est inférieur à 0, s= s(mod phi), i.e., s=%d."%(s,s,s%phi))
        elif(s>0):
            print("s=%d."%(s))
        return s%phi

def generatePrimeNumbers():
  
    number  = 2
    c = 0
    
    while True:
      
        if not (number % 2 == 0 and number > 2):
         
            for divisor in range(3, int(sqrt(number))+1, 2):
                if number % divisor == 0:
                    c = 1
                    break
                    
            if  c != 1:
                yield number
                
        number += 1
        c = 0

def getPrimeFactors(multiple):

    primeNumbers = generatePrimeNumbers()

    output = []

    while multiple > 1:

        factor = next(primeNumbers)
        
        if multiple % factor == 0:
            output.append(factor)
            multiple /= factor
            primeNumbers = generatePrimeNumbers()
        else:
            continue
            
    return output

def main(number):
         y=[]
         primeFactors = getPrimeFactors(number)
         y.append((lambda x, y: str(x)+ "," + str(y), primeFactors))
         print(y)
         for i in y:
                  print(i[1])
         if len(i[1])==2:
                  return i[1][0],i[1][1]
         elif len(i[1])==3:
                  return i[1][0]*i[1][1],i[1][2]



def coupcoup(k, long):
	
	""""découpe des blocs de longueur long dans une chaine de caractères k et retourne une liste des blocs"""
	
	d , f = 0 , long
	
	
	l = []
	
	while f <= len(k):
		
		l.append(k[d:f])
		
		d , f = f , f + long
		
	
	m = len(k)%long
	
	if m != 0:
		
		l.append(k[len(k)-m:])
	
	return l



def pgcd(a,b):
	
	"""retourne le plus grand dénominateur commun de a et b"""
	
	while (b>0):
		
		r=a%b
		
		a,b=b,r
		
	return a
	
	
	
def pgcde(a, b):
	
	""" pgcd étendu avec les 2 coefficients de bézout u et v
	Entrée : a, b entiers
	Sorties : r = pgcd(a,b) et u, v entiers tels que a*u + b*v = r
	"""
	r, u, v = a, 1, 0
	rp, up, vp = b, 0, 1
	
	while rp != 0:
		q = r//rp
		rs, us, vs = r, u, v
		r, u, v = rp, up, vp
		rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)
	
	return (r, u, v)





def key():
	
	"""retourne un dictionnaire contenant la clé privée et la clé publique sous forme de tuples: {priv:(clé privée),pub:(clé publique)}"""
	
	#choix au hasard de deux entiers premiers (n et q)
	p = random.randrange(1,1000)
	q = random.randrange(1,1000)
	
	while isprime(p)==false:
		p =random.randrange(1,1000)
		
	while isprime(q) is False:
		q = random.randrange(1,1000)

	return p,q	
	#calcul de n et m


a=key()
p=int(a[0])
q=int(a[1])
phi = (int(p)-1)*(int(q)-1)

def key2():
	
	n = p*q
	m = (p-1)*(q-1)

	#recherche de c premier de m (c'est a dire tel que pgcd(m,c)=1 ) et de d = pgcde(m,c) tel que 2 < d < m
	r = 10
	d = 0
	while r != 1 or d <= 2 or d >= m:
		c = random.randrange(1,1000)
		r, d, v = pgcde(c,m)
		
	n, c, d = int(n), int(c), int(d)


	# return {"priv":(n,c), "pub":(n,d)}
	return n,c,d


	
def chiffre(n, c, msg):
	
	#conversion du message en codes ascii	
	asc = [str(ord(j)) for j in msg]
	
	#ajout de 0 pour avoir une longueur fixe (3) de chaque code asccii
	for i, k in enumerate(asc):
		
		if len(k) < 3:		
			
			while len(k) < 3:
				
				k = '0' + k
			
			asc[i] = k
				
	#formation de blocs de taille inferieure a n (ici blocs de 4)
	ascg = ''.join(asc)
	
	d , f = 0 , 4
	
	while len(ascg)%f != 0: #on rajoute eventuellement des 0 a la fin de ascg de maniere a ce que len(ascg) soit un multiple de f
		
		ascg = ascg + '0'

	l = []
	
	while f <= len(ascg):
		
		l.append(ascg[d:f])
		
		d , f = f , f + 4
			
	#chiffrement des groupes
	crypt = [str(((int(i))**c)%n) for i in l]
	
	return crypt
	

	
	
def dechiffre(n, d, *crypt):

	"""*crypt est une liste des blocks à déchiffrer"""
	
	
	#dechiffrage des blocs
	resultat = [str((int(i)**d)%n) for i in crypt]
		
		
	#on rajoute les 0 en debut de blocs pour refaire des blocs de 4
	for i, s in enumerate(resultat):
		
		if len(s) < 4:
			
			while len(s) < 4:
				
				s = '0' + s
			
			resultat[i] = s
		
		
	#on refait des groupes de 3 et on les convertie directement en ascii
	g = ''.join(resultat)
	
	asci = ''
	
	d , f = 0 , 3
	
	while f < len(g):
		
		asci = asci + chr(int(g[d:f])) #conversion ascii
		
		d , f = f , f + 3
	
	
	
	
	return asci
	



#return n,c,d
#def dechiffre(n, d, *crypt):
#def chiffre(n, c, msg):

f= key2()
k=key()

n=f[0]
c=f[1]
d=f[2]
	

# print(f)
# chifreee=chiffre(f[0], f[1], "hajiba")
# print(chifreee)
# dechiffree=dechiffre(f[0], f[2], *chifreee)
# print(dechiffree)
