import turtle
t = turtle.Turtle()
t.speed(0) # maximum speed
def equilateral(longueur):
    polygone(longueur,3)
    
def carre(longueur):
    polygone(longueur,4)

def polygone(longueur,nb_cote,ajout=0, deviation=0):
    angle = (360/nb_cote) - deviation
    for _ in range(nb_cote):
        longueur += ajout
        t.forward(longueur)
        t.left(angle)
        t.color("green", "red")

def figure1():
    polygone(0.5,360000,0.05,-15)

figure1()

        
turtle.exitonclick()
