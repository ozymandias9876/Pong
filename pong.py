import turtle
import winsound
wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(800,600)
wn.title("Pong by H.T")
wn.tracer()

#paddle_1
paddle_1=turtle.Turtle()
paddle_1.color("white")
paddle_1.penup()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(4,1)
paddle_1.goto(-350,0)
#paddle_2
paddle_2=turtle.Turtle()
paddle_2.color("white")
paddle_2.penup()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(4,1)
paddle_2.goto(350,0)

#ball
ball=turtle.Turtle()
ball.color("white")
ball.penup()
ball.shape("circle")
ball.goto(0,0)
dx=3
dy=3

score=turtle.Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1:0|Computer:0",align="center",font=("courier",14,"bold"))
score_a=0
score_b=0


def paddle_1_up():
    y=paddle_1.ycor()
    y+=20
    paddle_1.sety(y)


def paddle_1_down():
    y=paddle_1.ycor()
    y-=20
    paddle_1.sety(y)

def paddle_2_up():
    z=paddle_2.ycor()
    z+=20
    paddle_2.sety(z)

def paddle_2_down():
    z=paddle_2.ycor()
    z-=20
    paddle_2.sety(z)
wn.listen()
wn.onkeypress(paddle_2_up,'Up')
wn.onkeypress(paddle_2_down,'Down')
wn.onkeypress(paddle_1_up,'w')
wn.onkeypress(paddle_1_down,'s')

while True:
    wn.update()
    ball.setx(ball.xcor()+dx)
    ball.sety(ball.ycor()+dy)
    if ball.ycor()>290:
        ball.sety(290)
        dy *=-1
    elif ball.ycor()<-290:
        ball.sety(-290)
        dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        dx *=-1
        score_a+=1
        score.clear()
        score.write("Player 1:{}|Computer:{}".format(score_a,score_b),align="center",font=("courier",14,"bold"))



    elif ball.xcor()<-390:
        ball.goto(0,0)
        dx *=-1
        score_b+=1
        score.clear()
        score.write("Player 1:{}|Computer:{}".format(score_a,score_b),align="center",font=("courier",14,"bold"))



    if ball.xcor()>0 and dx>0:
        paddle_2.sety(ball.ycor())
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_2.ycor() +40 and ball.ycor()>paddle_2.ycor() -40):
        ball.setx(340)
        dx*=-1
        winsound.PlaySound('SystemHand',1)
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_1.ycor() +40 and ball.ycor()>paddle_1.ycor() -40):
        ball.setx(-340)
        dx*=-1
        winsound.PlaySound('SystemHand',1)
    if paddle_1.ycor()>250:
        paddle_1.sety(250)
    if paddle_1.ycor()<-250:
        paddle_1.sety(-250)
    if paddle_2.ycor()>250:
        paddle_2.sety(250)
    if paddle_2.ycor()<-250:
        paddle_2.sety(-250)






wn.exitonclick()
