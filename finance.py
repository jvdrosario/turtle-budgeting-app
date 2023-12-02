import turtle as t
from datetime import date
from datetime import datetime
import random as r

t.colormode(255)
t.tracer(False)

# ----- DEFINE OBJECTS & DATABASES -----

# databases
user_assets = {"TOTAL": 0, "CATEGORIES": 0}
categories = {5: {"NAME": "Monthly Expenses", "SPENDING": 0, "BUDGET": 0, "TRANSACTIONS": []},
              6: {"NAME": "Monthly Savings", "SPENDING": 0, "BUDGET": 0, "TRANSACTIONS": []}}
fonts = [("Helvetica", 20, "bold"), ("Helvetica", 12, "italic"), ("Helvetica", 12, "bold")]
modes = {"PARTY": False, "BUDGET": False, "TRANSACTIONS": False}
paid = {"EXPENSES": True, "SAVINGS": True}
budget_category = [0]

# turtles
t.addshape("button.gif")
for num in range(1, 11):
    t.addshape("ag" + str(num) + ".gif")
t.hideturtle()
text = t.Turtle()
text.hideturtle()
text.penup()
temp_text = t.Turtle()
temp_text.hideturtle()
temp_text.penup()
budget_text = t.Turtle()
budget_text.hideturtle()
budget_text.penup()
expense_text = t.Turtle()
expense_text.hideturtle()
expense_text.penup()
savings_text = t.Turtle()
savings_text.hideturtle()
savings_text.penup()
total = t.Turtle()
total.hideturtle()
total.penup()
party_mode_t = t.Turtle()
party_mode_t.penup()
party_mode_t.hideturtle()
pie = t.Turtle()
pie.penup()
pie.hideturtle()
pie.speed(10)
key = t.Turtle()
key.hideturtle()
key.penup()
key.color("white")

# buttons
button = t.Turtle()
button.shape("button.gif")
button.penup()
button.hideturtle()
deposit_b = t.Turtle()
deposit_b.shape("button.gif")
deposit_b.penup()
deposit_b.goto(500, 280)


# ----- DEFINE FUNCTIONS -----

def stall(num):
    t.tracer(True)
    tt = t.Turtle()
    tt.hideturtle()
    tt.penup()
    tt.speed(1)
    tt.forward(600 * num)
    t.tracer(False)


def alert(message):
    t.penup()
    t.goto(-300, 100)
    t.pendown()
    t.fillcolor((35, 36, 46))
    t.begin_fill()
    t.goto(300, 100)
    t.goto(300, -100)
    t.goto(-300, -100)
    t.goto(-300, 100)
    t.end_fill()
    t.penup()
    t.goto(0, -13)
    t.color((65, 139, 166))
    t.write(message, font=fonts[0], align="center")
    t.color("black")
    stall(0.5)
    t.clear()


def display_pie_chart():
    t.tracer(True)
    pie.goto(-200, 110 - 140)
    pie.clear()
    key.clear()
    prev_x = pie.xcor()
    prev_y = pie.ycor()
    total_spending = 0
    for category in categories:
        total_spending += categories[category]["SPENDING"]
    for category in categories:
        if category == 1:
            pie.fillcolor("red")
        elif category == 2:
            pie.fillcolor("green")
        elif category == 3:
            pie.fillcolor("yellow")
        elif category == 4:
            pie.fillcolor("orange")
        elif category == 5:
            pie.fillcolor("purple")
        elif category == 6:
            pie.fillcolor("ivory")
        pie.pendown()
        pie.begin_fill()
        pie.circle(140, (categories[category]["SPENDING"] / total_spending) * 360)
        prev_x_temp = pie.xcor()
        prev_y_temp = pie.ycor()
        t.tracer(False)
        if (categories[category]["SPENDING"] / total_spending) * 360 != 360:
            pie.goto(-200, 110)
            pie.goto(prev_x, prev_y)
        pie.end_fill()
        pie.penup()
        prev_x = prev_x_temp
        prev_y = prev_y_temp
        pie.goto(prev_x, prev_y)
        t.tracer(True)
    t.tracer(False)
    for category in categories:
        if category == 1:
            key.fillcolor("red")
        elif category == 2:
            key.fillcolor("green")
        elif category == 3:
            key.fillcolor("yellow")
        elif category == 4:
            key.fillcolor("orange")
        elif category == 5:
            key.fillcolor("purple")
        elif category == 6:
            key.fillcolor("ivory")
        key.showturtle()
        key.goto(0, 200 - (20 * int(category)))
        key.setheading(0)
        key.stamp()
        key.hideturtle()
        key.goto(10, 200 - (20 * int(category)) - 10)
        key.write(categories[category]["NAME"], font=fonts[2])


