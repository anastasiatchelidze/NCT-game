import turtle
import pandas

screen = turtle.Screen()
screen.title("Nct ot23 Game")
screen.setup(width=0.8, height=0.8)
image = "nct_ot23.gif"
screen.addshape(image)  # using image as a background
turtle.shape(image)

data = pandas.read_csv("nct_database.csv")
nct_members = data.name.to_list()  # converting csv name column to a list

guessed_members = []
score = 0

while score < 23:

    guess = turtle.textinput(title=f"{score}/23 members correct", prompt="Enter NCT member's name:").title()

    if guess == "Exit":
        break

    if guess in nct_members:
        if guess in guessed_members:
            continue
        guessed_members.append(guess)
        score += 1
        guessed_member = data[data.name == guess]
        member_t = turtle.Turtle()
        member_t.hideturtle()
        member_t.penup()
        member_t.goto(int(guessed_member.x), int(guessed_member.y))
        member_t.write(arg=guess, align="center", font=('Georgia', 20, 'bold'))

# Storing members' names which weren't guessed into a csv file
if score != 23:
    missing_members = [member for member in nct_members if member not in guessed_members]  # List Comprehension
    df = pandas.DataFrame(missing_members)
    df.to_csv("missed_members.csv")