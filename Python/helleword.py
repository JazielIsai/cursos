from guizero import App, Text, TextBox, PushButton, Silder, Picture

def say_my_name():
    welcome_message.value= my_name.value
    
app= App(title = "Hello World")

welcome_message = Text(app, text="Welcome to my App, write your name", size=15, font="Times new Roman", color='#80d202')
my_name = TextBox(app, width="10")

update_text= PushButton(app, command= say_my_name, text="Display my name")
text_size = Silder(app, command=change_text_size, start=10, end=80)

my_cat= Picture(app, image="RaspberryPi_logo.gif")

app.display()