def display_account_total():
    total.clear()
    total_text = "Total: ${:.2f}".format(user_assets["TOTAL"])
    total.write(total_text, font=fonts[0])


def deposit(x, y):
    amount = t.textinput("Deposit", "Deposit Amount:")
    try:
        user_assets["TOTAL"] += float(amount)
        if categories[5]["SPENDING"] <= user_assets["TOTAL"] and not paid["EXPENSES"]:
            user_assets["TOTAL"] -= categories[5]["SPENDING"]
            display_account_total()
            paid["EXPENSES"] = True
            alert("Monthly Expenses Paid")
            display_pie_chart()
        if categories[6]["SPENDING"] <= user_assets["TOTAL"] and not paid["SAVINGS"]:
            user_assets["TOTAL"] -= categories[6]["SPENDING"]
            display_account_total()
            paid["SAVINGS"] = True
            alert("Monthly Goal Saved")
            display_pie_chart()
        else:
            display_account_total()
    except ValueError:
        alert("Error: Deposit amount must be number")


def create_category():
    if user_assets["CATEGORIES"] < 4:
        category = t.textinput("New Category", "Create Category:")
        user_assets["CATEGORIES"] += 1
        # create dictionary in database
        temp_dict = {"NAME": category, "SPENDING": 0, "BUDGET": 0, "TRANSACTIONS": list()}
        categories[user_assets["CATEGORIES"]] = temp_dict
        t.tracer(True)
        if user_assets["CATEGORIES"] == 1:  # displays all categories
            button.goto(-250, -125)
            button.showturtle()
            button.stamp()
            button.hideturtle()
            text.goto(-250, -140)
            text.color("white")
            text.write(category, font=fonts[0], align="center")
            text.color("black")
        elif user_assets["CATEGORIES"] == 2:
            button.goto(-250, -250)
            button.showturtle()
            button.stamp()
            button.hideturtle()
            text.goto(-250, -265)
            text.color("white")
            text.write(category, font=fonts[0], align="center")
            text.color("black")
        elif user_assets["CATEGORIES"] == 3:
            button.goto(125, -125)
            button.showturtle()
            button.stamp()
            button.hideturtle()
            text.goto(125, -140)
            text.color("white")
            text.write(category, font=fonts[0], align="center")
            text.color("black")
        elif user_assets["CATEGORIES"] == 4:
            button.goto(125, -250)
            button.showturtle()
            button.stamp()
            button.hideturtle()
            text.goto(125, -265)
            text.color("white")
            text.write(category, font=fonts[0], align="center")
            text.color("black")
        t.tracer(False)
    else:
        alert("Max 4 Categories")


def monthly_expenses():
    if categories[5]["SPENDING"] == 0:
        expense_text.clear()
        expenses = t.textinput("Monthly Expenses", "Amount: (Rent, Utilities, etc...)")
        try:
            expenses = float(expenses)
            paid["EXPENSES"] = False
            temp_dict = {"NAME": "Monthly Expenses", "SPENDING": expenses, "BUDGET": 0,
                         "TRANSACTIONS": ["${:.2f}".format(float(expenses))]}
            categories[5] = temp_dict
            if expenses <= user_assets["TOTAL"]:
                user_assets["TOTAL"] -= expenses
                display_account_total()
                paid["EXPENSES"] = True
                display_pie_chart()
            expense_text.goto(500, 123)
            expense_text.color("white")
            expense_text.write("${:.2f}".format(float(categories[5]["SPENDING"])), font=fonts[0], align="center")
        except ValueError:
            alert("Amount must be number")
    else:
        alert("Expense already set")


