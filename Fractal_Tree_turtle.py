from turtle import *

bgcolor("black")
color("white")
# speed(15)
pensize(5)
left(90)
backward(100)

li = [{1: [1, 2, 3]}, {2: [3, 4]}, {3: [4, 5]}, {4: [4, 5, 1, 2, 3, 4]}]


def start(x, y):
    for k in x:
        if(isinstance(x, dict)):
            right(30)
            circle(5)
            forward(100)
            start(x[list(x.keys())[0]])
        elif(isinstance(x, list)):
            flag = True
            for i in x:
                if(flag):
                    left(60)
                    forward(50)
                    color("green")
                    backward(50)
                else:
                    right(60)
                    forward(50)
                    color("red")
                    backward(50)
                pass
        backward(y)
        # else:
        #     for i in x:
        #         start(i, y-5)
        # forward(x)
        # right(30)
        # color("red")
        # circle(2)
        # start(x-10)
        # color("yellow")
        # left(60)
        # color("green")
        # start(x-10)
        # color("white")
        # right(30)


start(li, 100)

# color('red', 'yellow')
# speed(20)
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

t = turtle.Pen()

n = 50

t.left(90)
t.backward(150)
t.forward(150)


t.circle(50, steps=5)


count = 5
angle = 360/count
while(count > -1):
    t.forward(100)
    t.left(angle)
    count -= 1

my_wn = Screen()

exitonclick()
