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
from time import *
from math import sin, cos, pi
import math

taille = 20
angle = 30

title("ICN -- Projet Python")

screensize(1920, 1080)

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

tmenu1 = Turtle()
tmenu1.ht()

tsave = Turtle()
tsave.ht()

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

def cachequadri():
    tquadrillage.clear()

def quadrillage():
    tquadrillage.color("black")
    tquadrillage.width(1)
    tquadrillage.speed("fastest")

    axex(0,700)
    axey(0,-1000)
    tquadrillage.up()
    tquadrillage.goto(600,-450)
    tquadrillage.down()
    tquadrillage.write("F10 - Cacher le Quadrillage", font=("Arial", 20, "normal"))
    tquadrillage.up()
    tquadrillage.goto(0,0)
    tquadrillage.seth(0)
    tquadrillage.down()
    onkey(cachequadri, "F10")

################################################################################
################################################################################

def changecolor(x=0, y=0):
    global colordown

    #Permet de monter la valeur
    colordown = colordown[1:]+colordown[:1]
    color(colordown[0])

def changetaille(x=0, y=0):
    global taillepen
    global tailleshape

    taillepen = taillepen[1:]+taillepen[:1]
    tailleshape = tailleshape[1:]+tailleshape[:1]
    width(taillepen[0])
    shapesize(float(tailleshape[0]))

def switchuppen(a=0, b=0):
    global colordown

    if pen()["pendown"]:
        end_fill()
        up()
        color("#95a5a6")
    else:
        down()

        colordown=["#1abc9c", "#2ecc71", "#3498db", "#9b59b6", "#34495e",
                "#f1c40f", "#e67e22", "#e74c3c", "#ecf0f1",]
        color(colordown[0])

        begin_fill()


def menudessin(a,b,c):
    tmenu1.up()
    tmenu1.goto(930,500)
    tmenu1.down()
    tmenu1.width(5)
    tmenu1.color("#16a085")
    tmenu1.fillcolor("#1abc9c")
    tmenu1.begin_fill()
    while(a<5):
        tmenu1.rt(45)
        tmenu1.forward(b)
        tmenu1.rt(45)
        tmenu1.forward(c)
        a=a+1
    tmenu1.end_fill()

    tmenu1.up()
    tmenu1.goto(630,450)
    tmenu1.down()
    tmenu1.color("#ecf0f1")
    tmenu1.write("F1 - Changer la Couleur", font=("Arial", 20, "normal"))

    tmenu1.up()
    tmenu1.goto(630,400)
    tmenu1.down()
    tmenu1.color("#ecf0f1")
    tmenu1.write("F2 - Changer la Taille", font=("Arial", 20, "normal"))

    tmenu1.up()
    tmenu1.goto(630,350)
    tmenu1.down()
    tmenu1.color("#ecf0f1")
    tmenu1.write("F11 - Cacher le Menu", font=("Arial", 20, "normal"))

    tmenu1.up()
    tmenu1.goto(630,300)
    tmenu1.down()
    tmenu1.color("#ecf0f1")
    tmenu1.write("F3 - Effacer le Contenu", font=("Arial", 20, "normal"))

    tmenu1.up()
    tmenu1.goto(630,250)
    tmenu1.down()
    tmenu1.color("#ecf0f1")
    tmenu1.write("F4 - Sauvegarder", font=("Arial", 20, "normal"))


    tmenu1.up()
    tmenu1.color("black")
    tmenu1.goto(0,0)
    tmenu1.down()
    tmenu1.setheading(0)

def gomme():
    clear()

def save():
    name = input("Nom du fichier ?")

    chrono1 = clock()

    tmenu1.clear()
    tmenu.clear()
    ht()

    try:
        ts = getscreen()

        ts.getcanvas().postscript(file= name + ".eps")
    except:
        print("Erreur lors de la sauvegarde !")

    st()
    menu(0,25,300)
    menudessin(0,25,300)

    chrono2 = clock()
    temps = chrono2-chrono1

    print(temps)

    tsave.up()
    tsave.goto(-380, 450)
    tsave.down()

    tsave.write("Le fichier s'est sauvegarder en " + str(temps) + " sec. !", font=("Arial", 20, "normal"))
    sleep(2)
    tsave.clear()

def cachemenucolor():
    if tmenu1.pen()["pendown"]:
        tmenu1.clear()
        tmenu1.up()
    else:
        tmenu1.down()
        menudessin(0,25,300)


