import turtle

angle = 45


def draw_pithagoras_tree(t, branch_len, level):
    if level == 0:
        return

    t.forward(branch_len)
    t.right(angle)
    draw_pithagoras_tree(t, branch_len * 0.7, level - 1)

    t.left(2 * angle)
    draw_pithagoras_tree(t, branch_len * 0.7, level - 1)

    t.right(angle)
    t.backward(branch_len)


def main():
    recursion_level = int(input("Input recursion level: ").strip())

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(1)
    t.color("brown")
    t.left(90)
    t.up()
    t.goto(0, -200)
    t.down()
    t.pensize(2)

    draw_pithagoras_tree(t, 100, recursion_level)

    t.hideturtle()
    screen.exitonclick()


if __name__ == "__main__":
    main()
