import turtle
turtle.Screen().bgcolor("Red")
num =int(input("enter how many squares you want?: "))
board = turtle.Turtle()
 
for i in range(num):
    for j in range(4):
        board.forward(50)
        board.left(90)
        
    board.penup()
    board.forward(100)
    board.pendown()
turtle.done()


