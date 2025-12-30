import turtle
import math

angle = 45

scale = math.sqrt(2) / 2
init_len = 100


def draw_pithagoras_tree(t, branch_len, level):
    if level == -1:
        return

    t.forward(branch_len)
    t.right(angle)
    draw_pithagoras_tree(t, branch_len * scale, level - 1)

    t.left(2 * angle)
    draw_pithagoras_tree(t, branch_len * scale, level - 1)

    t.right(angle)
    t.backward(branch_len)


def main():
    recursion_level = int(input("Input recursion level: ").strip())

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(1)
    t.color("brown")
    t.pensize(2)
    t.left(90)
    t.up()
    t.goto(0, -200)
    t.down()

    draw_pithagoras_tree(t, init_len, recursion_level)

    t.hideturtle()
    screen.exitonclick()


if __name__ == "__main__":
    main()
