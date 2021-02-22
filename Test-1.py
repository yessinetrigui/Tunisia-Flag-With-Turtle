import turtle
import winsound
import tkinter
from tkinter import ttk
winsound.PlaySound("Run33.wav", winsound.SND_ASYNC)
pen=turtle.Turtle()
turtle.title('Tunisia flag')
pen2=turtle.Turtle()
pen2.penup()
pen2.goto(-270, -290)
pen2.speed(100)
class parl () :
    def t1():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write("حماة الحمى يا حماة الحمى	",font=("andalus",50))
    def t2():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('هلموا هلموا لمجد الزمــن',font=("andalus",50))
    def t3():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('لقد صرخت في عروقنا الدما	',font=("andalus",50))
    def t4():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('نموت نموت ويحيا الوطن',font=("andalus",50))
    def t5():
        pen2.penup()
        pen2.goto(-220,-290)
        pen2.write('لتدو السماوات برعدها	',font=("andalus",50))
    def t6():
        pen2.penup()
        pen2.goto(-220,-290)
        pen2.write('لترم الصواعق نيرانها',font=("andalus",50))
    def t7():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('إلى عز تونس إلى مجدها	',font=("andalus",50))
    def t8():
        pen2.penup()
        pen2.goto(-220,-290)
        pen2.write('رجال البلاد وشبانها',font=("andalus",50))
    def t9():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('فلا عاش في تونس من خانها	',font=("andalus",50))
    def t10():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('ولا عاش من ليس من جندها',font=("andalus",50))
    def t11():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('نموت ونحيا على عهدها	',font=("andalus",50))
    def t12():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('حياة الكرام وموت العظام',font=("andalus",50))
    def t13():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('حماة الحمى يا حماة الحمى	',font=("andalus",50))
    def t14():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('هلموا هلموا لمجد الزمــن',font=("andalus",50))

    def t15():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('لقد صرخت في عروقنا الدما	', font=("andalus", 50))
    def t16():
        pen2.penup()
        pen2.goto(-270,-290)
        pen2.write('نموت نموت ويحيا الوطن',font=("andalus",50))

    def clear():
        pen2.clear()
        pen2.goto(-270,-290)
turtle.listen()
#Ya monsieur les parole rbathom bl keyboard lezm nnzl kol mara bch iji el parole
turtle.onkey(parl.t1, "1")
turtle.onkey(parl.t2, "2")
turtle.onkey(parl.t3, "3")
turtle.onkey(parl.t4, "4")
turtle.onkey(parl.t5, "5")
turtle.onkey(parl.t6, "6")
turtle.onkey(parl.t7, "7")
turtle.onkey(parl.t8, "8")
turtle.onkey(parl.t9, "9")
turtle.onkey(parl.t10, "A")
turtle.onkey(parl.t11, "Z")
turtle.onkey(parl.t12, "E")
turtle.onkey(parl.t13, "R")
turtle.onkey(parl.t14, "T")
turtle.onkey(parl.t15, "Y")
turtle.onkey(parl.t16, "U")
turtle.onkey(parl.clear,"F")

print('Coding by; Yessine Trigui')
pen.pensize(5)
pen.color('red')

pen.shape('classic')
pen.speed("slowest")
pen.penup()
pen.goto(-300,-200)
pen.pendown()
pen.color('red')
pen.begin_fill()
for i in range(2):
    pen.forward(600)
    pen.left(90)
    pen.forward(450)
    pen.left(90)
pen.end_fill()
pen.color('white')
pen.penup()
pen.goto(0,-125)
pen.pendown()
pen.color('White')
pen.begin_fill()
pen.circle(150)
pen.end_fill()
pen.color('red')
pen.penup()
pen.goto(0,-85)
pen.pendown()
pen.color('red')
pen.begin_fill()
pen.circle(110)
pen.end_fill()
pen.color('White')
pen.penup()
pen.goto(38,-70)
pen.pendown()
pen.begin_fill()
pen.circle(95)
pen.end_fill()
pen.color('red')
pen.penup()
pen.goto(-28,25)
pen.pendown()
pen.color('red')
pen.begin_fill()

pen.setheading(20)
for i in range(5):
    pen.forward(100)
    pen.right(144)
pen.end_fill()
pen.penup()
pen.goto(300,3300)





turtle.done()