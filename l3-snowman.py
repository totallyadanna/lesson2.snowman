import turtle as t
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

t.mainloop ()