def savings_goal():
    if categories[6]["SPENDING"] == 0:
        savings_text.clear()
        goal = t.textinput("Monthly Savings", "Savings Goal: (How much would you like to have saved?)")
        timeframe = t.textinput("Monthly Savings", "Months: (In how many months?)")
        try:
            savings = float(goal) / float(timeframe)
            paid["SAVINGS"] = False
            temp_dict = {"NAME": "Monthly Savings", "SPENDING": savings, "BUDGET": 0,
                         "TRANSACTIONS": ["${:.2f}".format(float(savings))]}
            categories[6] = temp_dict
            if savings <= user_assets["TOTAL"]:
                user_assets["TOTAL"] -= savings
                display_account_total()
                paid["SAVINGS"] = True
                display_pie_chart()
            savings_text.goto(500, -17)
            savings_text.color("white")
            savings_text.write("${:.2f}".format(float(categories[6]["SPENDING"])), font=fonts[0], align="center")
        except ValueError:
            alert("Amount must be number")
    else:
        alert("Savings already set")


def set_budget():
    if user_assets["CATEGORIES"] != 0:  # does not trigger if categories do not exist
        modes["BUDGET"] = True
        alert("Please select category")
        while budget_category[0] == 0:  # waits while category is selected
            stall(0.01)
        budget_amount = t.textinput("Budget", "Amount:")
        try:
            categories[budget_category[0]]["BUDGET"] = float(budget_amount)
            budget_text.clear()
            for i in categories:
                if categories[i]["BUDGET"] == 0:
                    pass
                else:
                    budget_text.color("white")
                    if i == 1:
                        budget_text.goto(-140, -150)
                        budget_text.write("Budget: ${:.2f}".format(categories[1]["BUDGET"]), font=fonts[1])
                    elif i == 2:
                        budget_text.goto(-140, -275)
                        budget_text.write("Budget: ${:.2f}".format(categories[2]["BUDGET"]), font=fonts[1])
                    elif i == 3:
                        budget_text.goto(235, -150)
                        budget_text.write("Budget: ${:.2f}".format(categories[3]["BUDGET"]), font=fonts[1])
                    elif i == 4:
                        budget_text.goto(235, -275)
                        budget_text.write("Budget: ${:.2f}".format(categories[4]["BUDGET"]), font=fonts[1])
            budget_category[0] = 0
            modes["BUDGET"] = False
        except ValueError:
            alert("Deposit amount must be number")