def déplacement():
    global taillepen
    global tailleshape

    taillepen=["1","2","3","4","5","6","7","8","9","10"]
    tailleshape=["1.1","1.2","1.3","1.4","1.5","1.6","1.7","1.8","1.9","2"]

    menudessin(0,25,300)
    seth(90)
    st()
    speed(5)
    shape("circle")
    shapesize(int(taillepen[0]))
    width(taillepen[0])
    switchuppen()
    ondrag(goto,1)
    onscreenclick(goto,1)
    onscreenclick(switchuppen,3)
    onkey(changecolor, "F1")
    onkey(changetaille, "F2")
    onkey(cachemenucolor, "F11")
    onkey(gomme, "F3")
    onkey(save, "F4")
    onkey(apercu, "F5")


################################################################################
################################################################################

def cathedrale():
    tquadrillage.speed(1)
    tcathe.color("#7f8c8d")
    tcathe.width(3)
    tcathe.up()
    tcathe.setheading(0)
    tcathe.goto(0,0)
    tcathe.down()
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

    def boite1():
        tcathe.begin_fill()
        tcathe.circle(5,180)
        tcathe.forward(300)
        tcathe.circle(5,180)
        tcathe.forward(300)
        tcathe.end_fill()
    boite1()

    tcathe.rt(90)
    tcathe.forward(350)
    tcathe.lt(90)

    boite1()

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
    tcathe.setheading(0)
    tcathe.rt(90)
    tcathe.forward(650)
    tcathe.rt(90)
    tcathe.forward(300)
    boite1()
    tcathe.setheading(0)
    tcathe.forward(50)
    tcathe.lt(90)
    tcathe.forward(300)
    tcathe.up()
    tcathe.goto(100,-175)
    tcathe.down()
    tcathe.rt(180)
    tcathe.forward(300)

    def cIN():
        tcathe.begin_fill()
        tcathe.setheading(180)
        tcathe.circle(5,180)
        tcathe.forward(50)
        tcathe.circle(5,180)
        tcathe.forward(50)
        tcathe.end_fill()

    #######################
    tcathe.up()
    tcathe.goto(150,-175)
    tcathe.down()
    tcathe.setheading(0)
    tcathe.rt(30)
    tcathe.forward(100)

    cIN()
    tcathe.lt(90)
    tcathe.forward(50)
    tcathe.setheading(150)
    tcathe.forward(100)

    tcathe.setheading(0)
    tcathe.up()
    tcathe.goto(150,175)
    tcathe.down()

    tcathe.rt(30)
    tcathe.forward(100)
    print(tcathe.pos())
    tcathe.setheading(0)

    cIN()
    tcathe.lt(90)
    tcathe.forward(50)
    tcathe.setheading(150)
    tcathe.forward(100)

    tcathe.setheading(0)
    tcathe.up()
    tcathe.goto((236.60,125.00))
    tcathe.down()

    tcathe.rt(90)
    tcathe.forward(600)
    print(tcathe.pos())
    tcathe.rt(90)
    cIN()
    tcathe.setheading(0)
    tcathe.forward(50)
    tcathe.lt(90)
    tcathe.forward(600)
    tcathe.setheading(120)
    tcathe.forward(50)
    tcathe.lt(120)
    tcathe.forward(50)

    ######################
    tcathe.up()
    tcathe.goto(-150,-175)
    tcathe.down()
    tcathe.setheading(180)
    tcathe.lt(30)
    tcathe.forward(100)
    tcathe.setheading(180)
    tcathe.forward(50)
    cIN()
    tcathe.setheading(0)
    tcathe.forward(50)
    tcathe.rt(90)
    tcathe.forward(50)
    tcathe.setheading(30)
    tcathe.forward(100)

    tcathe.setheading(180)
    tcathe.up()
    tcathe.goto(-150,175)
    tcathe.down()

    tcathe.lt(30)
    tcathe.forward(100)
    print(tcathe.pos())
    tcathe.setheading(180)

    tcathe.setheading(180)
    tcathe.forward(50)
    cIN()
    tcathe.setheading(0)
    tcathe.forward(50)
    tcathe.rt(90)
    tcathe.forward(50)
    tcathe.setheading(30)
    tcathe.forward(100)

    tcathe.setheading(0)
    tcathe.up()
    tcathe.goto((-236.60,125.00))
    tcathe.setheading(180)
    tcathe.forward(50)
    tcathe.down()

    tcathe.lt(90)
    tcathe.forward(600)
    tcathe.lt(90)
    cIN()
    tcathe.setheading(0)
    tcathe.forward(50)
    tcathe.lt(90)
    tcathe.forward(600)
    tcathe.setheading(120)
    tcathe.forward(50)
    tcathe.lt(120)
    tcathe.forward(50)

    ######################
    tcathe.up()
    tcathe.goto(73.5,0)

    tcathe.down()
    tcathe.setheading(135)
    tcathe.forward(103.9)
    tcathe.lt(90)
    tcathe.forward(103.9)
    tcathe.lt(90)
    tcathe.forward(103.9)
    tcathe.lt(90)
    tcathe.forward(103.9)

    tcathe.up()
    tcathe.goto(0,-475)
    tcathe.down()
    tcathe.setheading(0)
    tcathe.forward(50)
    tcathe.lt(90)
    tcathe.forward(100)
    tcathe.lt(30)
    tcathe.forward(100)
    tcathe.lt(120)
    tcathe.forward(100)
    tcathe.setheading(0)
    tcathe.rt(90)
    tcathe.forward(100)


    sleep(5)
    tcathe.clear()

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

