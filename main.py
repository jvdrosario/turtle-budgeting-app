import turtle as t
import finance as f

# ----- SCREEN & TURTLE SETUP -----

t.colormode(255)
t.setup(1280, 720)
t.screensize(1300, 740)
t.Screen().bgcolor((35, 36, 46))
t.tracer(False)

# ----- SETUP WINDOW -----

# show logo in corner
t.addshape("logo.gif")
ui = t.Turtle()
ui.hideturtle()
ui.penup()
logo = t.Turtle()
logo.shape("logo.gif")

# spending displays for savings and needs
ui.color("white")
f.button.goto(500, 140)
f.button.stamp()
ui.goto(500, 70)
ui.write("MONTHLY EXPENSES", font=f.fonts[1], align="center")
f.button.goto(500, 0)
f.button.stamp()
ui.goto(500, -70)
ui.write("MONTHLY SAVINGS", font=f.fonts[1], align="center")
ui.color("black")

# (----- OPEN DATA -----)
try:
    f.open_data()
except:
    pass

# draw sidebar
ui.penup()
ui.goto(-400, 250)
ui.pendown()
ui.fillcolor((65, 139, 166))
ui.begin_fill()
ui.goto(-400, -250)
ui.setheading(90)
ui.circle(120, -90)
ui.goto(-650, -370)
ui.goto(-650, 250)
ui.goto(-400, 250)
ui.penup()
ui.end_fill()
logo.penup()
logo.goto(-500, 300)
t.tracer(True)
t.tracer(False)  # makes turtle shape show
f.total.goto(-350, 280)
f.total.color((255, 255, 255))
f.display_account_total()

# deposit button
ui.penup()
ui.color("white")
ui.goto(500, 210)
ui.write("DEPOSIT", font=f.fonts[1], align="center")
ui.goto(-425, 370)

# sidebar text & buttons
ui.color((35, 36, 46))
ui.penup()
ui.goto(-512.5, 170)
ui.write("Create Category", font=f.fonts[2], align="center")
ui.goto(-512.5, 120)
ui.write("View Transactions", font=f.fonts[2], align="center")
ui.goto(-512.5, 70)
ui.write("Create/Edit Saving Goal", font=f.fonts[2], align="center")
ui.goto(-512.5, 20)
ui.write("Create/Edit Budget", font=f.fonts[2], align="center")
ui.goto(-512.5, -30)
ui.write("Set Monthly Expenses", font=f.fonts[2], align="center")
ui.goto(-512.5, -80)
ui.write("Party Mode", font=f.fonts[2], align="center")
ui.goto(-512.5, -130)
ui.write("Auto Budget", font=f.fonts[2], align="center")
ui.goto(-512.5, -180)
ui.write("Exit App", font=f.fonts[2], align="center")
ui.goto(-512.5, -280)
ui.write(f.get_month_year()[:-5] + " " + f.get_month_year()[-4:], font=f.fonts[2], align="center")
ui.goto(0, -330)
ui.color("white")
ui.write("Click on category to report expense", font=f.fonts[2], align="center")

# ----- USER INTERACTION -----

f.deposit_b.onclick(f.deposit)
t.onscreenclick(f.screen_nav)

t.mainloop()