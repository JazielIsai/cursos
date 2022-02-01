from guizero import App, Text, TextBox, PushButton, Silder, Picture, Window

app= App(title="GUI 1", width=1000, height =500, layout="grid")

Year = Text(app, text="Ingrese Year", font="Times new Roman", size=15, color="#80d2d2", grid=[0,0]. align="left")
Year1 = Text(app, width=10, grid=[1,0]. align="left")

espacio= Text(app, text="      ", font="Times new Roman", size=15, color="#80d2d2", grid=[2,0], align="left")

Edad = Text(app, text="Ingrese Edad", font="Times new Roman", size=15, color="#80d2d2", grid=[0,1]. align="left")
Edad1 = Text(app, width=10, grid=[1,1]. align="left")

dato = PushButton(app, command="say_data", text="Display dato", grid=[1,3], align="left")

my_cat = Picture(app, image="Titulacion1.gif", grid=[8,10], align="left")