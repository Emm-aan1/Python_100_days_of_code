from turtle import Turtle, Screen
from prettytable import PrettyTable


# # Turtle
# derrick = Turtle()
# derrick.shape('turtle')
# derrick.color('goldenrod')
# derrick.forward(245)
# derrick.left(180)
# derrick.forward(379)
#
# derrick_screen = Screen()
# print(derrick_screen.canvheight)
# derrick_screen.exitonclick()


# PrettyTable
table = PrettyTable()
table.add_column("Igbo Places", ['Anambra', 'Enugu', 'Abia', 'Owerri', 'Delta'])
table.add_column("Ibo Names", ['Amaka', 'Chinaza', 'Uche', 'Ebube', 'Ebuka'])
table.align = 'l'
print(table)