def report_expense(num):
    if not modes["BUDGET"]:  # does not trigger if setting budget
        amount = t.textinput("Expense", "Amount:")
        description = t.textinput("Expense", "Description:")
        # if spending exceeds budget
        try:
            if (categories[num]["BUDGET"] == 0) or (
                    categories[num]["BUDGET"] >= (categories[num]["SPENDING"] + float(amount))):
                expense_date = date.today()
                if float(amount) <= user_assets["TOTAL"]:  # if spending doesn't exceed amount
                    if len(description) > 7:  # reflects spending into database
                        report = "${:.2f} / {}... / {}".format(float(amount), description[:7], expense_date)
                    else:
                        report = "${:.2f} / {} / {}".format(float(amount), description, expense_date)
                    user_assets["TOTAL"] -= float(amount)
                    categories[num]["SPENDING"] += float(amount)
                    categories[num]["TRANSACTIONS"].append(report)
                    temp_text.clear()
                    temp_text.color("white")
                    if user_assets["CATEGORIES"] == 1:  # display spending amounts for each category
                        temp_text.goto(-140, -120)
                        temp_text.write("Spent: ${:.2f}".format(categories[1]["SPENDING"]), font=fonts[1])
                    elif user_assets["CATEGORIES"] == 2:
                        temp_text.goto(-140, -120)
                        temp_text.write("Spent: ${:.2f}".format(categories[1]["SPENDING"]), font=fonts[1])
                        temp_text.goto(-140, -245)
                        temp_text.write("Spent: ${:.2f}".format(categories[2]["SPENDING"]), font=fonts[1])
                    elif user_assets["CATEGORIES"] == 3:
                        temp_text.goto(-140, -120)
                        temp_text.write("Spent: ${:.2f}".format(categories[1]["SPENDING"]), font=fonts[1])
                        temp_text.goto(-140, -245)
                        temp_text.write("Spent: ${:.2f}".format(categories[2]["SPENDING"]), font=fonts[1])
                        temp_text.goto(235, -120)
                        temp_text.write("Spent: ${:.2f}".format(categories[3]["SPENDING"]), font=fonts[1])
                    elif user_assets["CATEGORIES"] == 4:
                        temp_text.goto(-140, -120)
                        temp_text.write("Spent: ${:.2f}".format(categories[1]["SPENDING"]), font=fonts[1])
                        temp_text.goto(-140, -245)
                        temp_text.write("Spent: ${:.2f}".format(categories[2]["SPENDING"]), font=fonts[1])
                        temp_text.goto(235, -120)
                        temp_text.write("Spent: ${:.2f}".format(categories[3]["SPENDING"]), font=fonts[1])
                        temp_text.goto(235, -245)
                        temp_text.write("Spent: ${:.2f}".format(categories[4]["SPENDING"]), font=fonts[1])
                    temp_text.color("black")
                    display_account_total()
                    display_pie_chart()
                else:
                    alert("Not enough money")
            else:
                alert("Exceeds budget")
        except ValueError:  # if amount can't be turned into float, return error
            alert("Error: Deposit amount must be number")
        except TypeError:
            alert("Error: Enter amount")


def transactions_mode_off():
    modes["TRANSACTIONS"] = False


def view_transactions():
    modes["TRANSACTIONS"] = True
    # creates strings  containing transactions from the database
    full_report1 = ""
    full_report2 = ""
    full_report3 = ""
    counter = 0
    for i in categories:
        for transaction in categories[i]["TRANSACTIONS"]:
            if counter <= 20:
                full_report1 += f"{categories[i]['NAME']}: {transaction}\n"
                counter += 1
            elif counter <= 40:
                full_report2 += f"{categories[i]['NAME']}: {transaction}\n"
                counter += 1
            elif counter <= 60:
                full_report3 += f"{categories[i]['NAME']}: {transaction}\n"
                counter += 1
            elif counter == 61:
                full_report3 += f"...More than 60 transactions"
            else:
                break
    # alert
    t.penup()
    t.goto(500, 250)
    t.pendown()
    t.fillcolor((35, 36, 46))
    t.begin_fill()
    t.goto(500, 250)
    t.goto(500, -250)
    t.goto(-500, -250)
    t.goto(-500, 250)
    t.end_fill()
    t.penup()
    t.goto(-300, -200)
    t.color((65, 139, 166))
    t.write(full_report1, font=fonts[2], align="center")
    t.goto(-0, -200)
    t.write(full_report2, font=fonts[2], align="center")
    t.goto(300, -200)
    t.write(full_report3, font=fonts[2], align="center")
    t.color("black")
    while modes["TRANSACTIONS"]:
        stall(0.01)
        t.listen()
        t.onkey(transactions_mode_off, "Escape")
    t.clear()


def party_mode_off():
    modes["PARTY"] = False


def party_mode():
    # simple gif and text animation
    party_text = t.Turtle()
    party_text.hideturtle()
    party_text.penup()
    party_text.goto(0, 200)
    party_mode_t.showturtle()
    party_mode_t.goto(0, 0)
    modes["PARTY"] = True
    while modes["PARTY"]:
        for frame in range(1, 11):
            stall(0.01)
            party_mode_t.clear()
            party_text.clear()
            # colorful text
            red = r.randint(50, 255)
            green = r.randint(50, 255)
            blue = r.randint(50, 255)
            party_text.color((red, green, blue))
            party_text.write("PARTY MODE", font=fonts[0], align="center")
            # animated gif
            party_mode_t.shape("ag" + str(frame) + ".gif")
            t.tracer(True)
            t.tracer(False)
            t.listen()
            t.onkey(party_mode_off, "Escape")
    party_mode_t.shape("turtle")
    party_mode_t.hideturtle()
    party_text.clear()