def etoile1():
    up()
    home()
    down()
    for i in range(350):
        forward(i)
        right(100)

def etoile2():
    up()
    home()
    down()
    for i in range(200):
        forward(i)
        left(216)

def polyspi(angle,varb,longueur,times):
    if times > 0:
        fd(longueur)
        rt(angle)
        polyspi(angle,varb, (longueur + varb),(times - 1))

def figure3():
    up()
    home()
    down()
    polyspi(117,3,25,200)
    fd(500)

def rond():
    def carre():
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)

    for i in range(72):
        carre()
        rt(5)
        fd(20)

def rond2():
    up()
    home()
    down()
    r=200
    inc=2*pi/100
    t=0;n=1.5
    for i in range(100):
        x1=r*sin(t);  y1=r*cos(t)
        x2=r*sin(t+n);y2=r*cos(t+n)
        penup();
        goto(x1,y1)
        pendown();
        goto(x2,y2)
        t+=inc

def fonctionsinus():
  x = -math.pi
  y = math.sin(x)
  coordX = x * 100
  coordY = y * 100
  up()
  goto(coordX, coordY)
  down()
  while x < math.pi:
    x = x + 0.01
    y = math.sin(x)
    coordX, coordY = x * 100, y * 100
    goto(coordX, coordY)
  up()


def rond3():
    tdessin=Turtle()
    tdessin.ht()
    tdessin.speed(0)

    listeturtle = [tdessin]

    for i in range(36):
        tclone = tdessin.clone()
        tclone.rt(10)
        #Pour rajouter les turtles
        listeturtle.append(tclone)
        tdessin = tclone
        tdessin.clear()

    for i in range(36):
        #Pour la couleur, color RGB pencolor(r, g, b)
        colorrond = abs(18-i)/(36*.7)

        for tdessin in listeturtle:
            tdessin.rt(10)
            tdessin.color(1-colorrond,0,colorrond)
            tdessin.fd(19)

    sleep(2)

    #On efface toute la liste des turtles
    for i in range(1,36):
        for tdessin in listeturtle:
            tclone.clear()
            tdessin.clear()

def dessins():
    color("black")
    ht()

    clear()
    etoile1()
    sleep(2)

    clear()
    etoile2()
    sleep(2)

    clear()
    figure3()
    sleep(2)

    clear()
    rond()
    sleep(2)

    clear()
    rond2()
    sleep(2)

    clear()
    fonctionsinus()
    sleep(2)

    clear()
    rond3()

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
    a=a-5

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
    tmenu.goto(-930,250)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("E - Dessins", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.goto(-930,200)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("F - Cacher le menu", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.color("black")
    tmenu.goto(0,0)
    tmenu.down()
    tmenu.setheading(0)

def cachemenu():
    if pen()["pendown"]:
        tmenu.clear()
        up()
    else:
        menu(0,25,300)
        down()



################################################################################
################################################################################

menu(0,25,300)

################################################################################
################################################################################

onkey(quadrillage,"a")
onkey(cathedrale,"b")
onkey(déplacement,"c")
onkey(arbreentier,"d")
onkey(dessins,"e")
onkey(cachemenu,"f")
listen()

################################################################################
################################################################################

mainloop()

################################################################################
################################################################################
