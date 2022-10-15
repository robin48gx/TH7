
from guizero import App, Text, TextBox, PushButton, Slider, Picture

def change_text_size(slider_value):
    welcome_message.size = slider_value
def say_my_name():
    welcome_message.value = my_name.value

app = App(title="Hello World")
welcome_message = Text(app, text="Welcome to my app")
my_name = TextBox(app)
update_text = PushButton(app, command=say_my_name, text="Display my name");
tex_size = Slider(app, command=change_text_size, start=10, end=20)
my_cat = Picture(app, image="dog.png")
app.display()