def auto_budget():
    if user_assets["CATEGORIES"] > 0:
        alert("Auto-budget is only meant as starting point")
        aver_monthly_earning = t.textinput("Auto Budget", "Average Monthly Earning:")
        auto_dict = dict()
        budget_file = open("auto_budget.txt")
        budget_text_list = budget_file.readlines()
        for i in range(len(budget_text_list)):
            budget_text_list[i] = budget_text_list[i].replace("\n", "")
            budget_text_list[i] = budget_text_list[i].split(",")
        for line in budget_text_list:
            auto_dict[line[0]] = int(line[1])
        for category in categories:
            if categories[category]["NAME"].lower() in auto_dict:
                categories[category]["BUDGET"] = ((auto_dict[categories[category]["NAME"].lower()] / 100) *
                                                  float(aver_monthly_earning))
            else:
                categories[category]["BUDGET"] = (0.1) * float(aver_monthly_earning)
        # display budget
        budget_text.clear()
        for i in range(1, 7):
            try:
                if categories[i]["BUDGET"] == 0:
                    pass
            except KeyError:
                pass
            else:
                budget_text.color("white")
                if i == 1:
                    budget_text.goto(-140, -150)
                    budget_text.write("Budget: ${:.2f}".format(categories[1]["BUDGET"]), font=fonts[1])
                elif i == 2:
                    budget_text.goto(-140, -275)
                    budget_text.write("Budget: ${:.2f}".format(categories[2]["BUDGET"]), font=fonts[1])
                elif i == 3:
                    budget_text.goto(235, -150)
                    budget_text.write("Budget: ${:.2f}".format(categories[3]["BUDGET"]), font=fonts[1])
                elif i == 4:
                    budget_text.goto(235, -275)
                    budget_text.write("Budget: ${:.2f}".format(categories[4]["BUDGET"]), font=fonts[1])
    else:
        alert("Error: No categories made")


# mapping inputs to relating functions
def screen_nav(x, y):
    if (-600 < x < -425) and (150 < y < 200):
        create_category()
    elif (-600 < x < -425) and (100 < y < 150):
        view_transactions()
    elif (-600 < x < -425) and (50 < y < 100):
        savings_goal()
    elif (-600 < x < -425) and (0 < y < 50):
        set_budget()
    elif (-600 < x < -425) and (-50 < y < 0):
        monthly_expenses()
    elif (-600 < x < -425) and (-100 < y < -50):
        party_mode()
    elif (-600 < x < -425) and (-150 < y < -100):
        auto_budget()
    elif (-600 < x < -425) and (-200 < y < -150):
        store_data()
    if modes["BUDGET"]:
        if (-350 < x < -150) and (-170 < y < -70):
            budget_category[0] = 1
        elif (-350 < x < -150) and (-295 < y < -205):
            budget_category[0] = 2
        elif (25 < x < 225) and (-170 < y < -70):
            budget_category[0] = 3
        elif (25 < x < 225) and (-295 < y < -205):
            budget_category[0] = 4
    else:
        if (-350 < x < -150) and (-170 < y < -70) and user_assets["CATEGORIES"] >= 1:
            report_expense(1)
        elif (-350 < x < -150) and (-295 < y < -205) and user_assets["CATEGORIES"] >= 2:
            report_expense(2)
        elif (25 < x < 225) and (-170 < y < -70) and user_assets["CATEGORIES"] >= 3:
            report_expense(3)
        elif (25 < x < 225) and (-295 < y < -205) and user_assets["CATEGORIES"] == 4:
            report_expense(4)


def get_month_year():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    month_num = int(datetime.now().month) - 1
    return f"{months[month_num]}_{datetime.now().year}"


