import kivy
kivy.require("1.2.0")
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.boxlayout  import BoxLayout

#this line we will use later to make a link to another kv
'''
class Mainwin(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__( **kwargs)
'''
    
class Mainapp(App):
    def build(self):
        return Label(text="Hello kamel altohamy")



if __name__ == "__main__":
    Mainapp().run()
