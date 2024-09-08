import random
import turtle
import time

hiz = 0.13
pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('white')
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape('square')
kafa.color('black')
kafa.penup()
kafa.goto(0, 100)
kafa.direction = 'stop'


yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape('circle')
yemek.color('red')
yemek.penup()
yemek.goto(0, 0)
yemek.shapesize(0.80, 0.80)

kuyruklar = []
def move():
    if kafa.direction == 'Up':
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == 'Down':
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == 'Right':
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == 'Left':
        x = kafa.xcor()
        kafa.setx(x - 20)


def goUp():
     if kafa.direction != 'Down':
         kafa.direction = 'Up'
def goDown():
    if kafa.direction != 'Up':
        kafa.direction = 'Down'

def goRight():
    if kafa.direction != 'Left':
        kafa.direction = 'Right'

def goLeft():
    if kafa.direction != 'Right':
        kafa.direction = 'Left'



pencere.listen()
pencere.onkey (goUp, 'Up')
pencere.onkey (goDown, 'Down')
pencere.onkey (goRight, 'Right')
pencere.onkey (goLeft, 'Left')

while True:
    pencere.update()


    if kafa.distance(yemek) <15:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        yemek.goto(x,y)

        yenikuyruk = turtle.Turtle()
        yenikuyruk.speed(0)
        yenikuyruk.shape('square')
        yenikuyruk.color('black')
        yenikuyruk.penup()
        kuyruklar.append(yenikuyruk)

    for i in range (len(kuyruklar)- 1,0,-1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()
        kuyruklar[i].goto(x,y)

        if len(kuyruklar) > 0:
            x=kafa.xcor()
            y=kafa.ycor()
            kuyruklar[0].goto(x,y)
    move()
    time.sleep(hiz)

