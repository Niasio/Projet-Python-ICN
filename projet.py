"""

        ########################################################
        #                                                      #
        #      Créer par Jimmy Fontaine et Thomas Blanquet     #
        #               Création en Libre Accès                #
        #                       GitHub:                        #
        #      https://github.com/Niasio/Projet-Python-ICN     #
        #                                                      #
        ########################################################

"""
from turtle import *

taille = 20
angle = 30

title("ICN -- Projet Python")

################################################################################
################################################################################

speed("fastest")

################################################################################
################################################################################

ht()

tquadrillage = Turtle()
tquadrillage.ht()

tcathe = Turtle()
tcathe.ht()

tarbre = Turtle()
tarbre.ht()

tmenu = Turtle()
tmenu.ht()

################################################################################
################################################################################

#Valeur conseillée: a=0 b=700
def axex(a,b):
    tquadrillage.up()
    tquadrillage.goto(-1000,b)
    tquadrillage.down()
    while(a<1000):
        tquadrillage.forward(2500)
        b=b-taille
        a=a+10
        tquadrillage.up()
        tquadrillage.goto(-1000,b)
        tquadrillage.down()

#Valeur conseillée: a=0 b=-1000
def axey(a,b):
    tquadrillage.up()
    tquadrillage.goto(-1000,b)
    tquadrillage.down()
    tquadrillage.right(90)
    while(a<1000):
        tquadrillage.forward(2500)
        b=b+taille
        a=a+10
        tquadrillage.up()
        tquadrillage.goto(b,700)
        tquadrillage.down()

def quadrillage():
    tquadrillage.color("black")
    tquadrillage.width(1)
    tquadrillage.speed("fastest")
    axex(0,700)
    axey(0,-1000)
    tquadrillage.up()
    tquadrillage.goto(0,0)
    tquadrillage.seth(90)
    tquadrillage.down()

################################################################################
################################################################################

def changecolor(x=0, y=0):
    global colordown

    colordown = colordown[1:]+colordown[:1]
    color(colordown[0])

def changetaille(x=0, y=0):
    global taillepen

    taillepen = taillepen[1:]+taillepen[:1]
    width(taillepen[0])

def switchuppen(a=0, b=0):
    global colordown

    if pen()["pendown"]:
        end_fill()
        up()
        color("#95a5a6")
    else:
        down()
        colordown=["#1abc9c", "#2ecc71", "#3498db", "#9b59b6", "#34495e",
                    "#f1c40f", "#e67e22", "#e74c3c", "#ecf0f1"]
        color(colordown[0])
        begin_fill()


def menudessin(a,b,c):
    tmenu.up()
    tmenu.goto(950,180)
    tmenu.down()
    tmenu.width(5)
    tmenu.color("#16a085")
    tmenu.fillcolor("#1abc9c")
    tmenu.begin_fill()
    while(a<5):
        tmenu.rt(45)
        tmenu.forward(b)
        tmenu.rt(45)
        tmenu.forward(c)
        a=a+1
    tmenu.end_fill()

    tmenu.up()
    tmenu.goto(630,450)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("F1 - Changer la Couleur", font=("Arial", 20, "normal"))

    tmenu.up()
    tmenu.goto(630,400)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("F2 - Changer la Taille", font=("Arial", 20, "normal"))

    tmenu.up()
    tmenu.color("black")
    tmenu.goto(0,0)
    tmenu.down()

def déplacement():
    global taillepen

    taillepen=["1","2","3","4","5","6","7","8","9","10"]

    menudessin(0,25,300)
    seth(90)
    st()
    speed(5)
    shape("circle")
    shapesize(1)
    width(taillepen[0])
    switchuppen()
    ondrag(goto,1)
    onscreenclick(goto,1)
    onscreenclick(switchuppen,3)
    onkey(changecolor, "F1")
    onkey(changetaille, "F2")


################################################################################
################################################################################

