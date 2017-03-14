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

#taille = int(input("Taille Quadrillage = "))
taille = 20

################################################################################
################################################################################

speed("fastest")

################################################################################
################################################################################

#Valeur conseillée: a=5 b=1 c=2
def ellipse(a,b,c):
    shape("circle")
    shapesize(a,b,c)

################################################################################
################################################################################

#Valeur conseillée: a=0 b=700
def axex(a,b):
    up()
    goto(-1000,b)
    down()
    while(a<1000):
        forward(2500)
        b=b-taille
        a=a+10
        up()
        goto(-1000,b)
        down()

#Valeur conseillée: a=0 b=-1000
def axey(a,b):
    up()
    goto(-1000,b)
    down()
    right(90)
    while(a<1000):
        forward(2500)
        b=b+taille
        a=a+10
        up()
        goto(b,700)
        down()

def quadrillage():
    color("black")
    rt(heading())
    width(1)
    speed("fastest")
    axex(0,700)
    axey(0,-1000)
    up()
    goto(0,0)
    rt(heading())
    down()

################################################################################
################################################################################

def switchuppen(a=0, b=0):
    if pen()["pendown"]:
        end_fill()
        up()
        color("#3498db")
    else:
        down()
        color("#2980b9")
        begin_fill()

def déplacement():
    st()
    speed(5)
    shape("circle")
    shapesize(1)
    width(3)
    switchuppen()
    onscreenclick(goto,1)
    onscreenclick(switchuppen,3)

################################################################################
################################################################################

def cathedrale():
    reset()
    width(3)
    up()
    goto(100,0)
    down()
    lt(90)
    forward(175)

    up()
    goto(-100,0)
    down()

    forward(175)
    up()
    goto(73.5,0)

    down()
    circle(73.5)
    up()
    goto(80.25,0)
    lt(180)
    down()

    circle(-80.25,180)
    up()
    goto(-80.25,0)
    down()
    circle(-160.5,60 )
    up()

    goto(80.25,0)
    lt(90)
    down()
    #circle(160.5,60)
    print(heading())
    lt(240)
    lt(90)

    up()
    goto(80.25,0)
    down()
    circle(160.5,60 )
    rt(240)
    rt(90)
    up()
    goto(100,0)
    down()
    rt(270)
    forward(175)
    lt(90)
    print(heading())
    up()
    goto(-100,0)
    down()
    rt(90)
    forward(175)

    rt(90)
    forward(50)
    rt(90)
    forward(350)
    rt(180)
    forward(350)
    rt(90)

    def b():
        circle(5,180)
        forward(300)
        circle(5,180)
        forward(300)
    b()

    rt(90)
    forward(350)
    lt(90)

    b()

    up()
    goto(150,-175)
    down()
    rt(90)
    forward(350)

    up()
    goto(150,-175)
    down()
    rt(180)
    forward(300)
    up()
    goto(-150,-175)
    down()

    forward(300)
    lt(90)
    forward(100)
    up()
    goto(100,175)
    down()
    lt(90)
    forward(80)
    up()
    goto(-100,175)
    down()
    forward(80)
    rt(30)
    forward(200)
    rt(120)
    forward(200)

    up()
    goto(150,175)
    down()
    print(heading())
    lt(60)
    lt(90)
    forward(80)
    up()
    goto(-150,175)
    down()
    print(heading())
    forward(80)

    rt(30)
    forward(300)
    rt(120)
    forward(300)
    print(heading())
    up()
    goto(150,175)
    down()

################################################################################
################################################################################

def menu(a,b,c):
    ht()
    up()
    goto(-100,300)
    down()
    width(5)
    color("#16a085")
    fillcolor("#1abc9c")
    begin_fill()
    while(a<5):
        rt(45)
        forward(b)
        rt(45)
        forward(c)
        a=a+1
    end_fill()

    up()
    goto(-400,250)
    down()
    color("#ecf0f1")
    write("A - Quadrillage", font=("Arial", 25, "normal"))

    up()
    goto(-400,200)
    down()
    color("#ecf0f1")
    write("B - Cathédrale", font=("Arial", 25, "normal"))

    up()
    goto(-400,150)
    down()
    color("#ecf0f1")
    write("C - Coloriage", font=("Arial", 25, "normal"))

    up()
    color("black")
    goto(0,0)
    rt(heading())
    down()

################################################################################
################################################################################

menu(0,25,300)

################################################################################
################################################################################

onkey(quadrillage,"a")
onkey(cathedrale,"b")
onkey(déplacement,"c")
listen()

################################################################################
################################################################################

mainloop()

################################################################################
################################################################################

exitonclick()