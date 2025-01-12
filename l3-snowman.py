import turtle as t
t.speed(0)
t.bgcolor ("#528dd1")

t.width (4)

t.color ("grey","white")
t.begin_fill ()
for x in range (36) :
    t.forward (20)
    t.right (10)
t.end_fill ()
t.color ("grey","white")
t.begin_fill ()
for x in range (36) :
    t.forward (15)
    t.left (10)
t.end_fill ()

t.penup()
t.goto(0,174)
t.pendown ()
t.color ("grey","white")
t.begin_fill ()
for x in range (36) :
    t.forward (10)
    t.left (10)
t.end_fill ()

# smile
t.penup ()
t.goto (-20,214)
t.pendown ()
t.setheading(270)
t.color ("red")
t.circle (26,180)

# eyes
t.penup ()
t.goto (-15,250)
t.pendown ()
t.color ("black")
t.circle (2)


# eyes
t.penup ()
t.goto (20,250)
t.pendown ()
t.color ("black")
t.circle (2)
t.mainloop ()
