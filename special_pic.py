from turtle import *
import random

setup(width = 1000, height=1000)

position = []

class molecule:
    global position
    def __init__(self, coorX, coorY, speed, size):
        self.head = Turtle()
        self.head.speed(0)
        self.tspeed = speed
        self.head.shapesize(size)
        self.head.shape("circle")
        self.head.color("black")
        self.head.penup()
        self.head.goto(coorX, coorY)
        self.head.direction = "stop"

    def initMolecule(self):
        #self.head.hideturtle()
        self.head.pendown()
        #self.head.speed(self.tspeed)

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 10)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 10)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 10)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 10)

    def changeDirec(self):
        if self.head.direction == "up":
            self.head.direction = "down"
        if self.head.direction == "down":
            self.head.direction = "up"
        if self.head.direction == "right":
            self.head.direction = "left"
        if self.head.direction == "left":
            self.head.direction = "right"

    def makeMove(self):
        self.initMolecule()
        for a in range(1):
            self.head.direction = str(random.choice(['up', 'right', 'left', 'down']))
            self.move()
            self.head.ycor()
            pos = list((self.head.xcor(), self.head.ycor()))
            for el in position:
                if el[0] == pos[0] or el[1] == pos[1]:
                    self.changeDirec()
                    return

            position.append(pos)
            if self.head.xcor() >= 500 or self.head.ycor() >= 500 or \
                    self.head.xcor() <= -500 or self.head.ycor() <= -500 :
                self.changeDirec()

class colony:
    def __init__(self, size):
        self.mc = []
        self.m_thread = []
        for a in range(size):
            m = molecule(random.randint(-500, 500), random.randint(-500, 500), random.randint(0, 10), random.random())
            self.mc.append(m)

    def startMove(self):
        global position
        while True:
            for a in self.mc:
                a.makeMove()
            position.clear()


if __name__ == "__main__":
    Colony = colony(int(textinput(title="Colony size", prompt="Enter the size of the colony: ")))
    Colony.startMove()