def store_data():
    database = open(get_month_year() + ".txt", "w")
    database.write(get_month_year() + "\n")
    report = f"{user_assets['TOTAL']}, {user_assets['CATEGORIES']}\n"
    database.write(report)
    report = f"{paid['EXPENSES']}, {paid['SAVINGS']}\n"
    database.write(report)
    for category in categories:
        report = f"{category}, {categories[category]['NAME']}, {categories[category]['SPENDING']}, {categories[category]['BUDGET']}"
        for transaction in categories[category]["TRANSACTIONS"]:
            report += f", {transaction}"
        database.write(report + "\n")
    database.close()
    alert("Data saved")
    stall(0.5)
    exit()


def open_data():
    database = open(get_month_year() + ".txt")
    database_list = database.readlines()
    for i in range(len(database_list)):
        database_list[i] = database_list[i].replace("\n", "")
        database_list[i] = database_list[i].split(", ")
    user_assets["TOTAL"] = float(database_list[1][0])
    user_assets["CATEGORIES"] = float(database_list[1][1])
    paid["EXPENSES"] = database_list[2][0] == "True"
    paid["SAVINGS"] = database_list[2][1] == "True"
    database_list = database_list[3:]
    for line in database_list:
        if len(line) > 4:
            temp_transactions = line[4:]
            temp_dict = {"NAME": line[1], "SPENDING": float(line[2]), "BUDGET": float(line[3]),
                         "TRANSACTIONS": temp_transactions}
        else:
            temp_dict = {"NAME": line[1], "SPENDING": float(line[2]), "BUDGET": float(line[3]), "TRANSACTIONS": list()}
        categories[int(line[0])] = temp_dict

    # display account total
    display_account_total()
    # display categories
    t.tracer(False)
    if user_assets["CATEGORIES"] == 1:  # displays all categories
        button.goto(-250, -125)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(-250, -140)
        text.color("white")
        text.write(categories[1]["NAME"], font=fonts[0], align="center")
        text.color("black")
    elif user_assets["CATEGORIES"] == 2:
        button.goto(-250, -125)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(-250, -140)
        text.color("white")
        text.write(categories[1]["NAME"], font=fonts[0], align="center")
        button.goto(-250, -250)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(-250, -265)
        text.write(categories[2]["NAME"], font=fonts[0], align="center")
        text.color("black")
    elif user_assets["CATEGORIES"] == 3:
        button.goto(-250, -125)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(-250, -140)
        text.color("white")
        text.write(categories[1]["NAME"], font=fonts[0], align="center")
        button.goto(-250, -250)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(-250, -265)
        text.write(categories[2]["NAME"], font=fonts[0], align="center")
        button.goto(125, -125)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(125, -140)
        text.write(categories[3]["NAME"], font=fonts[0], align="center")
        text.color("black")
    elif user_assets["CATEGORIES"] == 4:
        button.goto(-250, -125)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(-250, -140)
        text.color("white")
        text.write(categories[1]["NAME"], font=fonts[0], align="center")
        button.goto(-250, -250)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(-250, -265)
        text.write(categories[2]["NAME"], font=fonts[0], align="center")
        button.goto(125, -125)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(125, -140)
        text.write(categories[3]["NAME"], font=fonts[0], align="center")
        button.goto(125, -250)
        button.showturtle()
        button.stamp()
        button.hideturtle()
        text.goto(125, -265)
        text.write(categories[4]["NAME"], font=fonts[0], align="center")
        text.color("black")
    # display spending
    temp_text.color("white")
    if user_assets["CATEGORIES"] == 1:  # display spending amounts for each category
        temp_text.goto(-140, -120)
        temp_text.write("Spent: ${:.2f}".format(categories[1]["SPENDING"]), font=fonts[1])
    elif user_assets["CATEGORIES"] == 2:
        temp_text.goto(-140, -120)
        temp_text.write("Spent: ${:.2f}".format(categories[1]["SPENDING"]), font=fonts[1])
        temp_text.goto(-140, -245)
        temp_text.write("Spent: ${:.2f}".format(categories[2]["SPENDING"]), font=fonts[1])
    elif user_assets["CATEGORIES"] == 3:
        temp_text.goto(-140, -120)
        temp_text.write("Spent: ${:.2f}".format(categories[1]["SPENDING"]), font=fonts[1])
        temp_text.goto(-140, -245)
        temp_text.write("Spent: ${:.2f}".format(categories[2]["SPENDING"]), font=fonts[1])
        temp_text.goto(235, -120)
        temp_text.write("Spent: ${:.2f}".format(categories[3]["SPENDING"]), font=fonts[1])
    elif user_assets["CATEGORIES"] == 4:
        temp_text.goto(-140, -120)
        temp_text.write("Spent: ${:.2f}".format(categories[1]["SPENDING"]), font=fonts[1])
        temp_text.goto(-140, -245)
        temp_text.write("Spent: ${:.2f}".format(categories[2]["SPENDING"]), font=fonts[1])
        temp_text.goto(235, -120)
        temp_text.write("Spent: ${:.2f}".format(categories[3]["SPENDING"]), font=fonts[1])
        temp_text.goto(235, -245)
        temp_text.write("Spent: ${:.2f}".format(categories[4]["SPENDING"]), font=fonts[1])
    # display budget
    for i in categories:
        if categories[i]["BUDGET"] == 0:
            pass
        else:
            budget_text.color("white")
            if i == 1:
                budget_text.goto(-140, -150)
                budget_text.write("Budget: ${:.2f}".format(categories[1]["BUDGET"]), font=fonts[1])
            elif i == 2:
                budget_text.goto(-140, -275)
                budget_text.write("Budget: ${:.2f}".format(categories[2]["BUDGET"]), font=fonts[1])
            elif i == 3:
                budget_text.goto(235, -150)
                budget_text.write("Budget: ${:.2f}".format(categories[3]["BUDGET"]), font=fonts[1])
            elif i == 4:
                budget_text.goto(235, -275)
                budget_text.write("Budget: ${:.2f}".format(categories[4]["BUDGET"]), font=fonts[1])
    # display monthly expenses and savings
    if categories[5]["SPENDING"] != 0:
        expense_text.goto(500, 123)
        expense_text.color("white")
        expense_text.write("${:.2f}".format(float(categories[5]["SPENDING"])), font=fonts[0], align="center")
    if categories[6]["SPENDING"] != 0:
        savings_text.goto(500, -17)
        savings_text.color("white")
        savings_text.write("${:.2f}".format(float(categories[6]["SPENDING"])), font=fonts[0], align="center")
    pie.goto(-200, 110 - 140)
    pie.clear()
    key.clear()
    prev_x = pie.xcor()
    prev_y = pie.ycor()
    total_spending = 0
    for category in categories:
        total_spending += categories[category]["SPENDING"]
    for category in categories:
        if category == 1:
            pie.fillcolor("red")
        elif category == 2:
            pie.fillcolor("green")
        elif category == 3:
            pie.fillcolor("yellow")
        elif category == 4:
            pie.fillcolor("orange")
        elif category == 5:
            pie.fillcolor("purple")
        elif category == 6:
            pie.fillcolor("ivory")
        pie.pendown()
        pie.begin_fill()
        pie.circle(140, (categories[category]["SPENDING"] / total_spending) * 360)
        prev_x_temp = pie.xcor()
        prev_y_temp = pie.ycor()
        if (categories[category]["SPENDING"] / total_spending) * 360 != 360:
            pie.goto(-200, 110)
            pie.goto(prev_x, prev_y)
        pie.end_fill()
        pie.penup()
        prev_x = prev_x_temp
        prev_y = prev_y_temp
        pie.goto(prev_x, prev_y)
    for category in categories:
        if category == 1:
            key.fillcolor("red")
        elif category == 2:
            key.fillcolor("green")
        elif category == 3:
            key.fillcolor("yellow")
        elif category == 4:
            key.fillcolor("orange")
        elif category == 5:
            key.fillcolor("purple")
        elif category == 6:
            key.fillcolor("ivory")
        key.showturtle()
        key.goto(0, 200 - (20 * int(category)))
        key.setheading(0)
        key.stamp()
        key.hideturtle()
        key.goto(10, 200 - (20 * int(category)) - 10)
        key.write(categories[category]["NAME"], font=fonts[2])
