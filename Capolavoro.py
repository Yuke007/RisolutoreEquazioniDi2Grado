#Inizio del programma.
import math
#Definzione funzioni e procedure per le operazioni di 1 grado.
def proceduraPrimoGrado (b, c):
    if (c < 0):
        print(str(b) + "X - " + str(-c) + " =0")
    else:
        print(str(b) + "X + " + str(c) + " =0")
    print()
    
    print(str(b) + "X = " + str(-c))
    print()
    
    print("X = " + str(-c) + " / " + str(b) )
    print()
    
    if (b < 0) and (c > 0):
        print("X = " + str(c) + " / " + str(-b) )
    print()
    
    #Fine Definizione.

#Presentazione del programma.
def calcoloDelta(a, b, c):

    #calcolo del Delta.
    
    print ("Delta = b^2 - 4(a * c)")
    print ()
    
    if (b < 0):
        print ("Delta = (" + str(b) + ")^2 - 4(" + str(a) + " * " + str(c) + ")")
    else:
        print ("Delta = " + str(b) + "^2 - 4(" + str(a) + " * " + str(c) + ")")
    print()

    print ("Delta = " + str(b**2) + " -4(" + str(a*c) + ")")
    print ()
    
    print ("Delta = " + str(b**2) + str(-4*a*c) )
    print ()
    
    print ("Delta = " + str( (b**2) - 4 * (a*c) ) )
    print ()
    
    delta = (b**2) - 4*(a*c)
    
    if (delta > 0):
        print ("X1,2 = ( -b +- radq(Delta) ) / 2a")
        print ()
        
        print ("X1,2 = ( " + str(-b) + " +- radq(" + str(delta) + ") ) / (2 * " + str(a) + ")")
        print ()
        
        print ("X1,2 = ( " + str(-b) + " +- " + str(math.sqrt(delta)) + " ) / " + str(2*a))
        print ()
        
        print ("X1 = " + str(-b - math.sqrt(delta) ) + " / " + str(2*a) )
        print ()
        
        print ("X1 = " + str((-b - math.sqrt(delta)) / (2*a) ) )
        print ()
        
        print ("X2 = " + str(-b + math.sqrt(delta) ) + " / " + str(2*a) )
        print ()
        
        print ("X2 = " + str((-b + math.sqrt(delta)) / (2*a) ) )
        print ()
        
    elif (delta == 0):
        print ("X = -b / 2a")
        print ()
        
        print ("X = " + str(-b) + " / " + str(2*a) )
        print ()
        
        print ("X = " + str(-b / (2*a) ) )
        print ()
        
    else:
        print ("Calcolo impossibile, Delta non puo essere minore di 0")
        
    #Fine Definizione.

#Entry point.

#Presentazione.
print ("Questo programma scrive le risoluzioni e i passaggi delle operazioni di primo e secondo grado.")
  
#Chiedo i dati di a, b e c.
a = float(input("a = "))
print()

b = float(input("b = "))
print()

c = float(input("c = "))
print()

print(a)
print(b)
print(c)
#Fine inserimento dati.

#Controllo equazione per verificare se è di primo o secondo grado.

if (a == 0):
    print("è un'equazione di primo grado")
    print()
    if (b == 0):
        print("Non esiste nessuna X.")
    else: #La X esiste.
        X = -c / b
        proceduraPrimoGrado(b, c)
        print("X = " + str(X))
        
else: #(a != 0)
    
    print("è un'equazione di secondo grado")
    calcoloDelta(a, b, c)
    print()

input("Premi un tasto per continuare...")
#Exit point.