def cathedrale():
    tcathe.seth(0)
    tcathe.width(3)
    tcathe.up()
    tcathe.goto(100,0)
    tcathe.down()
    tcathe.lt(90)
    tcathe.forward(175)

    tcathe.up()
    tcathe.goto(-100,0)
    tcathe.down()

    tcathe.forward(175)
    tcathe.up()
    tcathe.goto(73.5,0)

    tcathe.down()
    tcathe.circle(73.5)
    tcathe.up()
    tcathe.goto(80.25,0)
    tcathe.lt(180)
    tcathe.down()

    tcathe.circle(-80.25,180)
    tcathe.up()
    tcathe.goto(-80.25,0)
    tcathe.down()
    tcathe.circle(-160.5,60 )
    tcathe.up()

    tcathe.goto(80.25,0)
    tcathe.lt(90)
    tcathe.down()
    #circle(160.5,60)
    print(tcathe.heading())
    tcathe.lt(240)
    tcathe.lt(90)

    tcathe.up()
    tcathe.goto(80.25,0)
    tcathe.down()
    tcathe.circle(160.5,60 )
    tcathe.rt(240)
    tcathe.rt(90)
    tcathe.up()
    tcathe.goto(100,0)
    tcathe.down()
    tcathe.rt(270)
    tcathe.forward(175)
    tcathe.lt(90)
    print(tcathe.heading())
    tcathe.up()
    tcathe.goto(-100,0)
    tcathe.down()
    tcathe.rt(90)
    tcathe.forward(175)

    tcathe.rt(90)
    tcathe.forward(50)
    tcathe.rt(90)
    tcathe.forward(350)
    tcathe.rt(180)
    tcathe.forward(350)
    tcathe.rt(90)

    def b():
        tcathe.circle(5,180)
        tcathe.forward(300)
        tcathe.circle(5,180)
        tcathe.forward(300)
    b()

    tcathe.rt(90)
    tcathe.forward(350)
    tcathe.lt(90)

    b()

    tcathe.up()
    tcathe.goto(150,-175)
    tcathe.down()
    tcathe.rt(90)
    tcathe.forward(350)

    tcathe.up()
    tcathe.goto(150,-175)
    tcathe.down()
    tcathe.rt(180)
    tcathe.forward(300)
    tcathe.up()
    tcathe.goto(-150,-175)
    tcathe.down()

    tcathe.forward(300)
    tcathe.lt(90)
    tcathe.forward(100)
    tcathe.up()
    tcathe.goto(100,175)
    tcathe.down()
    tcathe.lt(90)
    tcathe.forward(80)
    tcathe.up()
    tcathe.goto(-100,175)
    tcathe.down()
    tcathe.forward(80)
    tcathe.rt(30)
    tcathe.forward(200)
    tcathe.rt(120)
    tcathe.forward(200)

    tcathe.up()
    tcathe.goto(150,175)
    tcathe.down()
    print(tcathe.heading())
    tcathe.lt(60)
    tcathe.lt(90)
    tcathe.forward(80)
    tcathe.up()
    tcathe.goto(-150,175)
    tcathe.down()
    print(tcathe.heading())
    tcathe.forward(80)

    tcathe.rt(30)
    tcathe.forward(300)
    tcathe.rt(120)
    tcathe.forward(300)
    print(tcathe.heading())
    tcathe.up()
    tcathe.goto(150,175)
    tcathe.down()

################################################################################
################################################################################

#Arbre Fractal
def arbreentier():

    tarbre.seth(0)

    tarbre.up()
    tarbre.goto(pos())
    tarbre.down()

    def arbrepartie(n, longueur):
        if n == 0:
            tarbre.color("red")
            tarbre.fd(longueur)
            tarbre.backward(longueur)
            tarbre.color("black")
        else :
            tarbre.width(n)
            tarbre.forward(longueur/3)
            tarbre.left(angle)
            arbrepartie(n-1 , longueur/3 * 2)
            tarbre.right(2*angle)
            arbrepartie(n-1 , longueur/3 * 2)
            tarbre.lt(angle)
            tarbre.back(longueur/3)

    tarbre.lt(90)
    tarbre.ht()
    arbrepartie(11,500)

################################################################################
################################################################################

def menu(a,b,c):

    delay(0)

    tmenu.up()
    tmenu.goto(-630,500)
    tmenu.down()
    tmenu.width(5)
    tmenu.color("#16a085")
    tmenu.fillcolor("#1abc9c")
    tmenu.begin_fill()
    while(a<5):
        tmenu.rt(45)
        tmenu.forward(b)
        tmenu.rt(45)
        tmenu.forward(c)
        a=a+1
    tmenu.end_fill()

    tmenu.up()
    tmenu.goto(-930,450)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("A - Quadrillage", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.goto(-930,400)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("B - Cathédrale", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.goto(-930,350)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("C - Coloriage", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.goto(-930,300)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("D - Arbre", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.color("black")
    tmenu.goto(0,0)
    tmenu.down()

################################################################################
################################################################################

menu(0,25,300)

################################################################################
################################################################################

onkey(quadrillage,"a")
onkey(cathedrale,"b")
onkey(déplacement,"c")
onkey(arbreentier,"d")
listen()

################################################################################
################################################################################

mainloop()

################################################################################
################################################################################